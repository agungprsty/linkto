# AGENTS.md — Linkto Project

## Project Overview
Link-in-Bio SaaS platform (linkto.com). Users create a landing page to consolidate all their important links. Fast loading, mobile-first, scalable.

## Tech Stack
- **Backend:** FastAPI (Python) + MongoDB via Motor/Beanie ODM
- **Frontend:** Nuxt.js (Vue.js) — SSR for public bio pages, SPA for dashboard
- **Database:** MongoDB (NoSQL, time-series for analytics)
- **Caching:** Redis
- **Infra:** Docker, Docker Compose
- **Auth:** JWT (access + refresh tokens), OAuth Google

## Project Structure Convention

```
linkto/
├── backend/           # FastAPI application
│   ├── src/
│   │   ├── api/       # Route handlers
│   │   ├── models/    # MongoDB models (Beanie)
│   │   ├── schemas/   # Pydantic schemas
│   │   ├── services/  # Business logic
│   │   └── core/      # Config, security, dependencies
│   ├── tests/
│   └── requirements.txt
├── frontend/          # Nuxt.js application
│   ├── pages/         # Vue pages (public + dashboard)
│   ├── components/    # Reusable components
│   ├── composables/   # Vue composables
│   ├── stores/        # Pinia stores
│   └── nuxt.config.ts
├── docker-compose.yml
├── AGENTS.md
└── .opencode/
    ├── agents/        # Subagent role definitions (for Task tool)
    │   ├── backend-specialist.md
    │   ├── frontend-specialist.md
    │   └── infra-specialist.md
    └── skills/        # Domain-specific skill definitions (for Skill tool)
        ├── auth-system/
        ├── link-management/
        ├── bio-page/
        ├── analytics-track/
        ├── docker-setup/
        ├── db-mongodb/
        ├── backend-fastapi/
        ├── frontend-nuxt/
        └── project-plan/
```

## Commands

### Backend
```bash
# Install
pip install -r backend/requirements.txt

# Dev server
uvicorn backend.src.main:app --reload --host 0.0.0.0 --port 8000

# Test
pytest backend/tests/ -v

# Format
ruff check backend/ && ruff format backend/
```

### Frontend
```bash
# Install
npm install --prefix frontend

# Dev
npm run dev --prefix frontend

# Build
npm run build --prefix frontend

# Lint & typecheck
npm run lint --prefix frontend
```

### Docker
```bash
docker compose up -d
docker compose down
docker compose build backend
```

## Code Conventions
- **Python:** Type hints everywhere, async/await for I/O, Pydantic v2
- **Vue:** Composition API + `<script setup>`, Pinia state management
- **API:** RESTful, `/api/v1/` prefix, JSON, consistent error format
- **MongoDB:** Beanie ODM with typed documents
- **Naming:** snake_case (Python), camelCase (TS/JS), kebab-case (Vue files)
- **Testing:** pytest + pytest-asyncio (backend), Vitest (frontend)

## Database Collections
| Collection | Purpose |
|---|---|
| `users` | Profile, tier, auth |
| `links` | User links (standard, affiliate_product types) |
| `analytics` | Time-series: page views & link clicks |

## API Design
- **Public (no auth):** `GET /api/v1/bio/{username}`, `POST /api/v1/track/*`
- **Protected (JWT):** `/api/v1/user/*`, `/api/v1/links/*`, `/api/v1/analytics/*`

## Architecture Decisions
- Decoupled backend/frontend for independent scaling
- SSR for public pages (SEO), SPA for dashboard (interactivity)
- Referencing (not embedding) links for scalability
- Async everything in Python (Motor/Beanie for non-blocking DB)
