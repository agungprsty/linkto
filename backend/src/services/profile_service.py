from datetime import datetime, timezone

from src.models.user import User
from src.schemas.profile import UpdateProfileRequest


class ProfileService:
    """Business logic for user profile operations."""

    @staticmethod
    async def get_profile(user: User) -> User:
        """Return the user object as-is (serialization handled by response model)."""
        return user

    @staticmethod
    async def update_profile(user: User, req: UpdateProfileRequest) -> User:
        """Update user profile and theme fields (partial update)."""
        update_data = req.model_dump(exclude_unset=True)
        if not update_data:
            return user

        # Profile fields
        profile_fields = {"full_name", "bio", "avatar_url"}
        theme_fields = {"background_color", "button_style", "button_color", "font_family"}

        for field, value in update_data.items():
            if field in profile_fields and value is not None:
                setattr(user.profile, field, value)
            elif field in theme_fields and value is not None:
                setattr(user.theme, field, value)

        user.updated_at = datetime.now(timezone.utc)
        await user.save()
        return user
