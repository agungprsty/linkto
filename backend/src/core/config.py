from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # App
    app_env: str = Field(default="development", alias="APP_ENV")
    debug: bool = Field(default=True, alias="DEBUG")

    # MongoDB
    mongo_uri: str = Field(
        default="mongodb://linkto:pass@localhost:27017/linkto?authSource=admin",
        alias="MONGO_URI",
    )
    mongo_user: Optional[str] = Field(default=None, alias="MONGO_USER")
    mongo_pass: Optional[str] = Field(default=None, alias="MONGO_PASS")

    # Redis
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")

    # JWT
    jwt_secret_key: str = Field(
        default="dev-secret-key-change-in-production", alias="JWT_SECRET_KEY"
    )
    jwt_algorithm: str = Field(default="HS256", alias="JWT_ALGORITHM")
    jwt_access_expire_minutes: int = Field(default=30, alias="JWT_ACCESS_EXPIRE_MINUTES")
    jwt_refresh_expire_days: int = Field(default=7, alias="JWT_REFRESH_EXPIRE_DAYS")

    # Google OAuth
    google_client_id: Optional[str] = Field(default=None, alias="GOOGLE_CLIENT_ID")
    google_client_secret: Optional[str] = Field(default=None, alias="GOOGLE_CLIENT_SECRET")
    google_redirect_uri: str = Field(
        default="http://localhost:8000/api/v1/auth/google/callback",
        alias="GOOGLE_REDIRECT_URI",
    )

    # S3 / Uploads
    aws_access_key_id: Optional[str] = Field(default=None, alias="AWS_ACCESS_KEY_ID")
    aws_secret_access_key: Optional[str] = Field(default=None, alias="AWS_SECRET_ACCESS_KEY")
    aws_s3_bucket_name: str = Field(default="linkto-uploads", alias="AWS_S3_BUCKET_NAME")
    aws_s3_region: str = Field(default="ap-southeast-1", alias="AWS_S3_REGION")
    aws_s3_endpoint_url: Optional[str] = Field(default=None, alias="AWS_S3_ENDPOINT_URL")
    upload_max_size_mb: int = Field(default=10, alias="UPLOAD_MAX_SIZE_MB")

    @property
    def upload_max_size_bytes(self) -> int:
        return self.upload_max_size_mb * 1024 * 1024

    @property
    def jwt_access_expire_seconds(self) -> int:
        return self.jwt_access_expire_minutes * 60

    @property
    def jwt_refresh_expire_seconds(self) -> int:
        return self.jwt_refresh_expire_days * 24 * 60 * 60


settings = Settings()
