---
name: backend-fastapi
description: Full-stack backend development for Linkto using FastAPI, Motor/Beanie, and async Python
---

## What I Do
- Implement FastAPI application factory and configuration
- Build async route handlers with dependency injection
- Create Beanie ODM Document models
- Design Pydantic v2 schemas for validation
- Write business logic in services layer
- Implement JWT auth, rate limiting, and error handling
- Write pytest tests with httpx AsyncClient

## Project Structure
```
backend/
├── src/
│   ├── __init__.py
│   ├── main.py                    # App factory
│   ├── core/
│   │   ├── config.py              # pydantic-settings
│   │   ├── security.py            # JWT, hashing
│   │   ├── deps.py                # DI: get_current_user, get_db
│   │   └── exceptions.py          # Custom error handlers
│   ├── models/
│   │   ├── user.py                # User Document
│   │   ├── link.py                # Link Document
│   │   └── analytics.py           # Analytics Document
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── link.py
│   │   └── analytics.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── link_service.py
│   │   └── analytics_service.py
│   └── api/
│       └── v1/
│           └── endpoints/
│               ├── auth.py
│               ├── links.py
│               ├── bio.py
│               ├── track.py
│               └── analytics.py
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_links.py
│   └── test_bio.py
└── requirements.txt
```

## Key Conventions
- All route handlers are async
- Error response: `{"detail": {"code": "ERROR_CODE", "message": "Human message"}}`
- Business logic in services, not handlers
- Dependency injection for DB, current user, etc.

## Testing Standard
- `conftest.py`: async client fixture, test DB setup
- `pytest.mark.asyncio` for all async tests
- `mongomock_motor` or test containers for DB mocking
- Test success + error cases for each endpoint
