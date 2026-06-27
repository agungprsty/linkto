from typing import Optional

from fastapi import Depends, Request
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError

from src.core.exceptions import UnauthorizedException
from src.core.security import verify_token
from src.models.user import User

# Global HTTP Bearer scheme — tells Swagger that /me etc. need Bearer token.
# Swagger shows a simple input field to paste the token (not a login form).
bearer_scheme = HTTPBearer(auto_error=False)


def _extract_token(
    credentials: Optional[HTTPAuthorizationCredentials],
    request: Request,
) -> Optional[str]:
    """Extract Bearer token from Authorization header or fallback to cookie."""
    if credentials is not None:
        return credentials.credentials
    # Fallback: read from httpOnly cookie (not shown in Swagger docs)
    return request.cookies.get("access_token")


async def get_current_user(
    request: Request,
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(bearer_scheme),
) -> User:
    """Dependency: extract current authenticated user from JWT.

    Checks Authorization header first (via HTTPBearer),
    then falls back to access_token cookie (hidden from Swagger docs).
    """
    token_str = _extract_token(credentials, request)

    if not token_str:
        raise UnauthorizedException("Not authenticated")

    try:
        payload = verify_token(token_str, expected_type="access")
        user_id: str = payload.get("sub", "")
        if not user_id:
            raise UnauthorizedException("Invalid token payload")
    except (JWTError, ValueError):
        raise UnauthorizedException("Invalid or expired token")

    user = await User.get(user_id)
    if not user:
        raise UnauthorizedException("User not found")

    return user


async def get_optional_user(
    request: Request,
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(bearer_scheme),
) -> Optional[User]:
    """Dependency: extract user if authenticated, but don't require it."""
    token_str = _extract_token(credentials, request)

    if not token_str:
        return None

    try:
        payload = verify_token(token_str, expected_type="access")
        user_id: str = payload.get("sub", "")
        if not user_id:
            return None
        user = await User.get(user_id)
        return user
    except (JWTError, ValueError):
        return None
