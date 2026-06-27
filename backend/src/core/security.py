import uuid
from datetime import datetime, timedelta, timezone
from typing import Any, Optional

import bcrypt
from jose import JWTError, jwt

from src.core.config import settings


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain text password against a bcrypt hash."""
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8"),
    )


def hash_password(password: str) -> str:
    """Hash a plain text password using bcrypt."""
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode("utf-8")


def create_access_token(
    subject: str,
    extra_claims: Optional[dict[str, Any]] = None,
) -> str:
    """Create a JWT access token (short-lived)."""
    now = datetime.now(timezone.utc)
    expire = now + timedelta(seconds=settings.jwt_access_expire_seconds)
    to_encode = {
        "sub": subject,
        "exp": expire,
        "type": "access",
        "iat": now,
        "jti": uuid.uuid4().hex,
    }
    if extra_claims:
        to_encode.update(extra_claims)
    return jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def create_refresh_token(subject: str) -> str:
    """Create a JWT refresh token (long-lived)."""
    now = datetime.now(timezone.utc)
    expire = now + timedelta(seconds=settings.jwt_refresh_expire_seconds)
    to_encode = {
        "sub": subject,
        "exp": expire,
        "type": "refresh",
        "iat": now,
        "jti": uuid.uuid4().hex,
    }
    return jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)


def decode_token(token: str) -> dict[str, Any]:
    """Decode and validate a JWT token. Returns the payload."""
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm],
        )
        return payload
    except JWTError:
        raise ValueError("Invalid or expired token")


def verify_token(token: str, expected_type: str = "access") -> dict[str, Any]:
    """Verify a JWT token and check its type."""
    payload = decode_token(token)
    if payload.get("type") != expected_type:
        raise ValueError(f"Invalid token type. Expected '{expected_type}'.")
    return payload
