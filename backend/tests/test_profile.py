"""Tests for user profile endpoints."""

import pytest
from httpx import AsyncClient


async def _register_and_login(client: AsyncClient, suffix: str = "") -> tuple:
    """Register a test user and return (access_token, username).

    The suffix ensures unique emails across tests.
    Username is auto-generated via ULID.
    """
    resp = await client.post("/api/v1/auth/register", json={
        "email": f"puser{suffix}@test.com",
        "password": "Pass1234",
    })
    if resp.status_code == 409:
        resp = await client.post("/api/v1/auth/login", json={
            "email": f"puser{suffix}@test.com",
            "password": "Pass1234",
        })
    data = resp.json()
    return data["access_token"], data["user"]["username"]


@pytest.mark.asyncio
class TestGetProfile:
    """Test GET /api/v1/user/profile."""

    async def test_get_profile(self, client: AsyncClient):
        token, username = await _register_and_login(client, "gp")
        h = {"Authorization": f"Bearer {token}"}

        response = await client.get("/api/v1/user/profile", headers=h)
        assert response.status_code == 200
        data = response.json()
        # Username is auto-generated via ULID (26 chars)
        assert len(data["username"]) == 26
        assert data["username"] == username
        assert data["email"] == "pusergp@test.com"
        assert "profile" in data
        assert "theme" in data
        assert "id" in data

    async def test_get_profile_requires_auth(self, client: AsyncClient):
        response = await client.get("/api/v1/user/profile")
        assert response.status_code == 401


@pytest.mark.asyncio
class TestUpdateProfile:
    """Test PUT /api/v1/user/profile."""

    async def test_update_full_name(self, client: AsyncClient):
        token, _ = await _register_and_login(client, "up1")
        h = {"Authorization": f"Bearer {token}"}

        response = await client.put("/api/v1/user/profile", headers=h, json={
            "full_name": "John Doe",
        })
        assert response.status_code == 200
        assert response.json()["profile"]["full_name"] == "John Doe"

    async def test_update_bio(self, client: AsyncClient):
        token, _ = await _register_and_login(client, "up2")
        h = {"Authorization": f"Bearer {token}"}

        response = await client.put("/api/v1/user/profile", headers=h, json={
            "bio": "Full-stack developer & content creator",
        })
        assert response.status_code == 200
        assert response.json()["profile"]["bio"] == "Full-stack developer & content creator"

    async def test_update_avatar_url(self, client: AsyncClient):
        token, _ = await _register_and_login(client, "up3")
        h = {"Authorization": f"Bearer {token}"}

        response = await client.put("/api/v1/user/profile", headers=h, json={
            "avatar_url": "https://storage.com/avatar.jpg",
        })
        assert response.status_code == 200
        assert response.json()["profile"]["avatar_url"] == "https://storage.com/avatar.jpg"

    async def test_update_invalid_avatar_url(self, client: AsyncClient):
        token, _ = await _register_and_login(client, "up4")
        h = {"Authorization": f"Bearer {token}"}

        response = await client.put("/api/v1/user/profile", headers=h, json={
            "avatar_url": "ftp://bad-url",
        })
        assert response.status_code == 422

    async def test_update_theme_colors(self, client: AsyncClient):
        token, _ = await _register_and_login(client, "up5")
        h = {"Authorization": f"Bearer {token}"}

        response = await client.put("/api/v1/user/profile", headers=h, json={
            "background_color": "#ff0000",
            "button_color": "#00ff00",
            "button_style": "pill",
            "font_family": "Poppins",
        })
        assert response.status_code == 200
        theme = response.json()["theme"]
        assert theme["background_color"] == "#ff0000"
        assert theme["button_color"] == "#00ff00"
        assert theme["button_style"] == "pill"
        assert theme["font_family"] == "Poppins"

    async def test_update_invalid_hex_color(self, client: AsyncClient):
        token, _ = await _register_and_login(client, "up6")
        h = {"Authorization": f"Bearer {token}"}

        response = await client.put("/api/v1/user/profile", headers=h, json={
            "background_color": "red",  # not a hex color
        })
        assert response.status_code == 422

    async def test_update_invalid_button_style(self, client: AsyncClient):
        token, _ = await _register_and_login(client, "up7")
        h = {"Authorization": f"Bearer {token}"}

        response = await client.put("/api/v1/user/profile", headers=h, json={
            "button_style": "square",  # not in allowed values
        })
        assert response.status_code == 422

    async def test_update_partial_does_not_clear_other_fields(self, client: AsyncClient):
        """Updating one field should not reset others to default."""
        token, _ = await _register_and_login(client, "up8")
        h = {"Authorization": f"Bearer {token}"}

        # First update full_name and bio
        await client.put("/api/v1/user/profile", headers=h, json={
            "full_name": "Alice",
            "bio": "Designer",
        })

        # Then update only bio
        resp2 = await client.put("/api/v1/user/profile", headers=h, json={
            "bio": "UX Designer",
        })
        data = resp2.json()
        assert data["profile"]["full_name"] == "Alice"  # unchanged
        assert data["profile"]["bio"] == "UX Designer"  # updated

    async def test_update_requires_auth(self, client: AsyncClient):
        response = await client.put("/api/v1/user/profile", json={"full_name": "X"})
        assert response.status_code == 401
