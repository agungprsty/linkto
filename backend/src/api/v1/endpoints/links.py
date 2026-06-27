from typing import List

from fastapi import APIRouter, Depends

from src.core.deps import get_current_user
from src.models.user import User
from src.schemas.link import (
    CreateLinkRequest,
    LinkResponse,
    ReorderLinksRequest,
    UpdateLinkRequest,
)
from src.services.link_service import LinkService

router = APIRouter(prefix="/links", tags=["Links"])


@router.get("", response_model=List[LinkResponse])
async def list_links(current_user: User = Depends(get_current_user)):
    """Get all links for the authenticated user (sorted by sort_order)."""
    links = await LinkService.get_user_links(str(current_user.id))
    return links


@router.post("", response_model=LinkResponse, status_code=201)
async def create_link(
    req: CreateLinkRequest,
    current_user: User = Depends(get_current_user),
):
    """Create a new link."""
    link = await LinkService.create_link(str(current_user.id), req)
    return link


@router.put("/reorder", response_model=List[LinkResponse])
async def reorder_links(
    req: ReorderLinksRequest,
    current_user: User = Depends(get_current_user),
):
    """Batch reorder links (update sort_order for multiple links at once)."""
    links = await LinkService.reorder_links(str(current_user.id), req.items)
    return links


@router.put("/{link_id}", response_model=LinkResponse)
async def update_link(
    link_id: str,
    req: UpdateLinkRequest,
    current_user: User = Depends(get_current_user),
):
    """Update a link (partial update: title, url, type, image_url, sort_order, is_active)."""
    link = await LinkService.update_link(link_id, str(current_user.id), req)
    return link


@router.delete("/{link_id}", status_code=204)
async def delete_link(
    link_id: str,
    current_user: User = Depends(get_current_user),
):
    """Delete a link (hard delete)."""
    await LinkService.delete_link(link_id, str(current_user.id))
