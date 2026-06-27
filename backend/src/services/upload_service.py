import asyncio
import uuid
from typing import Optional

from src.core.config import settings
from src.core.exceptions import BadRequestException

# Allowed image MIME types
ALLOWED_MIME_TYPES = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/gif": ".gif",
    "image/webp": ".webp",
}

# Max file size (bytes)
MAX_SIZE = settings.upload_max_size_bytes


class UploadService:
    """Handle file uploads to S3-compatible storage."""

    @staticmethod
    def _get_s3_client():
        """Create a boto3 S3 client (called in thread pool)."""
        import boto3

        session = boto3.Session(
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region_name=settings.aws_s3_region,
        )
        kwargs = {}
        if settings.aws_s3_endpoint_url:
            kwargs["endpoint_url"] = settings.aws_s3_endpoint_url
        return session.client("s3", **kwargs)

    @staticmethod
    def _upload_file_sync(file_bytes: bytes, key: str, content_type: str) -> str:
        """Synchronous upload to S3 (runs in thread pool)."""
        s3 = UploadService._get_s3_client()
        extra_args = {
            "ContentType": content_type,
            "CacheControl": "public, max-age=31536000, immutable",
        }
        s3.put_object(
            Bucket=settings.aws_s3_bucket_name,
            Key=key,
            Body=file_bytes,
            **extra_args,
        )
        # Return public URL
        if settings.aws_s3_endpoint_url:
            return f"{settings.aws_s3_endpoint_url}/{settings.aws_s3_bucket_name}/{key}"
        return f"https://{settings.aws_s3_bucket_name}.s3.{settings.aws_s3_region}.amazonaws.com/{key}"

    @staticmethod
    async def upload_image(
        file_bytes: bytes,
        filename: str,
        content_type: str,
        user_id: str,
    ) -> str:
        """Upload an image to S3. Returns the public URL."""
        # Validate file type
        ext = ALLOWED_MIME_TYPES.get(content_type)
        if not ext:
            raise BadRequestException(
                f"Invalid image type '{content_type}'. "
                f"Allowed: {', '.join(ALLOWED_MIME_TYPES.keys())}",
            )

        # Validate file size
        if len(file_bytes) > MAX_SIZE:
            max_mb = settings.upload_max_size_mb
            raise BadRequestException(
                f"File too large. Maximum size is {max_mb}MB",
            )

        # Generate unique key
        unique_name = f"{uuid.uuid4().hex}{ext}"
        key = f"uploads/{user_id}/{unique_name}"

        # Upload in thread pool to avoid blocking
        url = await asyncio.to_thread(
            UploadService._upload_file_sync,
            file_bytes,
            key,
            content_type,
        )
        return url
