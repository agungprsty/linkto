"""Tests for link management endpoints."""

import pytest
from httpx import AsyncClient


async def _register_and_login(client: AsyncClient, suffix: str = "") -> dict:
    """Helper: register a user and return auth tokens."""
    resp = await client.post("/api/v1/auth/register", json={
        "username": f"linkuser{suffix}",
        "email": f"linkuser{suffix}@test.com",
        "password": "Pass1234",
    })
    if resp.status_code == 409:
        # Already exists, login instead
        resp = await client.post("/api/v1/auth/login", json={
            "email": f"linkuser{suffix}@test.com",
            "password": "Pass1234",
        })
    data = resp.json()
    return {
        "access_token": data["access_token"],
        "user_id": data["user"]["id"],
    }


@pytest.mark.asyncio
class TestListLinks:
    """Test GET /api/v1/links."""

    async def test_list_empty(self, client: AsyncClient):
        """No links returns empty list."""
        auth = await _register_and_login(client, "list1")
        response = await client.get(
            "/api/v1/links",
            headers={"Authorization": f"Bearer {auth['access_token']}"},
        )
        assert response.status_code == 200
        assert response.json() == []

    async def test_list_links_sorted(self, client: AsyncClient):
        """Links are returned sorted by sort_order."""
        auth = await _register_and_login(client, "list2")
        h = {"Authorization": f"Bearer {auth['access_token']}"}

        # Create 3 links
        link1 = await client.post("/api/v1/links", headers=h, json={
            "title": "Z Link", "url": "https://z.com", "type": "standard",
        })
        link2 = await client.post("/api/v1/links", headers=h, json={
            "title": "A Link", "url": "https://a.com", "type": "standard",
        })

        response = await client.get("/api/v1/links", headers=h)
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
        # sort_order should be 0, 1
        assert data[0]["sort_order"] == 0
        assert data[1]["sort_order"] == 1

    async def test_list_requires_auth(self, client: AsyncClient):
        """No token returns 401."""
        response = await client.get("/api/v1/links")
        assert response.status_code == 401


@pytest.mark.asyncio
class TestCreateLink:
    """Test POST /api/v1/links."""

    async def test_create_standard(self, client: AsyncClient):
        auth = await _register_and_login(client, "create1")
        h = {"Authorization": f"Bearer {auth['access_token']}"}

        response = await client.post("/api/v1/links", headers=h, json={
            "title": "My GitHub",
            "url": "https://github.com/user",
            "type": "standard",
        })
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "My GitHub"
        assert data["url"] == "https://github.com/user"
        assert data["type"] == "standard"
        assert data["image_url"] is None
        assert data["sort_order"] == 0
        assert data["is_active"] is True
        assert "id" in data
        assert "created_at" in data

    async def test_create_affiliate(self, client: AsyncClient):
        auth = await _register_and_login(client, "create2")
        h = {"Authorization": f"Bearer {auth['access_token']}"}

        response = await client.post("/api/v1/links", headers=h, json={
            "title": "Cool Product",
            "url": "https://shop.com/product",
            "type": "affiliate_product",
            "image_url": "https://shop.com/product.jpg",
        })
        assert response.status_code == 201
        data = response.json()
        assert data["type"] == "affiliate_product"
        assert data["image_url"] == "https://shop.com/product.jpg"

    async def test_create_affiliate_optional_image(self, client: AsyncClient):
        """Affiliate product without image_url should succeed (image_url is optional)."""
        auth = await _register_and_login(client, "create3")
        h = {"Authorization": f"Bearer {auth['access_token']}"}

        response = await client.post("/api/v1/links", headers=h, json={
            "title": "No Image Product",
            "url": "https://shop.com/product",
            "type": "affiliate_product",
        })
        assert response.status_code == 201
        assert response.json()["image_url"] is None

    async def test_create_invalid_url(self, client: AsyncClient):
        auth = await _register_and_login(client, "create4")
        h = {"Authorization": f"Bearer {auth['access_token']}"}

        response = await client.post("/api/v1/links", headers=h, json={
            "title": "Bad URL",
            "url": "ftp://bad.com",
            "type": "standard",
        })
        assert response.status_code == 422

    async def test_create_auto_increment_sort(self, client: AsyncClient):
        """sort_order auto-increments with each new link."""
        auth = await _register_and_login(client, "create5")
        h = {"Authorization": f"Bearer {auth['access_token']}"}

        r1 = await client.post("/api/v1/links", headers=h, json={
            "title": "L1", "url": "https://a.com", "type": "standard",
        })
        r2 = await client.post("/api/v1/links", headers=h, json={
            "title": "L2", "url": "https://b.com", "type": "standard",
        })
        assert r1.json()["sort_order"] == 0
        assert r2.json()["sort_order"] == 1

    async def test_create_requires_auth(self, client: AsyncClient):
        response = await client.post("/api/v1/links", json={
            "title": "X", "url": "https://x.com", "type": "standard",
        })
        assert response.status_code == 401


