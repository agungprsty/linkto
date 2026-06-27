---
name: project-plan
description: Overall project architecture, execution strategy, and decision records for Linkto development
---

## What I Do
- Guide overall project execution following PLAN.md phases
- Enforce architecture decisions (decoupled, async, referencing)
- Track which phase is active and what needs to be built next
- Ensure consistency across backend and frontend implementations

## Execution Order (MVP)

### Phase 1: Core System & Authentication
1. Docker Compose setup (MongoDB + Redis)
2. FastAPI app factory + config
3. MongoDB connection with Motor/Beanie
4. User model + registration/login endpoints
5. JWT access + refresh token system
6. Google OAuth integration

### Phase 2: Link Management
1. Link Beanie document + indexes
2. CRUD API endpoints for links
3. Dashboard page with link list
4. Add/edit/delete link UI
5. Drag-and-drop reordering

### Phase 3: Public Bio Page
1. Bio endpoint (cached with Redis)
2. SSR `[username].vue` page
3. Theme customization
4. Responsive mobile-first design
5. SEO meta tags

### Phase 4: Tracking & Analytics
1. Time-series collection setup
2. Track view/click endpoints
3. Client-side tracking (fire-and-forget)
4. Analytics summary endpoint
5. Dashboard charts

## Architecture Rules
- Backend ↔ Frontend via REST API only (no tight coupling)
- Public pages SSR (SEO), Dashboard SPA (interactivity)
- Links: referenced (not embedded) for scalability
- Async everything in Python
- Redis cache for bio endpoint (TTL 60s)
- MongoDB time-series for analytics (needs replica set)
