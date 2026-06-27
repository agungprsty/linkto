"""Tests for authentication endpoints."""

import pytest
from httpx import AsyncClient


class TestAuthRegister:
    """Test user registration endpoint."""

    @pytest.mark.asyncio
    async def test_register_success(self, client: AsyncClient, sample_register_payload: dict):
        """Test successful user registration."""
        response = await client.post("/api/v1/auth/register", json=sample_register_payload)
        assert response.status_code == 201
        data = response.json()
        assert "access_token" in data
        assert "refresh_token" in data
        assert data["token_type"] == "bearer"
        assert "expires_in" in data
        assert data["user"]["username"] == sample_register_payload["username"]
        assert data["user"]["email"] == sample_register_payload["email"]

    @pytest.mark.asyncio
    async def test_register_duplicate_email(self, client: AsyncClient, sample_register_payload: dict):
        """Test registration with existing email fails."""
        # First registration
        await client.post("/api/v1/auth/register", json=sample_register_payload)
        # Duplicate registration
        response = await client.post("/api/v1/auth/register", json=sample_register_payload)
        assert response.status_code == 409

    @pytest.mark.asyncio
    async def test_register_duplicate_username(self, client: AsyncClient, sample_register_payload: dict):
        """Test registration with existing username fails."""
        # First registration
        await client.post("/api/v1/auth/register", json=sample_register_payload)
        # Try with same username but different email
        payload = {
            "username": sample_register_payload["username"],
            "email": "other@example.com",
            "password": "Password1",
        }
        response = await client.post("/api/v1/auth/register", json=payload)
        assert response.status_code == 409

    @pytest.mark.asyncio
    async def test_register_invalid_username(self, client: AsyncClient):
        """Test registration with invalid username."""
        payload = {
            "username": "ab",  # too short
            "email": "test@example.com",
            "password": "Password1",
        }
        response = await client.post("/api/v1/auth/register", json=payload)
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_register_weak_password(self, client: AsyncClient):
        """Test registration with weak password (no letter)."""
        payload = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "12345678",  # no letters
        }
        response = await client.post("/api/v1/auth/register", json=payload)
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_register_short_password(self, client: AsyncClient):
        """Test registration with short password."""
        payload = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "Sh0rt",  # too short
        }
        response = await client.post("/api/v1/auth/register", json=payload)
        assert response.status_code == 422


class TestAuthLogin:
    """Test user login endpoint."""

    @pytest.mark.asyncio
    async def test_login_success(self, client: AsyncClient, sample_register_payload: dict, sample_login_payload: dict):
        """Test successful login."""
        # Register first
        await client.post("/api/v1/auth/register", json=sample_register_payload)
        # Login
        response = await client.post("/api/v1/auth/login", json=sample_login_payload)
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert "refresh_token" in data
        assert data["token_type"] == "bearer"

    @pytest.mark.asyncio
    async def test_login_invalid_password(self, client: AsyncClient, sample_register_payload: dict):
        """Test login with wrong password."""
        await client.post("/api/v1/auth/register", json=sample_register_payload)
        payload = {
            "email": sample_register_payload["email"],
            "password": "WrongPass1",
        }
        response = await client.post("/api/v1/auth/login", json=payload)
        assert response.status_code == 401

    @pytest.mark.asyncio
    async def test_login_nonexistent_email(self, client: AsyncClient):
        """Test login with email that doesn't exist."""
        payload = {
            "email": "nobody@example.com",
            "password": "Password1",
        }
        response = await client.post("/api/v1/auth/login", json=payload)
        assert response.status_code == 401


class TestTokenRefresh:
    """Test token refresh endpoint."""

    @pytest.mark.asyncio
    async def test_refresh_success(self, client: AsyncClient, sample_register_payload: dict):
        """Test successful token refresh."""
        # Register and get tokens
        reg_resp = await client.post("/api/v1/auth/register", json=sample_register_payload)
        reg_data = reg_resp.json()
        refresh_token = reg_data["refresh_token"]

        # Refresh token
        response = await client.post(
            "/api/v1/auth/refresh",
            json={"refresh_token": refresh_token},
        )
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert "refresh_token" in data
        # New tokens should be different
        assert data["access_token"] != reg_data["access_token"]
        assert data["refresh_token"] != reg_data["refresh_token"]

    @pytest.mark.asyncio
    async def test_refresh_invalid_token(self, client: AsyncClient):
        """Test refresh with invalid token."""
        response = await client.post(
            "/api/v1/auth/refresh",
            json={"refresh_token": "invalid_token_here"},
        )
        assert response.status_code == 401

    @pytest.mark.asyncio
    async def test_refresh_missing_token(self, client: AsyncClient):
        """Test refresh with missing token."""
        response = await client.post("/api/v1/auth/refresh", json={})
        assert response.status_code == 400


class TestAuthMe:
    """Test get current user endpoint."""

    @pytest.mark.asyncio
    async def test_get_me_authenticated(self, client: AsyncClient, sample_register_payload: dict):
        """Test getting current user profile with valid token."""
        # Register
        reg_resp = await client.post("/api/v1/auth/register", json=sample_register_payload)
        access_token = reg_resp.json()["access_token"]

        # Get profile
        response = await client.get(
            "/api/v1/auth/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == sample_register_payload["username"]
        assert data["email"] == sample_register_payload["email"]

    @pytest.mark.asyncio
    async def test_get_me_unauthenticated(self, client: AsyncClient):
        """Test getting profile without token."""
        response = await client.get("/api/v1/auth/me")
        assert response.status_code == 401

    @pytest.mark.asyncio
    async def test_get_me_invalid_token(self, client: AsyncClient):
        """Test getting profile with invalid token."""
        response = await client.get(
            "/api/v1/auth/me",
            headers={"Authorization": "Bearer invalid_token"},
        )
        assert response.status_code == 401


class TestHealth:
    """Test health check endpoint."""

    @pytest.mark.asyncio
    async def test_health_check(self, client: AsyncClient):
        """Test health check endpoint."""
        response = await client.get("/api/v1/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "linkto-api"
