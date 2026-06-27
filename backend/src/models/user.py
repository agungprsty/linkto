from datetime import datetime, timezone
from typing import Optional, Literal

from beanie import Document, Indexed
from pydantic import BaseModel, Field


class ProfileModel(BaseModel):
    """Embedded profile model for user's public profile."""
    full_name: Optional[str] = None
    bio: Optional[str] = None
    avatar_url: Optional[str] = None


class ThemeModel(BaseModel):
    """Embedded theme customization model."""
    background_color: str = "#ffffff"
    button_style: str = "rounded"
    button_color: str = "#000000"
    font_family: str = "Inter"


class User(Document):
    """User document model."""

    username: str = Indexed(unique=True)
    email: str = Indexed(unique=True)
    password_hash: Optional[str] = None
    google_id: Optional[str] = None

    profile: ProfileModel = Field(default_factory=ProfileModel)
    theme: ThemeModel = Field(default_factory=ThemeModel)

    tier: Literal["free", "pro", "business"] = "free"

    is_active: bool = True
    email_verified: bool = False

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "users"
        indexes = [
            [("username", 1)],  # unique
            [("email", 1)],     # unique
        ]

    async def update_timestamp(self) -> None:
        """Update the updated_at timestamp."""
        self.updated_at = datetime.now(timezone.utc)

    class Config:
        json_schema_extra = {
            "example": {
                "username": "agung_dev",
                "email": "user@example.com",
                "profile": {
                    "full_name": "Agung Prasetyo",
                    "bio": "Backend Engineer | Tech Enthusiast",
                    "avatar_url": "https://storage.com/avatar.jpg",
                },
                "tier": "free",
            }
        }
