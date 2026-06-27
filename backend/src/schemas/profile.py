from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field, field_validator


class UpdateProfileRequest(BaseModel):
    """Request schema for updating user profile and theme."""

    # Profile fields
    full_name: Optional[str] = Field(default=None, max_length=100)
    bio: Optional[str] = Field(default=None, max_length=500)
    avatar_url: Optional[str] = Field(default=None, max_length=2048)

    # Theme fields
    background_color: Optional[str] = Field(default=None, pattern=r"^#[0-9a-fA-F]{6}$")
    button_style: Optional[Literal["rounded", "pill", "soft"]] = None
    button_color: Optional[str] = Field(default=None, pattern=r"^#[0-9a-fA-F]{6}$")
    font_family: Optional[str] = Field(default=None, max_length=100)

    @field_validator("avatar_url")
    @classmethod
    def validate_avatar_url(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            v = v.strip()
            if v and not v.startswith(("http://", "https://")):
                raise ValueError("avatar_url must start with http:// or https://")
        return v


class UserProfileResponse(BaseModel):
    """Response schema for user profile (full data, for the owner)."""

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
