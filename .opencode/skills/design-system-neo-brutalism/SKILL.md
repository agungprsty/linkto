---
name: design-system-neo-brutalism
description: Neo Brutalism UI design language for Linkto — colors, shadows, typography, components, and mobile-first patterns
---

## What This Skill Covers
- Design tokens (colors, shadows, borders, fonts)
- Reusable component patterns (cards, buttons, nav, footer)
- Hover & interaction effects
- Mobile-first responsive adaptations
- Decorative elements & animations
- Tailwind CSS utility patterns used across the project

## Brand Colors
```css
--brand-yellow: #FFD800;   /* accent, highlights, CTAs */
--brand-pink:   #FF4DF8;   /* accent, tags, decorative */
--brand-blue:   #4D9FFF;   /* accent, featured sections */
--brand-green:  #00E676;   /* accent, success, decorative */
--brand-bg:     #F3F3F1;   /* page background */
```

Tailwind classes: `bg-brand-yellow`, `bg-brand-pink`, `bg-brand-blue`, `bg-brand-green`, `bg-brand-bg`

## Typography
- **Font:** Inter (Google Fonts), weights 400–900 loaded
- **Headings:** `font-black` (weight 900), large sizes (`text-4xl` to `text-7xl`)
- **Body:** `font-semibold` (600) or `font-bold` (700)
- **Meta/Byline:** `text-sm font-bold text-gray-400`
- Smaller headings: `text-3xl font-black`, `text-2xl font-black`
- Leading: `leading-[1.1]` for large headings

## Borders (Brutalism Core)
```
border-4 border-black                /* default card/button border */
border-b-4 border-black              /* section separator */
border-y-4 border-black              /* top + bottom separator */
border-t-4 border-black / md:border-l-4  /* responsive direction */
border-4 border-white                /* on dark backgrounds */
border-4 border-white/20             /* subtle on dark */
```

## Shadows (Brutalism Core)
```css
shadow-brutal:      8px 8px 0px 0px rgba(0,0,0,1)     /* large offset */
shadow-brutal-sm:   4px 4px 0px 0px rgba(0,0,0,1)     /* small offset */
shadow-brutal-hover: 2px 2px 0px 0px rgba(0,0,0,1)    /* button press */
shadow-brutal-lg:  12px 12px 0px 0px rgba(0,0,0,1)    /* featured */
```

Usage pattern: elements use `shadow-brutal-sm` by default, `hover:shadow-brutal` to grow on hover (cards lift), or `hover:shadow-brutal-hover` to shrink (buttons press).

## Tailwind Config (always include in new pages)
```js
tailwind.config = {
    theme: {
        extend: {
            fontFamily: { sans: ['Inter', 'sans-serif'] },
            colors: {
                brand: { yellow: '#FFD800', pink: '#FF4DF8', blue: '#4D9FFF', green: '#00E676', bg: '#F3F3F1' }
            },
            boxShadow: {
                'brutal': '8px 8px 0px 0px rgba(0,0,0,1)',
                'brutal-sm': '4px 4px 0px 0px rgba(0,0,0,1)',
                'brutal-hover': '2px 2px 0px 0px rgba(0,0,0,1)',
                'brutal-lg': '12px 12px 0px 0px rgba(0,0,0,1)',
            }
        }
    }
}
```

Global styles in `<style>`:
```css
body { font-family: 'Inter', sans-serif; }
html { scroll-behavior: smooth; }
.selection:bg-brand-pink selection:text-white  /* pink text selection */
```

## Component Patterns

### Navigation Bar
```html
<nav class="sticky top-0 w-full bg-brand-bg border-b-4 border-black z-50">
  <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between h-20 items-center">
      <!-- Logo: rotated circle + text -->
      <a href="index.html" class="flex items-center gap-2">
        <div class="w-10 h-10 bg-black rounded-full flex items-center justify-center -rotate-12 hover:rotate-0 transition-transform">
          <i class="ph ph-link text-brand-yellow text-2xl font-bold"></i>
        </div>
        <span class="font-black text-3xl tracking-tight">Linkto.</span>
      </a>
      <!-- CTA buttons -->
      <div class="flex items-center gap-4">
        <a href="login.html" class="hidden md:block font-bold text-lg hover:underline decoration-4 underline-offset-4 ...">Log in</a>
        <a href="register.html" class="bg-black text-white font-bold px-6 py-3 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full ...">Sign Up Free</a>
      </div>
    </div>
  </div>
</nav>
```

