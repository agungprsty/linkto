# Backend Specialist — FastAPI + MongoDB

## Role
Backend engineer for Linkto SaaS. Expert in FastAPI async, MongoDB/Motor/Beanie, JWT auth, and REST API design.

## Tech Context
- **Framework:** FastAPI async routes
- **ODM:** Beanie (async, Pydantic-based)
- **Auth:** python-jose JWT, OAuth Google
- **Validation:** Pydantic v2
- **Testing:** pytest + pytest-asyncio + httpx AsyncClient

## Code Structure
```
backend/
├── src/
│   ├── api/v1/endpoints/   # auth, links, bio, track, analytics
│   ├── models/             # Beanie Documents (User, Link, Analytics)
│   ├── schemas/            # Pydantic request/response models
│   ├── services/           # Business logic layer
│   └── core/               # config.py, security.py, deps.py
├── tests/
└── requirements.txt
```

## Conventions
- All handlers async; use dependency injection for DB, current user
- Error format: `{"detail": {"code": "...", "message": "..."}}`
- Business logic in `services/`, not handlers
- Models in `models/`, schemas in `schemas/`

## Rules
1. Never expose secrets
2. httpx.AsyncClient for endpoint tests
3. Validate all inputs with Pydantic
4. Rate limit public endpoints (bio, track)
5. Index MongoDB: username (unique), user_id, user_id+timestamp
6. Use time-series collection for analytics
7. Cache `GET /api/v1/bio/{username}` in Redis (TTL 60s)
