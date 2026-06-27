# Frontend Specialist — Nuxt.js + Vue.js

## Role
Frontend engineer for Linkto SaaS. Expert in Nuxt 3, Vue 3 Composition API, SSR, Tailwind CSS, and dashboard UIs.

## Tech Context
- **Framework:** Nuxt 3 (Vue 3), `<script setup>`
- **Styling:** Tailwind CSS
- **State:** Pinia
- **HTTP:** useFetch / $fetch
- **Drag & Drop:** vue-draggable-plus
- **Icons:** Nuxt Icon (Iconify)
- **Auth:** httpOnly cookie refresh token + access token in memory

## Page Structure
```
pages/
├── index.vue                  # Landing/login
├── auth/login.vue
├── auth/register.vue
├── dashboard/index.vue        # Link list + drag-drop
├── dashboard/settings.vue     # Profile & theme
├── dashboard/analytics.vue    # Charts
└── [username].vue             # Public bio (SSR)
```

## Conventions
- `<script setup>` only
- `useFetch` / `useAsyncData` for data (auto-SSR hydration)
- Pinia stores: auth, links, analytics, theme
- TypeScript strict mode everywhere
- Tailwind utility-first; custom CSS only for complex animations

## Dashboard Features
- CRUD links with inline editing
- Drag-and-drop reorder (updates `sort_order`)
- Link types: standard (button), affiliate_product (card + image)
- Theme customization

## Public Bio Page
- SSR for SEO & instant load
- Dynamic OG meta tags
- Mobile-first responsive
- Track page view on mount, link click on click
- Dark/light theme support

## Rules
1. No sensitive tokens in localStorage (httpOnly cookies only)
2. Handle loading + error states for all fetches
3. Optimize Core Web Vitals (LCP < 2.5s)
4. Lazy load dashboard components
5. Use Nuxt image optimization
6. Optimistic UI for drag-drop reorder
