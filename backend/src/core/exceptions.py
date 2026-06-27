from fastapi import HTTPException, status
from typing import Any


class AppException(HTTPException):
    """Base application exception with structured error response."""

    def __init__(
        self,
        status_code: int,
        code: str,
        message: str,
        details: Any = None,
    ):
        self.code = code
        self.message = message
        self.details = details
        super().__init__(
            status_code=status_code,
            detail={"code": code, "message": message, "details": details},
        )


class NotFoundException(AppException):
    def __init__(self, entity: str = "Resource", identifier: str = ""):
        msg = f"{entity} not found"
        if identifier:
            msg += f": {identifier}"
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            code="NOT_FOUND",
            message=msg,
        )


class DuplicateException(AppException):
    def __init__(self, entity: str = "Resource", field: str = ""):
        msg = f"{entity} already exists"
        if field:
            msg += f" with this {field}"
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            code="DUPLICATE",
            message=msg,
        )


class UnauthorizedException(AppException):
    def __init__(self, message: str = "Not authenticated"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            code="UNAUTHORIZED",
            message=message,
        )


class ForbiddenException(AppException):
    def __init__(self, message: str = "Not enough permissions"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            code="FORBIDDEN",
            message=message,
        )


class BadRequestException(AppException):
    def __init__(self, message: str = "Bad request", details: Any = None):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            code="BAD_REQUEST",
            message=message,
            details=details,
        )


class ValidationException(AppException):
    def __init__(self, message: str = "Validation error", details: Any = None):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            code="VALIDATION_ERROR",
            message=message,
            details=details,
        )
