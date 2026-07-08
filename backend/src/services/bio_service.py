"""Business logic for public bio page operations."""

from typing import List

from src.core.exceptions import NotFoundException
from src.models.link import Link
from src.models.user import User
from src.schemas.bio import BioLinkResponse, BioResponse


class BioService:
    """Business logic for the public bio page."""

    @staticmethod
    async def get_bio_by_username(username: str) -> BioResponse:
        """Get public bio data for a given username.

        Returns the user's public profile, theme settings, and active links.
        This endpoint is publicly accessible (no authentication required).
        """
        # Find user by username
        user = await User.find_one(User.username == username)
        if not user:
            raise NotFoundException("User", username)

        if not user.is_active:
            raise NotFoundException("User", username)

        # Fetch active links for this user, sorted by sort_order
        links = await Link.find(
            Link.user_id == str(user.id),
            Link.is_active == True,  # noqa: E712
        ).sort(Link.sort_order).to_list()

        # Build response
        bio_links = [BioLinkResponse(
            id=str(link.id),
            title=link.title,
            url=link.url,
            type=link.type,
            image_url=link.image_url,
            sort_order=link.sort_order,
        ) for link in links]

        return BioResponse(
            username=user.username,
            profile=user.profile,
            theme=user.theme,
            links=bio_links,
        )
