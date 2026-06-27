---
name: link-management
description: Build CRUD endpoints and dashboard UI for user link management with drag-and-drop sorting
---

## What I Do
- Create full CRUD REST API for user links
- Build dashboard UI with link list, add/edit/delete modals
- Implement drag-and-drop reordering (updates `sort_order`)
- Support multiple link types: `standard` (button) and `affiliate_product` (card with image)
- Add inline editing for link title, URL, and image
- Validate URLs and handle duplicate sorting

## API Endpoints
```
GET    /api/v1/links           # List all user links (sorted)
POST   /api/v1/links           # Create new link
PUT    /api/v1/links/{id}      # Update link or sort_order
DELETE /api/v1/links/{id}      # Delete link
```

## Link Types
### standard
Simple button with title + URL. No image.

### affiliate_product
Card layout with product image (`image_url`), title, and affiliate URL.

## Frontend Components
| Component | Purpose |
|---|---|
| `DashboardLinkList.vue` | Sortable link list with drag-drop |
| `DashboardLinkCard.vue` | Individual link item display |
| `LinkFormModal.vue` | Add/edit link form (type-aware) |
| `LinkTypeSelector.vue` | Toggle between standard/affiliate |

## Drag-and-Drop
- Use `vue-draggable-plus` for sortable lists
- On reorder: batch update `sort_order` values
- Optimistic UI: update immediately, revert on API failure
- Debounce API calls during rapid dragging

## Important
- Validate URL format server-side (Pydantic AnyUrl)
- `image_url` only required for `affiliate_product` type
- Sort order is 1-based integer, auto-assigned on create
- Soft delete not needed; hard delete links
- Index `user_id + sort_order` for fast sorted queries