@pytest.mark.asyncio
class TestUpdateLink:
    """Test PUT /api/v1/links/{id}."""

    async def test_update_title(self, client: AsyncClient):
        auth = await _register_and_login(client, "upd1")
        h = {"Authorization": f"Bearer {auth['access_token']}"}

        created = await client.post("/api/v1/links", headers=h, json={
            "title": "Old", "url": "https://old.com", "type": "standard",
        })
        link_id = created.json()["id"]

        response = await client.put(f"/api/v1/links/{link_id}", headers=h, json={
            "title": "New Title",
        })
        assert response.status_code == 200
        assert response.json()["title"] == "New Title"
        assert response.json()["url"] == "https://old.com"  # unchanged

    async def test_update_sort_order(self, client: AsyncClient):
        auth = await _register_and_login(client, "upd2")
        h = {"Authorization": f"Bearer {auth['access_token']}"}

        c1 = await client.post("/api/v1/links", headers=h, json={
            "title": "A", "url": "https://a.com", "type": "standard",
        })
        c2 = await client.post("/api/v1/links", headers=h, json={
            "title": "B", "url": "https://b.com", "type": "standard",
        })
        id1 = c1.json()["id"]

        # Move first link to sort_order 5
        response = await client.put(f"/api/v1/links/{id1}", headers=h, json={
            "sort_order": 5,
        })
        assert response.status_code == 200
        assert response.json()["sort_order"] == 5

    async def test_update_deactivate(self, client: AsyncClient):
        auth = await _register_and_login(client, "upd3")
        h = {"Authorization": f"Bearer {auth['access_token']}"}

        created = await client.post("/api/v1/links", headers=h, json={
            "title": "Active", "url": "https://active.com", "type": "standard",
        })
        link_id = created.json()["id"]

        response = await client.put(f"/api/v1/links/{link_id}", headers=h, json={
            "is_active": False,
        })
        assert response.status_code == 200
        assert response.json()["is_active"] is False

    async def test_update_other_user_link_returns_404(self, client: AsyncClient):
        """User cannot update another user's link."""
        auth1 = await _register_and_login(client, "upd4a")
        auth2 = await _register_and_login(client, "upd4b")
        h1 = {"Authorization": f"Bearer {auth1['access_token']}"}
        h2 = {"Authorization": f"Bearer {auth2['access_token']}"}

        created = await client.post("/api/v1/links", headers=h1, json={
            "title": "Secret", "url": "https://secret.com", "type": "standard",
        })
        link_id = created.json()["id"]

        # User2 tries to update user1's link
        response = await client.put(f"/api/v1/links/{link_id}", headers=h2, json={
            "title": "Hacked",
        })
        assert response.status_code == 404


@pytest.mark.asyncio
class TestDeleteLink:
    """Test DELETE /api/v1/links/{id}."""

    async def test_delete_link(self, client: AsyncClient):
        auth = await _register_and_login(client, "del1")
        h = {"Authorization": f"Bearer {auth['access_token']}"}

        created = await client.post("/api/v1/links", headers=h, json={
            "title": "Delete Me", "url": "https://del.com", "type": "standard",
        })
        link_id = created.json()["id"]

        response = await client.delete(f"/api/v1/links/{link_id}", headers=h)
        assert response.status_code == 204

        # Verify it's gone
        list_resp = await client.get("/api/v1/links", headers=h)
        assert len(list_resp.json()) == 0

    async def test_delete_nonexistent(self, client: AsyncClient):
        auth = await _register_and_login(client, "del2")
        h = {"Authorization": f"Bearer {auth['access_token']}"}

        response = await client.delete(
            "/api/v1/links/000000000000000000000000", headers=h,
        )
        assert response.status_code == 404


@pytest.mark.asyncio
class TestReorderLinks:
    """Test PUT /api/v1/links/reorder."""

    async def test_reorder(self, client: AsyncClient):
        auth = await _register_and_login(client, "ro1")
        h = {"Authorization": f"Bearer {auth['access_token']}"}

        c1 = await client.post("/api/v1/links", headers=h, json={
            "title": "First", "url": "https://a.com", "type": "standard",
        })
        c2 = await client.post("/api/v1/links", headers=h, json={
            "title": "Second", "url": "https://b.com", "type": "standard",
        })
        id1 = c1.json()["id"]
        id2 = c2.json()["id"]

        # Swap sort orders
        response = await client.put("/api/v1/links/reorder", headers=h, json={
            "items": [
                {"id": id1, "sort_order": 1},
                {"id": id2, "sort_order": 0},
            ],
        })
        assert response.status_code == 200
        data = response.json()
        # Should be sorted: [id2 (order 0), id1 (order 1)]
        assert len(data) == 2
        assert data[0]["id"] == id2
        assert data[1]["id"] == id1