### Primary CTA Button
```html
<a href="#" class="bg-black text-white font-black px-8 py-4 border-4 border-black shadow-brutal-sm hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px] transition-all rounded-full inline-flex items-center gap-2">
  Label <i class="ph ph-arrow-right font-bold"></i>
</a>
```

### Secondary/Pill Button
```html
<button class="px-5 py-2 font-bold text-sm border-4 border-black bg-white text-black shadow-brutal-sm hover:bg-black hover:text-white transition-all rounded-full">
  Label
</button>
```

### Card (Default)
```html
<div class="bg-white border-4 border-black shadow-brutal-sm p-8 hover:shadow-brutal hover:-translate-y-2 transition-all">
```

### Card (Rotated)
```html
<div class="bg-white border-4 border-black shadow-brutal p-8 -rotate-1 hover:rotate-0 transition-transform">
```

### Badge / Pill Label
```html
<span class="bg-black text-white px-4 py-1 rounded-full font-bold text-sm mb-6">🔥 LABEL</span>
```

Section badges use: `inline-block bg-black text-white px-4 py-1 rounded-full font-bold text-sm mb-6`

### Tag Badge (on blog cards)
```html
<span class="text-xs font-bold bg-brand-pink text-white px-2 py-1 rounded-full">Category</span>
```

### Input Field
```html
<input type="text" placeholder="..." class="w-full border-4 border-black py-3.5 px-4 font-semibold bg-white shadow-brutal-sm focus:shadow-brutal-hover focus:translate-x-[2px] focus:translate-y-[2px] outline-none transition-all">
```

### Checkbox / Radio
```html
<input type="checkbox" class="w-5 h-5 border-4 border-black accent-black">
```

## Section Layout Patterns

### Hero Section
```html
<section class="relative overflow-hidden bg-brand-bg border-b-4 border-black">
  <!-- Desktop decorative elements (hidden on mobile) -->
  <div class="hidden md:block absolute top-10 left-10 w-48 h-48 bg-brand-yellow border-4 border-black rounded-full -z-0 float-slow"></div>
  <!-- Mobile decorative elements (subtle, small) -->
  <div class="md:hidden absolute -top-6 -right-6 w-24 h-24 bg-brand-pink border-4 border-black -z-0 rotate-12 opacity-30"></div>
  <div class="max-w-4xl mx-auto px-4 py-16 md:py-24 text-center relative z-10">
    <h1 class="text-4xl sm:text-5xl md:text-7xl font-black leading-[1.1]">...</h1>
    <p class="text-base sm:text-lg md:text-xl font-semibold text-gray-700 mt-6 md:mt-8">...</p>
  </div>
</section>
```

### Alternating Section Flow
1. `bg-brand-bg border-b-4 border-black` — default background
2. `bg-black border-y-4 border-black text-white` — dark section for contrast
3. `bg-brand-yellow border-y-4 border-black` — CTA highlight section

### Footer
```html
<footer class="bg-black py-10 text-white">
  <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row justify-between items-center gap-4">
    <p class="font-bold text-gray-500">© 2026 Linkto Inc. All rights reserved.</p>
    <div class="flex gap-6 text-sm font-bold text-gray-500">
      <a href="about.html" class="hover:text-white transition-colors">About Us</a>
      <a href="blog.html" class="...">Blog</a>
      <!-- active page: class="text-white underline decoration-4 underline-offset-2" -->
    </div>
  </div>
</footer>
```

## Hover & Interaction Effects

| Element | Default | Hover |
|---------|---------|-------|
| Card | `shadow-brutal-sm` | `hover:shadow-brutal hover:-translate-y-2` |
| Button (primary) | `shadow-brutal-sm` | `hover:shadow-brutal-hover hover:translate-x-[2px] hover:translate-y-[2px]` |
| Rotated card | `-rotate-1` | `hover:rotate-0` |
| Logo circle | `-rotate-12` | `hover:rotate-0` |
| Nav link (ghost) | normal | `hover:underline decoration-4 underline-offset-4` |
| Footer link | `text-gray-500` | `hover:text-white` |
| Filter button | `bg-white text-black` | `hover:bg-black hover:text-white` |
| Tag chip | `bg-white text-black shadow-brutal-sm` | `hover:bg-black hover:text-white` |

