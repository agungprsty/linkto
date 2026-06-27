import os
import sys
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import AsyncGenerator

# Ensure backend/ is on the Python path so `from src.xxx` imports work
_backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _backend_dir not in sys.path:
    sys.path.insert(0, _backend_dir)

from beanie import init_beanie
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient

from src.core.config import settings
from src.core.exceptions import AppException
from src.models.link import Link
from src.models.user import User


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    """Application lifespan: setup DB connection and shutdown."""
    # Startup
    app.state.mongo_client = AsyncIOMotorClient(
        settings.mongo_uri,
        maxPoolSize=10,
    )
    database = app.state.mongo_client.get_default_database()

    # Initialize Beanie with document models
    await init_beanie(
        database=database,
        document_models=[
            User,
            Link,
        ],
    )

    yield

    # Shutdown
    app.state.mongo_client.close()


app = FastAPI(
    title="Linkto API",
    description="Link-in-Bio SaaS Platform API",
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Nuxt dev
        "http://localhost:8000",
        "https://linkto.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Global exception handler
@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": {"code": exc.code, "message": exc.message, "details": exc.details}},
    )


# Import and include routers
from src.api.v1.endpoints import auth, health, links  # noqa: E402

app.include_router(health.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")
app.include_router(links.router, prefix="/api/v1")


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "Linkto API",
        "version": "0.1.0",
        "docs": "/api/docs",
    }
