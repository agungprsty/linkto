from fastapi import APIRouter, Depends, UploadFile

from src.core.deps import get_current_user
from src.core.exceptions import BadRequestException
from src.models.user import User
from src.services.upload_service import UploadService

router = APIRouter(prefix="/uploads", tags=["Uploads"])


@router.post("/image")
async def upload_image(
    file: UploadFile,
    current_user: User = Depends(get_current_user),
):
    """Upload an image file to S3. Returns the public URL.

    Supported formats: JPEG, PNG, GIF, WebP.
    Max file size: configured via UPLOAD_MAX_SIZE_MB (default 10MB).
    """
    if not file.filename:
        raise BadRequestException("No file provided")

    content_type = file.content_type or "application/octet-stream"
    file_bytes = await file.read()

    url = await UploadService.upload_image(
        file_bytes=file_bytes,
        filename=file.filename,
        content_type=content_type,
        user_id=str(current_user.id),
    )

    return {"url": url}
