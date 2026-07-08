"""Test fixtures for Linkto backend tests.

Uses a real MongoDB instance (via Docker) for integration testing.
"""

import asyncio
import os
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

# Set environment variables for testing
os.environ["MONGO_URI"] = "mongodb://linkto:pass@localhost:27017/linkto_test?authSource=admin"
os.environ["MONGO_USER"] = "linkto"
os.environ["MONGO_PASS"] = "pass"
os.environ["JWT_SECRET_KEY"] = "test-secret-key-for-testing-only"
os.environ["JWT_ALGORITHM"] = "HS256"
os.environ["JWT_ACCESS_EXPIRE_MINUTES"] = "30"
os.environ["JWT_REFRESH_EXPIRE_DAYS"] = "7"
os.environ["APP_ENV"] = "test"
os.environ["DEBUG"] = "true"

# Use the same event loop for fixtures and tests
pytest_asyncio_default_fixture_loop_scope = "function"


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    """Create an httpx AsyncClient for testing.

    Uses the FastAPI app with lifespan events triggered.
    Connects to the Docker MongoDB instance.
    """
    from src.main import app

    async with LifespanManager(app):
        transport = ASGITransport(app=app)
        async with AsyncClient(
            transport=transport,
            base_url="http://test",
        ) as ac:
            yield ac


@pytest_asyncio.fixture(autouse=True)
async def clean_db():
    """Clean the database collections between tests.

    Uses Motor directly (not Beanie) to avoid dependency on app lifespan.
    """
    from motor.motor_asyncio import AsyncIOMotorClient

    mongo_uri = os.environ["MONGO_URI"]

    # Pre-test cleanup
    client = AsyncIOMotorClient(mongo_uri)
    db = client.get_default_database()
    for coll_name in await db.list_collection_names():
        if not coll_name.startswith("system."):
            await db[coll_name].delete_many({})
    client.close()

    yield

    # Post-test cleanup
    client = AsyncIOMotorClient(mongo_uri)
    db = client.get_default_database()
    for coll_name in await db.list_collection_names():
        if not coll_name.startswith("system."):
            await db[coll_name].delete_many({})
    client.close()


@pytest.fixture
def sample_register_payload() -> dict:
    """Sample payload for user registration.

    Only email and password are required — username is auto-generated via ULID.
    """
    return {
        "email": "test@example.com",
        "password": "Password1",
    }


@pytest.fixture
def sample_login_payload() -> dict:
    """Sample payload for user login."""
    return {
        "email": "test@example.com",
        "password": "Password1",
    }
