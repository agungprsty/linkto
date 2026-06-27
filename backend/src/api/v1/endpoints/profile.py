from fastapi import APIRouter, Depends

from src.core.deps import get_current_user
from src.models.user import User
from src.schemas.profile import UpdateProfileRequest, UserProfileResponse
from src.services.profile_service import ProfileService

router = APIRouter(prefix="/user", tags=["Profile"])


@router.get("/profile", response_model=UserProfileResponse)
async def get_profile(current_user: User = Depends(get_current_user)):
    """Get the authenticated user's full profile (including theme)."""
    return await ProfileService.get_profile(current_user)


@router.put("/profile", response_model=UserProfileResponse)
async def update_profile(
    req: UpdateProfileRequest,
    current_user: User = Depends(get_current_user),
):
    """Update user profile and theme settings.

    Supports partial update — only send the fields you want to change.
    """
    user = await ProfileService.update_profile(current_user, req)
    return user
