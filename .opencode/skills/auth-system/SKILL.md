---
name: auth-system
description: Implement JWT authentication (access + refresh tokens) and Google OAuth for Linkto platform
---

## What I Do
- Build registration & login endpoints (email/password)
- Implement JWT token creation and verification (python-jose)
- Set up refresh token rotation with httpOnly cookies
- Integrate Google OAuth 2.0 flow
- Create password hashing and validation (passlib bcrypt)
- Add auth middleware/dependency injection for protected routes

## Endpoints Covered
```
POST /api/v1/auth/register        # Email + password registration
POST /api/v1/auth/login           # Login, returns tokens
POST /api/v1/auth/refresh         # Refresh access token
POST /api/v1/auth/google          # Google OAuth callback
POST /api/v1/auth/logout          # Invalidate refresh token
```

## Key Files
| File | Purpose |
|---|---|
| `backend/src/core/security.py` | JWT encode/decode, password hashing |
| `backend/src/core/deps.py` | `get_current_user` dependency |
| `backend/src/models/user.py` | User Beanie document |
| `backend/src/api/v1/endpoints/auth.py` | Auth route handlers |
| `backend/src/schemas/auth.py` | Request/response Pydantic schemas |

## Token Strategy
- Access token: short-lived (30 min), stored in memory/client
- Refresh token: long-lived (7 days), httpOnly secure cookie
- Refresh token rotation: old refresh token invalidated on refresh
- Google OAuth: state param to prevent CSRF

## Important
- Rate limit login/register endpoints (5 attempts/min per IP)
- Hash passwords with bcrypt, never store plain text
- Validate email format + uniqueness
- Log all auth events (login, register, failed attempts)
