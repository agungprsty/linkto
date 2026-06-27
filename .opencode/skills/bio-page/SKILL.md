---
name: bio-page
description: Build public bio landing page with SSR, SEO optimization, and theme customization
---

## What I Do
- Create public bio endpoint returning user profile + active links
- Build SSR bio page with Nuxt (dynamic route `[username].vue`)
- Implement responsive mobile-first design
- Add theme customization (background color, button style, font)
- Optimize for Core Web Vitals and SEO (OG meta tags)
- Cache responses with Redis for fast loading

## API Endpoint
```
GET /api/v1/bio/{username}
```
Response: user profile + array of active links (sorted by `sort_order`)

## Frontend Implementation
```
pages/[username].vue          # SSR public bio page
components/bio/
├── BioProfile.vue            # Avatar, name, bio
├── BioLinks.vue             # Link list renderer
├── BioAffiliateCard.vue      # Affiliate product card
└── BioTheme.vue             # Dynamic theme application
```

## Caching Strategy
- Redis cache key: `bio:{username}`
- TTL: 60 seconds (cache invalidation on link update)
- Cache-aside pattern: check cache → miss → query DB → set cache

## SEO
- Dynamic OG meta tags: `og:title` (username), `og:description` (bio), `og:image` (avatar)
- SSR renders full HTML for crawlers
- `useHead` composable for per-page meta tags
- Generate sitemap for public profiles

## Theme Customization
Support these customizable properties stored in user profile:
- `theme.background_color` — hex color
- `theme.button_style` — rounded / pill / square
- `theme.button_color` — hex color
- `theme.font_family` — system / serif / modern

## Tracking Events (Passive)
- Page view: `POST /api/v1/track/view` with referrer, device info
- Link click: `POST /api/v1/track/click` with link_id, timestamp
- Fire-and-forget (non-blocking), no await on response
