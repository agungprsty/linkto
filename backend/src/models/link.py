from datetime import datetime, timezone
from typing import Literal, Optional

from beanie import Document, Indexed
from pydantic import Field, field_validator


class Link(Document):
    """User link document model.

    Supports two types:
    - `standard`: simple button with title + URL
    - `affiliate_product`: card with product image, title, and affiliate URL
    """

    user_id: str = Indexed()
    title: str = Field(..., min_length=1, max_length=200)
    url: str = Field(..., max_length=2048)
    type: Literal["standard", "affiliate_product"] = "standard"
    image_url: Optional[str] = Field(default=None, max_length=2048)
    sort_order: int = Field(default=0, ge=0)
    is_active: bool = True

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator("url")
    @classmethod
    def validate_url(cls, v: str) -> str:
        """Basic URL validation — ensure it starts with http:// or https://."""
        v = v.strip()
        if not v.startswith(("http://", "https://")):
            raise ValueError("URL must start with http:// or https://")
        return v

    @field_validator("image_url")
    @classmethod
    def validate_image_url(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            v = v.strip()
            if v and not v.startswith(("http://", "https://")):
                raise ValueError("Image URL must start with http:// or https://")
        return v

    class Settings:
        name = "links"
        indexes = [
            [("user_id", 1), ("sort_order", 1)],  # fast sorted queries per user
            [("user_id", 1)],  # basic user lookup
        ]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Portfolio Github",
                "url": "https://github.com/username",
                "type": "standard",
                "sort_order": 1,
            }
        }
