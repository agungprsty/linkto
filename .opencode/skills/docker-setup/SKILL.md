---
name: docker-setup
description: Configure Docker Compose multi-service environment for Linkto development and production
---

## What I Do
- Create and maintain docker-compose.yml for all services
- Write Dockerfiles for backend (Python) and frontend (Node)
- Set up MongoDB with authentication and time-series support
- Configure Redis for caching
- Manage environment variables and .env files
- Add health checks and volume mounts

## Service Architecture
| Service | Image/Base | Port | Dependencies |
|---|---|---|---|
| backend | python:3.12-slim | 8000 | mongodb, redis |
| frontend | node:20-alpine | 3000 | backend |
| mongodb | mongo:7 | 27017 | — |
| redis | redis:7-alpine | 6379 | — |

## Development Setup
- Volume mount source code for hot-reload
- Backend: `uvicorn --reload`
- Frontend: `npm run dev` with HMR
- MongoDB data persisted in named volume
- Redis data persisted in named volume

## .env Template
```
MONGO_URI=mongodb://linkto:pass@mongodb:27017/linkto?authSource=admin
MONGO_USER=linkto
MONGO_PASS=changeme
REDIS_URL=redis://redis:6379/0
JWT_SECRET_KEY=your-256-bit-secret
JWT_ALGORITHM=HS256
JWT_ACCESS_EXPIRE_MINUTES=30
JWT_REFRESH_EXPIRE_DAYS=7
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
APP_ENV=development
DEBUG=true
```

## Important
- Never commit .env to git
- Pin image versions (no `:latest`)
- Add healthcheck to every service
- Use `docker compose up -d` for background start
- Create `docker-compose.override.yml` for local dev overrides
- Add `.dockerignore` to exclude node_modules, __pycache__, .git
- Production: add reverse proxy (Traefik/Caddy) for SSL
