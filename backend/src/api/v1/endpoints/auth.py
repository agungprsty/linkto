import secrets
from typing import Optional

from fastapi import APIRouter, Cookie, Depends, HTTPException, Request, Response
from fastapi.responses import RedirectResponse

from src.core.config import settings
from src.core.deps import get_current_user
from src.core.exceptions import BadRequestException
from src.models.user import User
from src.schemas.auth import (
    GoogleAuthRequest,
    LoginRequest,
    RefreshTokenRequest,
    RegisterRequest,
    TokenResponse,
    UserResponse,
)
from src.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


def _set_refresh_token_cookie(response: Response, refresh_token: str) -> None:
    """Set refresh token as httpOnly secure cookie."""
    max_age = settings.jwt_refresh_expire_seconds
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        max_age=max_age,
        httponly=True,
        samesite="lax",
        secure=settings.app_env != "development",
        path="/api/v1/auth",
    )


def _set_access_token_cookie(response: Response, access_token: str) -> None:
    """Set access token as cookie (not httpOnly so JS can read)."""
    max_age = settings.jwt_access_expire_seconds
    response.set_cookie(
        key="access_token",
        value=access_token,
        max_age=max_age,
        httponly=False,
        samesite="lax",
        secure=settings.app_env != "development",
        path="/",
    )


def _clear_auth_cookies(response: Response) -> None:
    """Clear auth cookies."""
    response.delete_cookie(key="access_token", path="/")
    response.delete_cookie(key="refresh_token", path="/api/v1/auth")


@router.post("/register", response_model=dict, status_code=201)
async def register(req: RegisterRequest, response: Response):
    """Register a new user account."""
    result = await AuthService.register(req)
    _set_refresh_token_cookie(response, result["refresh_token"])
    _set_access_token_cookie(response, result["access_token"])
    return result


@router.post("/login", response_model=dict)
async def login(req: LoginRequest, response: Response):
    """Authenticate with email and password."""
    result = await AuthService.login(req)
    _set_refresh_token_cookie(response, result["refresh_token"])
    _set_access_token_cookie(response, result["access_token"])
    return result


@router.post("/refresh", response_model=dict)
async def refresh_token(
    req: Optional[RefreshTokenRequest] = None,
    response: Response = None,
    refresh_token: Optional[str] = Cookie(None),
):
    """Get a new access token using a refresh token.

    Accepts refresh token in request body or httpOnly cookie.
    """
    # Try body first, then cookie
    token_str = None
    if req and req.refresh_token:
        token_str = req.refresh_token
    elif refresh_token:
        token_str = refresh_token

    if not token_str:
        raise BadRequestException("Refresh token is required")

    result = await AuthService.refresh_token(token_str)
    _set_refresh_token_cookie(response, result["refresh_token"])
    _set_access_token_cookie(response, result["access_token"])
    return result


@router.post("/google", response_model=dict)
async def google_auth(req: GoogleAuthRequest, response: Response):
    """Authenticate or register with Google OAuth (client-side token flow)."""
    result = await AuthService.google_auth(req.id_token, req.username)
    _set_refresh_token_cookie(response, result["refresh_token"])
    _set_access_token_cookie(response, result["access_token"])
    return result


@router.get("/google/login")
async def google_login():
    """Redirect user to Google's OAuth consent screen.

    Use this endpoint for server-side OAuth flow.
    After consent, Google redirects to /google/callback.
    """
    if not settings.google_client_id:
        raise HTTPException(status_code=501, detail="Google OAuth not configured")

    # Generate a random state for CSRF protection
    state = secrets.token_urlsafe(32)
    # In production, store state in session/cache to verify on callback
    login_url = AuthService.get_google_login_url(state)
    return RedirectResponse(url=login_url)


@router.get("/google/callback", response_model=dict)
async def google_callback(code: str, state: Optional[str] = None, response: Response = None):
    """Handle Google OAuth callback.

    Google redirects here after user consent with an authorization code.
    The code is exchanged for tokens, and the user is authenticated/created.
    """
    if not code:
        raise BadRequestException("Missing authorization code")

    try:
        result = await AuthService.handle_google_callback(code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    _set_refresh_token_cookie(response, result["refresh_token"])
    _set_access_token_cookie(response, result["access_token"])
    return result


@router.post("/logout")
async def logout(
    response: Response,
    current_user: Optional[User] = Depends(get_current_user),
):
    """Logout — clear auth cookies."""
    _clear_auth_cookies(response)
    return {"message": "Logged out successfully"}


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    """Get the currently authenticated user's profile."""
    return current_user
