import secrets
from datetime import datetime, timezone
from typing import Optional

from httpx import AsyncClient

from src.core.config import settings
from src.core.exceptions import (
    BadRequestException,
    DuplicateException,
    NotFoundException,
    UnauthorizedException,
)
from src.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password,
    verify_token,
)
from src.core.utils import generate_id
from src.models.user import User
from src.schemas.auth import RegisterRequest, LoginRequest


class AuthService:
    """Business logic for authentication operations."""

    @staticmethod
    async def register(req: RegisterRequest) -> dict:
        """Register a new user with email and password.

        Username is auto-generated using ULID for guaranteed uniqueness.
        """
        # Check if email already exists
        existing_email = await User.find_one(User.email == req.email)
        if existing_email:
            raise DuplicateException("User", "email")

        # Generate unique username using ULID
        username = generate_id()
        while await User.find_one(User.username == username):
            username = generate_id()

        # Create user
        user = User(
            username=username,
            email=req.email,
            password_hash=hash_password(req.password),
        )
        await user.insert()

        # Generate tokens
        access_token = create_access_token(subject=str(user.id))
        refresh_token = create_refresh_token(subject=str(user.id))

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": settings.jwt_access_expire_seconds,
            "user": {
                "id": str(user.id),
                "username": user.username,
                "email": user.email,
                "profile": user.profile.model_dump() if user.profile else {},
                "tier": user.tier,
            },
        }

    @staticmethod
    async def login(req: LoginRequest) -> dict:
        """Authenticate user with email and password."""
        user = await User.find_one(User.email == req.email)
        if not user:
            raise UnauthorizedException("Invalid email or password")

        if not user.password_hash:
            raise UnauthorizedException(
                "This account uses Google login. Please sign in with Google."
            )

        if not verify_password(req.password, user.password_hash or ""):
            raise UnauthorizedException("Invalid email or password")

        if not user.is_active:
            raise UnauthorizedException("Account is deactivated")

        # Update last login
        user.updated_at = datetime.now(timezone.utc)
        await user.save()

        # Generate tokens
        access_token = create_access_token(subject=str(user.id))
        refresh_token = create_refresh_token(subject=str(user.id))

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": settings.jwt_access_expire_seconds,
            "user": {
                "id": str(user.id),
                "username": user.username,
                "email": user.email,
                "profile": user.profile.model_dump() if user.profile else {},
                "tier": user.tier,
            },
        }

    @staticmethod
    async def refresh_token(refresh_token_str: str) -> dict:
        """Issue a new access token using a valid refresh token."""
        try:
            payload = verify_token(refresh_token_str, expected_type="refresh")
            user_id = payload.get("sub", "")
            if not user_id:
                raise UnauthorizedException("Invalid refresh token")
        except ValueError as e:
            raise UnauthorizedException(str(e))

        user = await User.get(user_id)
        if not user:
            raise UnauthorizedException("User not found")

        if not user.is_active:
            raise UnauthorizedException("Account is deactivated")

        # Issue new tokens (rotation)
        new_access_token = create_access_token(subject=str(user.id))
        new_refresh_token = create_refresh_token(subject=str(user.id))

        return {
            "access_token": new_access_token,
            "refresh_token": new_refresh_token,
            "token_type": "bearer",
            "expires_in": settings.jwt_access_expire_seconds,
        }

    @staticmethod
    async def google_auth(id_token: str, username: Optional[str] = None) -> dict:
        """Authenticate or register user with Google OAuth.

        Verifies the Google ID token, then either logs in an existing user
        or creates a new account.
        """
        # Verify Google ID token
        google_user = await AuthService._verify_google_token(id_token)
        if not google_user:
            raise UnauthorizedException("Invalid Google token")

        google_email = google_user.get("email", "")
        google_name = google_user.get("name", "")
        google_id = google_user.get("sub", "")
        google_picture = google_user.get("picture", "")

        if not google_email:
            raise BadRequestException("Google account has no email")

        # Check if user exists with this Google ID or email
        user = await User.find_one(
            User.google_id == google_id
        ) or await User.find_one(User.email == google_email)

        if user:
            # Existing user — update Google ID if not set
            if not user.google_id:
                user.google_id = google_id
                user.email_verified = True
                if google_picture and not user.profile.avatar_url:
                    user.profile.avatar_url = google_picture
                user.updated_at = datetime.now(timezone.utc)
                await user.save()

            # Generate tokens
            access_token = create_access_token(subject=str(user.id))
            refresh_token = create_refresh_token(subject=str(user.id))

            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "bearer",
                "expires_in": settings.jwt_access_expire_seconds,
                "user": {
                    "id": str(user.id),
                    "username": user.username,
                    "email": user.email,
                    "profile": user.profile.model_dump() if user.profile else {},
                    "tier": user.tier,
                },
            }

        # New user — create account
        # Generate unique username if not provided
        final_username = username or await AuthService._generate_username(google_name, google_email)

        # Ensure username is unique
        while await User.find_one(User.username == final_username):
            final_username = await AuthService._generate_username(google_name, google_email)

        user = User(
            username=final_username,
            email=google_email,
            google_id=google_id,
            password_hash=None,
            email_verified=True,
            profile={
                "full_name": google_name,
                "avatar_url": google_picture,
            },
        )
        await user.insert()

        # Generate tokens
        access_token = create_access_token(subject=str(user.id))
        refresh_token = create_refresh_token(subject=str(user.id))

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": settings.jwt_access_expire_seconds,
            "user": {
                "id": str(user.id),
                "username": user.username,
                "email": user.email,
                "profile": user.profile.model_dump() if user.profile else {},
                "tier": user.tier,
            },
        }

    @staticmethod
    def get_google_login_url(state: str) -> str:
        """Generate Google OAuth authorization URL."""
        params = {
            "client_id": settings.google_client_id or "",
            "redirect_uri": settings.google_redirect_uri,
            "response_type": "code",
            "scope": "openid email profile",
            "access_type": "offline",
            "state": state,
        }
        import urllib.parse
        return f"https://accounts.google.com/o/oauth2/v2/auth?{urllib.parse.urlencode(params)}"

    @staticmethod
    async def handle_google_callback(code: str) -> dict:
        """Exchange authorization code for tokens and authenticate user.

        Steps:
        1. Exchange code for Google tokens (ID token + access token)
        2. Verify the ID token
        3. Find or create user
        4. Return our own JWT tokens
        """
        if not settings.google_client_id or not settings.google_client_secret:
            raise ValueError("Google OAuth is not configured on the server")

        # Exchange code for tokens
        token_data = {
            "code": code,
            "client_id": settings.google_client_id,
            "client_secret": settings.google_client_secret,
            "redirect_uri": settings.google_redirect_uri,
            "grant_type": "authorization_code",
        }
        try:
            async with AsyncClient() as client:
                token_resp = await client.post(
                    "https://oauth2.googleapis.com/token",
                    data=token_data,
                    timeout=10,
                )
                if token_resp.status_code != 200:
                    raise UnauthorizedException("Failed to exchange Google code")
                token_json = token_resp.json()
        except Exception:
            raise UnauthorizedException("Failed to exchange Google code")

        id_token_str = token_json.get("id_token")
        if not id_token_str:
            raise UnauthorizedException("No ID token in Google response")

        # Verify the ID token and get user info by calling Google's tokeninfo
        id_info = await AuthService._verify_google_token(id_token_str)
        if not id_info:
            raise UnauthorizedException("Invalid Google ID token")

        google_email = id_info.get("email", "")
        google_name = id_info.get("name", "")
        google_id = id_info.get("sub", "")
        google_picture = id_info.get("picture", "")

        if not google_email:
            raise BadRequestException("Google account has no email")

        # Find or create user
        user = await User.find_one(
            User.google_id == google_id
        ) or await User.find_one(User.email == google_email)

        if user:
            # Existing user — update Google ID if not set
            if not user.google_id:
                user.google_id = google_id
                user.email_verified = True
                if google_picture and not user.profile.avatar_url:
                    user.profile.avatar_url = google_picture
                user.updated_at = datetime.now(timezone.utc)
                await user.save()
        else:
            # New user
            final_username = await AuthService._generate_username(google_name, google_email)
            while await User.find_one(User.username == final_username):
                final_username = await AuthService._generate_username(google_name, google_email)

            user = User(
                username=final_username,
                email=google_email,
                google_id=google_id,
                password_hash=None,
                email_verified=True,
                profile={
                    "full_name": google_name,
                    "avatar_url": google_picture,
                },
            )
            await user.insert()

        # Generate our own tokens
        access_token = create_access_token(subject=str(user.id))
        refresh_token = create_refresh_token(subject=str(user.id))

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": settings.jwt_access_expire_seconds,
            "user": {
                "id": str(user.id),
                "username": user.username,
                "email": user.email,
                "profile": user.profile.model_dump() if user.profile else {},
                "tier": user.tier,
            },
        }

    @staticmethod
    async def _verify_google_token(id_token: str) -> Optional[dict]:
        """Verify a Google ID token by calling Google's tokeninfo endpoint."""
        try:
            async with AsyncClient() as client:
                response = await client.get(
                    "https://oauth2.googleapis.com/tokeninfo",
                    params={"id_token": id_token},
                    timeout=10,
                )
                if response.status_code != 200:
                    return None
                return response.json()
        except Exception:
            return None

    @staticmethod
    async def _generate_username(name: str, email: str) -> str:
        """Generate a unique username from name or email."""
        # Try to derive from email first
        base = email.split("@")[0].lower()
        # Remove non-alphanumeric characters
        base = "".join(c for c in base if c.isalnum() or c in "_-")
        # Ensure it's at least 3 characters
        if len(base) < 3:
            base = f"user{secrets.token_hex(2)}"
        # Truncate if too long
        base = base[:28]
        # Add random suffix for uniqueness
        suffix = secrets.token_hex(2)
        return f"{base}_{suffix}"

    @staticmethod
    async def get_user_by_id(user_id: str) -> User:
        """Get user by ID."""
        user = await User.get(user_id)
        if not user:
            raise NotFoundException("User", user_id)
        return user

    @staticmethod
    async def get_user_by_username(username: str) -> User:
        """Get user by username."""
        user = await User.find_one(User.username == username)
        if not user:
            raise NotFoundException("User", username)
        return user

    @staticmethod
    async def update_profile(
        user: User,
        full_name: Optional[str] = None,
        bio: Optional[str] = None,
        avatar_url: Optional[str] = None,
    ) -> User:
        """Update user profile fields."""
        if full_name is not None:
            user.profile.full_name = full_name
        if bio is not None:
            user.profile.bio = bio
        if avatar_url is not None:
            user.profile.avatar_url = avatar_url
        user.updated_at = datetime.now(timezone.utc)
        await user.save()
        return user