## Decorative Elements

### Floating Animation
```css
.float-slow { animation: floatSlow 6s ease-in-out infinite; }
@keyframes floatSlow { 0%,100% { transform: translateY(0px); } 50% { transform: translateY(-10px); } }
```
Used on: large colored circles/squares in hero sections.

### Mobile Responsiveness for Decoratives
- Desktop large decorative elements: `hidden md:block`
- Mobile small decorative elements: `md:hidden` with `opacity-30` and smaller dimensions
- Never use decorative elements that overlap text on small screens

### Rotation Utility
- `-rotate-6`, `rotate-3`, `-rotate-12`, `rotate-12`, `-rotate-1`, `rotate-1`
- Used on: decorative shapes, icon circles, section headings

## Section Spacing (Mobile-First)
- Desktop: `py-20` or `py-24`
- Mobile: `py-12` or `py-16`
- Pattern: `py-12 md:py-20` or `py-16 md:py-24`

## Grid Patterns

| Use Case | Grid Columns |
|----------|-------------|
| Features/Values | `grid-cols-1 md:grid-cols-3` |
| Team | `grid-cols-1 sm:grid-cols-2 lg:grid-cols-4` |
| Blog (with sidebar) | `grid-cols-1 md:grid-cols-2` |
| Blog (full width) | `grid-cols-1 md:grid-cols-2 lg:grid-cols-3` |
| Stats | `grid-cols-2 md:grid-cols-4` |
| Story/Content | `grid-cols-1 md:grid-cols-2` |
| Templates | `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3` |

## Icon Usage
- Library: Phosphor Icons via `@phosphor-icons/web` CDN
- Loaded with: `<script src="https://unpkg.com/@phosphor-icons/web"></script>`
- Usage: `<i class="ph ph-link"></i>`, `<i class="ph ph-arrow-right font-bold"></i>`
- Common icons: `ph-link`, `ph-arrow-right`, `ph-magnifying-glass`, `ph-funnel`, `ph-calendar`, `ph-folder`, `ph-tag`, `ph-x-circle`, `ph-trend-up`, `ph-rocket`, `ph-users-three`, `ph-megaphone`, `ph-shopping-bag`, `ph-paint-roller`, `ph-chart-line-up`, `ph-lightning`, `ph-hand-heart`, `ph-globe`, `ph-discord-logo`, `ph-trophy`, `ph-video-camera`, `ph-chalkboard-simple`

## Page-Specific Patterns

### Blog — Faceted Search Sidebar
- Sidebar on left (md: `w-72`) with: search input, category checkboxes, tag chips, date radio buttons, clear filters button
- Mobile: sidebar hidden by default, toggled by "Filters" button
- Grid: `grid-cols-1 md:grid-cols-2` (sidebar takes space)
- Featured post: full width above, `md:grid-cols-2` layout

### Dashboard
- Sidebar: `w-72` with nav items, each with icon + label
- Connection status: `bg-brand-green/20 border-4 border-green-600` indicator
- Link cards: standard type (button style) vs affiliate_product (with image/price)

### Auth Pages (Login / Register)
- Centered card layout: max-w-md with `bg-white border-4 border-black shadow-brutal`
- Form fields with brutalist inputs
- Password strength: 3-bar indicator (weak/medium/strong)
- Social buttons: Google (`bg-white`), Apple (`bg-black text-white`)
- "OR" divider: `before:block before:h-[2px] before:bg-black` pattern

## Important Rules
1. All decorative elements MUST be hidden or reduced on mobile to avoid text overlap
2. Use `hidden md:block` for desktop-only decorations, `md:hidden opacity-30` for mobile-only ones
3. Section padding MUST be mobile-first: smaller on mobile (`py-12`), larger on desktop (`py-20`)
4. Stack grids on mobile: `grid-cols-1` for mobile, larger breakpoints for desktop columns
5. Always include `px-4 sm:px-6 lg:px-8` for responsive horizontal padding
6. Use `max-w-5xl` or `max-w-6xl` for content width, `max-w-screen-2xl` for nav/footer
7. Section separator: `border-b-4 border-black` between sections
8. No emojis unless the user explicitly requests them
