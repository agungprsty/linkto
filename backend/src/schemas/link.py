from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, Field, field_validator


class CreateLinkRequest(BaseModel):
    """Request schema for creating a new link."""

    title: str = Field(..., min_length=1, max_length=200)
    url: str = Field(..., max_length=2048)
    type: Literal["standard", "affiliate_product"] = "standard"
    image_url: Optional[str] = Field(default=None, max_length=2048)

    @field_validator("url")
    @classmethod
    def validate_url(cls, v: str) -> str:
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


class UpdateLinkRequest(BaseModel):
    """Request schema for updating an existing link (partial update)."""

    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    url: Optional[str] = Field(default=None, max_length=2048)
    type: Optional[Literal["standard", "affiliate_product"]] = None
    image_url: Optional[str] = Field(default=None, max_length=2048)
    sort_order: Optional[int] = Field(default=None, ge=0)
    is_active: Optional[bool] = None

    @field_validator("url")
    @classmethod
    def validate_url(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
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


class LinkResponse(BaseModel):
    """Response schema for a single link."""

    id: str
    title: str
    url: str
    type: str
    image_url: Optional[str] = None
    sort_order: int = 0
    is_active: bool = True
    created_at: datetime
    updated_at: datetime

    @field_validator("id", mode="before")
    @classmethod
    def coerce_id(cls, v):
        return str(v) if v else v

    class Config:
        from_attributes = True


class ReorderItem(BaseModel):
    """Single item in a reorder request."""

    id: str
    sort_order: int = Field(..., ge=0)


class ReorderLinksRequest(BaseModel):
    """Request schema for batch reordering links."""

    items: List[ReorderItem]
