"""Pydantic schemas for public bio page responses."""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator


class BioLinkResponse(BaseModel):
    """Response schema for a single link on the public bio page."""

    id: str
    title: str
    url: str
    type: str = "standard"
    image_url: Optional[str] = None
    sort_order: int = 0

    @field_validator("id", mode="before")
    @classmethod
    def coerce_id(cls, v):
        return str(v) if v else v

    class Config:
        from_attributes = True


class BioProfileResponse(BaseModel):
    """Response schema for the public bio profile section."""

    full_name: Optional[str] = None
    bio: Optional[str] = None
    avatar_url: Optional[str] = None


class BioThemeResponse(BaseModel):
    """Response schema for the public bio theme section."""

    background_color: str = "#ffffff"
    button_style: str = "rounded"
    button_color: str = "#000000"
    font_family: str = "Inter"


class BioResponse(BaseModel):
    """Public bio page response — accessible without authentication.

    Contains the user's public profile, theme settings, and active links.
    """

    username: str
    profile: BioProfileResponse = BioProfileResponse()
    theme: BioThemeResponse = BioThemeResponse()
    links: List[BioLinkResponse] = []

    @field_validator("profile", mode="before")
    @classmethod
    def coerce_profile(cls, v):
        if hasattr(v, "model_dump"):
            return v.model_dump()
        return v if isinstance(v, dict) else {}

    @field_validator("theme", mode="before")
    @classmethod
    def coerce_theme(cls, v):
        if hasattr(v, "model_dump"):
            return v.model_dump()
        return v if isinstance(v, dict) else {}

    class Config:
        from_attributes = True


class ErrorResponse(BaseModel):
    """Standard error response."""

    detail: dict
