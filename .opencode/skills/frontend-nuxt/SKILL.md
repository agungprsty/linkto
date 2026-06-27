---
name: frontend-nuxt
description: Build Nuxt 3 frontend with SSR public pages and SPA dashboard for Linkto
---

## What I Do
- Scaffold Nuxt 3 project with proper modules and config
- Build SSR public bio pages with SEO optimization
- Build SPA dashboard with auth guards
- Create reusable Vue components and composables
- Manage state with Pinia stores
- Implement auth flow with httpOnly cookies
- Write Vitest unit tests and component tests

## Project Structure
```
frontend/
├── pages/
│   ├── index.vue
│   ├── auth/
│   │   ├── login.vue
│   │   └── register.vue
│   ├── dashboard/
│   │   ├── index.vue
│   │   ├── settings.vue
│   │   └── analytics.vue
│   └── [username].vue
├── components/
│   ├── bio/
│   ├── dashboard/
│   └── ui/
├── composables/
│   ├── useAuth.ts
│   ├── useLinks.ts
│   └── useAnalytics.ts
├── stores/
│   ├── auth.ts
│   ├── links.ts
│   └── analytics.ts
├── middleware/
│   └── auth.ts
└── nuxt.config.ts
```

## Conventions
- Composition API + `<script setup>` everywhere
- TypeScript strict mode
- `useFetch` / `useAsyncData` for SSR-safe data fetching
- Pinia stores for global state
- Tailwind CSS utility classes

## Key Nuxt Modules
- `@nuxtjs/tailwindcss` — styling
- `nuxt-icon` — icon system
- `@pinia/nuxt` — state management
- `@vueuse/nuxt` — VueUse composables

## Dashboard Features
- CRUD links with inline edit forms
- Drag-and-drop via `vue-draggable-plus`
- Type-aware forms (standard vs affiliate_product)
- Theme customization UI
- Analytics charts

## Bio Page Features
- SSR for SEO (dynamic OG meta)
- Mobile-first responsive
- Dark/light theme
- Passive tracking (page view + link click)
- Optimized Core Web Vitals
