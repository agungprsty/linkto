# Linkto — Link-in-Bio SaaS Platform

[![Tech Stack](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![Tech Stack](https://img.shields.io/badge/Frontend-Nuxt.js-00DC82?logo=nuxt.js)](https://nuxt.com)
[![Tech Stack](https://img.shields.io/badge/Database-MongoDB-47A248?logo=mongodb)](https://www.mongodb.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Linkto** is a Link-in-Bio SaaS platform that allows creators, SMEs, and affiliates to create a single landing page consolidating all their important links. Fast loading, mobile-first, and built to scale.

## Features

- **User Authentication** — Email/password registration & login, Google OAuth, JWT access + refresh tokens
- **Link Management** — Full CRUD with drag-and-drop reordering, supports standard buttons and affiliate product cards
- **Public Bio Page** — SSR-optimized landing page at `linkto.com/username` with SEO meta tags and responsive design
- **Theme Customization** — Customizable background colors, button styles, and fonts
- **Analytics** — Time-series tracking for page views and link clicks with dashboard charts
- **Caching** — Redis-powered caching for fast bio page delivery

## Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | FastAPI (Python), Motor/Beanie ODM, Pydantic v2 |
| **Frontend** | Nuxt.js 3 (Vue 3), Tailwind CSS, Pinia |
| **Database** | MongoDB 7 (time-series for analytics) |
| **Cache** | Redis 7 |
| **Auth** | JWT (python-jose), Google OAuth, bcrypt |
| **Infra** | Docker, Docker Compose |

## Project Structure

```
linkto/
├── backend/               # FastAPI application
│   ├── src/
│   │   ├── api/           # Route handlers (v1 endpoints)
│   │   ├── models/        # Beanie ODM documents
│   │   ├── schemas/       # Pydantic request/response models
│   │   ├── services/      # Business logic layer
│   │   └── core/          # Config, security, dependencies
│   ├── tests/
│   └── requirements.txt
├── frontend/              # Nuxt.js application
│   ├── pages/             # Public bio & dashboard pages
│   ├── components/        # Reusable Vue components
│   ├── composables/       # Shared composable logic
│   ├── stores/            # Pinia state stores
│   └── nuxt.config.ts
├── docker-compose.yml
├── AGENTS.md              # AI agent project context
└── .opencode/
    ├── agents/            # Subagent role definitions
    └── skills/            # Domain-specific skill definitions
```

## Quick Start

### Prerequisites

- Python 3.12+
- Node.js 20+
- Docker & Docker Compose

### Development

```bash
# Clone the repository
git clone https://github.com/agungprsty/linkto.git
cd linkto

# Start infrastructure (MongoDB + Redis)
docker compose up -d mongodb redis

# Backend setup
pip install -r backend/requirements.txt
uvicorn backend.src.main:app --reload --host 0.0.0.0 --port 8000

# Frontend setup (separate terminal)
npm install --prefix frontend
npm run dev --prefix frontend
```

### Using Docker (all services)

```bash
docker compose up -d
```

## API Overview

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/api/v1/bio/{username}` | No | Public bio page data |
| POST | `/api/v1/track/view` | No | Track page view |
| POST | `/api/v1/track/click` | No | Track link click |
| GET | `/api/v1/user/profile` | JWT | Get user profile |
| PUT | `/api/v1/user/profile` | JWT | Update profile/theme |
| GET | `/api/v1/links` | JWT | List user links |
| POST | `/api/v1/links` | JWT | Create new link |
| PUT | `/api/v1/links/{id}` | JWT | Update link |
| DELETE | `/api/v1/links/{id}` | JWT | Delete link |
| GET | `/api/v1/analytics/summary` | JWT | Analytics dashboard data |

## Environment Variables

Create a `.env` file in the project root:

```env
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

## Roadmap

| Phase | Features |
|---|---|
| **1** | Auth system, MongoDB connection, JWT, Google OAuth |
| **2** | Link CRUD, drag-and-drop dashboard, multi-type links |
| **3** | Public bio page (SSR), theme customization, SEO |
| **4** | Analytics tracking, time-series data, dashboard charts |

## License

MIT
