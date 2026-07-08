from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator
import re


class RegisterRequest(BaseModel):
    """Request schema for user registration.

    Only requires email and password.
    Username is auto-generated using ULID for uniqueness.
    """

    email: EmailStr = Field(..., description="User email address")
    password: str = Field(..., min_length=8, max_length=128, description="Password (min 8 chars)")

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        """Password must have at least one letter and one digit."""
        if not re.search(r"[A-Za-z]", v):
            raise ValueError("Password must contain at least one letter")
        if not re.search(r"[0-9]", v):
            raise ValueError("Password must contain at least one digit")
        return v


class LoginRequest(BaseModel):
    """Request schema for user login."""

    email: EmailStr = Field(..., description="User email address")
    password: str = Field(..., description="User password")


class GoogleAuthRequest(BaseModel):
    """Request schema for Google OAuth authentication."""

    id_token: str = Field(..., description="Google ID token from the client")
    username: Optional[str] = Field(
        default=None, min_length=3, max_length=30,
        description="Optional username for new users (auto-generated if not provided)",
    )


class RefreshTokenRequest(BaseModel):
    """Request schema for token refresh."""

    refresh_token: Optional[str] = Field(default=None, description="Refresh token")


class TokenResponse(BaseModel):
    """Response schema for successful authentication."""

    access_token: str = Field(..., description="JWT access token")
    refresh_token: str = Field(..., description="JWT refresh token")
    token_type: str = "bearer"
    expires_in: int = Field(..., description="Access token TTL in seconds")


class UserResponse(BaseModel):
    """Response schema for user data (public-safe)."""

    id: str
    username: str
    email: str
    profile: dict = {}
    theme: dict = {}
    tier: str = "free"
    is_active: bool = True
    email_verified: bool = False
    created_at: datetime
    updated_at: datetime

    @field_validator("id", mode="before")
    @classmethod
    def coerce_id(cls, v):
        """Convert ObjectId/PydanticObjectId to string."""
        return str(v) if v else v

    @field_validator("profile", "theme", mode="before")
    @classmethod
    def coerce_embedded_model(cls, v):
        """Convert Beanie embedded models to dicts."""
        if hasattr(v, "model_dump"):
            return v.model_dump()
        return v if isinstance(v, dict) else {}

    class Config:
        from_attributes = True


class UserProfileResponse(BaseModel):
    """Lightweight user profile response."""

    username: str
    profile: dict = {}
    tier: str = "free"


class ErrorResponse(BaseModel):
    """Standard error response."""

    detail: dict


class ErrorDetail(BaseModel):
    """Error detail structure."""

    code: str
    message: str
    details: dict | None = None
