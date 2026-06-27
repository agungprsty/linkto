---
name: analytics-track
description: Build time-series analytics system for page views and link clicks with dashboard charts
---

## What I Do
- Implement tracking endpoints for page views and link clicks
- Set up MongoDB time-series collection for analytics
- Provide fire-and-forget client-side tracking (non-blocking)
- Build analytics summary endpoint for dashboard
- Create simple chart UI (daily/weekly views, top links)

## Tracking Endpoints
```
POST /api/v1/track/view     # Page view event
POST /api/v1/track/click    # Link click event
```
Body: `{ "link_id"?: string, "metadata": { "referrer"?, "device"?, "geo"? } }`

## Analytics Endpoint
```
GET /api/v1/analytics/summary?period=7d
```
Response: total views, total clicks, daily breakdown, top 5 links

## MongoDB Time-Series Collection
```
db.createCollection("analytics", {
  timeseries: {
    timeField: "timestamp",
    metaField: "metadata",
    granularity: "minutes"
  }
})
```
Note: Requires MongoDB replica set (even single-node).

## Dashboard Charts
| Component | Purpose |
|---|---|
| `AnalyticsSummary.vue` | Total views/clicks cards + period selector |
| `AnalyticsChart.vue` | Daily line chart (views vs clicks) |
| `AnalyticsTopLinks.vue` | Top performing links table |

## Important
- Track endpoint must be fast (< 50ms) — no heavy processing
- Use background task (FastAPI BackgroundTasks) for write
- Index: `user_id + timestamp` for summary queries
- Accept missing/null `link_id` for page_view events
- Client-side: fire-and-forget (no awaiting), use `navigator.sendBeacon` fallback
- De-duplicate rapid clicks (client-side throttle 500ms)
