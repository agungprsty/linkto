from datetime import datetime, timezone
from typing import List, Optional

from src.core.exceptions import NotFoundException
from src.models.link import Link
from src.schemas.link import CreateLinkRequest, ReorderItem, UpdateLinkRequest


class LinkService:
    """Business logic for link management."""

    @staticmethod
    async def get_user_links(user_id: str) -> List[Link]:
        """Get all links for a user, sorted by sort_order."""
        links = await Link.find(
            Link.user_id == user_id,
        ).sort(Link.sort_order).to_list()
        return links

    @staticmethod
    async def create_link(user_id: str, req: CreateLinkRequest) -> Link:
        """Create a new link with auto-assigned sort_order."""
        # Determine next sort_order
        last_link = await Link.find(
            Link.user_id == user_id,
        ).sort(-Link.sort_order).limit(1).first_or_none()

        next_order = (last_link.sort_order + 1) if last_link else 0

        link = Link(
            user_id=user_id,
            title=req.title.strip(),
            url=req.url.strip(),
            type=req.type,
            image_url=req.image_url.strip() if req.image_url else None,
            sort_order=next_order,
            is_active=True,
        )
        await link.insert()
        return link

    @staticmethod
    async def get_link_by_id(link_id: str, user_id: str) -> Link:
        """Get a single link by ID, ensuring it belongs to the user."""
        link = await Link.get(link_id)
        if not link or link.user_id != user_id:
            raise NotFoundException("Link", link_id)
        return link

    @staticmethod
    async def update_link(link_id: str, user_id: str, req: UpdateLinkRequest) -> Link:
        """Update an existing link (partial update)."""
        link = await LinkService.get_link_by_id(link_id, user_id)

        update_data = req.model_dump(exclude_unset=True)
        if not update_data:
            return link

        # Map fields
        if "title" in update_data:
            link.title = update_data["title"].strip()
        if "url" in update_data:
            link.url = update_data["url"].strip()
        if "type" in update_data:
            link.type = update_data["type"]
        if "image_url" in update_data:
            link.image_url = update_data["image_url"].strip() if update_data["image_url"] else None
        if "sort_order" in update_data:
            link.sort_order = update_data["sort_order"]
        if "is_active" in update_data:
            link.is_active = update_data["is_active"]

        link.updated_at = datetime.now(timezone.utc)
        await link.save()
        return link

    @staticmethod
    async def delete_link(link_id: str, user_id: str) -> None:
        """Delete a link (hard delete)."""
        link = await LinkService.get_link_by_id(link_id, user_id)
        await link.delete()

    @staticmethod
    async def reorder_links(user_id: str, items: List[ReorderItem]) -> List[Link]:
        """Batch update sort_order for multiple links."""
        updated = []
        for item in items:
            link = await Link.get(item.id)
            if link and link.user_id == user_id:
                link.sort_order = item.sort_order
                link.updated_at = datetime.now(timezone.utc)
                await link.save()
                updated.append(link)
        # Return all links in new order
        return await LinkService.get_user_links(user_id)
