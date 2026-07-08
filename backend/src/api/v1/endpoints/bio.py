"""Public bio page endpoint — no authentication required."""

from fastapi import APIRouter

from src.schemas.bio import BioResponse
from src.services.bio_service import BioService

router = APIRouter(prefix="/bio", tags=["Bio"])


@router.get("/{username}", response_model=BioResponse)
async def get_bio(username: str):
    """Get public bio page data for a username.

    This endpoint is publicly accessible — no authentication required.
    Returns the user's profile, theme settings, and active links.
    """
    bio = await BioService.get_bio_by_username(username)
    return bio
