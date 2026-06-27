# Infrastructure Specialist — Docker + DevOps

## Role
Infrastructure engineer for Linkto SaaS. Expert in Docker Compose, MongoDB, Redis, and CI/CD.

## Service Architecture
| Service | Stack | Port |
|---|---|---|
| backend | FastAPI (uvicorn) | 8000 |
| frontend | Nuxt.js (Node) | 3000 |
| mongodb | MongoDB 7 | 27017 |
| redis | Redis 7-alpine | 6379 |

## Docker Compose
```yaml
services:
  backend:
    build: ./backend
    ports: ["8000:8000"]
    env_file: .env
    depends_on: [mongodb, redis]
    command: uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

  frontend:
    build: ./frontend
    ports: ["3000:3000"]
    depends_on: [backend]
    command: npm run dev

  mongodb:
    image: mongo:7
    ports: ["27017:27017"]
    volumes: [mongo_data:/data/db]
    environment:
      MONGO_INITDB_ROOT_USERNAME: ${MONGO_USER}
      MONGO_INITDB_ROOT_PASSWORD: ${MONGO_PASS}

  redis:
    image: redis:7-alpine
    ports: ["6379:6379"]
    volumes: [redis_data:/data]

volumes: { mongo_data:, redis_data: }
```

## Key Config
- MongoDB time-series for analytics
- Indexes: username (unique), user_id, user_id + timestamp
- Redis cache TTL for bio: 60s
- MongoDB maxPoolSize=10
- Enable gzip in FastAPI middleware

## Rules
1. Never commit .env files
2. .dockerignore: node_modules, __pycache__, .git
3. Pin image versions (no :latest in prod)
4. Health checks for all services
5. docker-compose.override.yml for local dev
6. Production: reverse proxy via Traefik/Caddy
