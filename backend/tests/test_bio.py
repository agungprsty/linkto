"""Tests for public bio page endpoint."""

import pytest
from httpx import AsyncClient


class TestBioEndpoint:
    """Test public bio page endpoint (GET /api/v1/bio/{username})."""

    @pytest.mark.asyncio
    async def test_get_bio_success(self, client: AsyncClient, sample_register_payload: dict):
        """Test getting public bio for an existing user."""
        # Register a user first
        reg_resp = await client.post("/api/v1/auth/register", json=sample_register_payload)
        assert reg_resp.status_code == 201
        username = reg_resp.json()["user"]["username"]

        # Get public bio
        response = await client.get(f"/api/v1/bio/{username}")
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == username
        assert "profile" in data
        assert "theme" in data
        assert "links" in data
        assert isinstance(data["links"], list)

    @pytest.mark.asyncio
    async def test_get_bio_not_found(self, client: AsyncClient):
        """Test getting bio for a non-existent username."""
        response = await client.get("/api/v1/bio/nonexistent_user_12345")
        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_get_bio_with_links(self, client: AsyncClient, sample_register_payload: dict):
        """Test getting public bio with active links."""
        # Register user
        reg_resp = await client.post("/api/v1/auth/register", json=sample_register_payload)
        assert reg_resp.status_code == 201
        reg_data = reg_resp.json()
        username = reg_data["user"]["username"]
        access_token = reg_data["access_token"]

        # Create some links
        links_payloads = [
            {"title": "GitHub", "url": "https://github.com/test", "type": "standard"},
            {"title": "Twitter", "url": "https://twitter.com/test", "type": "standard"},
        ]
        for link_payload in links_payloads:
            resp = await client.post(
                "/api/v1/links",
                json=link_payload,
                headers={"Authorization": f"Bearer {access_token}"},
            )
            assert resp.status_code == 201

        # Get public bio — should include links
        response = await client.get(f"/api/v1/bio/{username}")
        assert response.status_code == 200
        data = response.json()
        assert len(data["links"]) == 2
        # Links should be sorted by sort_order
        assert data["links"][0]["sort_order"] <= data["links"][1]["sort_order"]

    @pytest.mark.asyncio
    async def test_get_bio_inactive_user(self, client: AsyncClient, sample_register_payload: dict):
        """Test getting bio for an inactive user returns 404."""
        # Register user
        reg_resp = await client.post("/api/v1/auth/register", json=sample_register_payload)
        assert reg_resp.status_code == 201
        reg_data = reg_resp.json()
        username = reg_data["user"]["username"]
        access_token = reg_data["access_token"]

        # Bio should work before deactivation
        response = await client.get(f"/api/v1/bio/{username}")
        assert response.status_code == 200

        # Deactivate the user (direct DB manipulation via Beanie)
        from src.models.user import User
        user = await User.find_one(User.username == username)
        assert user is not None
        user.is_active = False
        await user.save()

        # Bio should now return 404
        response = await client.get(f"/api/v1/bio/{username}")
        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_get_bio_no_auth_required(self, client: AsyncClient, sample_register_payload: dict):
        """Test that the bio endpoint works without any authentication."""
        # Register user
        reg_resp = await client.post("/api/v1/auth/register", json=sample_register_payload)
        assert reg_resp.status_code == 201
        username = reg_resp.json()["user"]["username"]

        # No auth header — should still work
        response = await client.get(f"/api/v1/bio/{username}")
        assert response.status_code == 200
