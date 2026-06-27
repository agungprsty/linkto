---
name: db-mongodb
description: Design MongoDB schemas, Beanie ODM models, and indexes for the Linkto platform
---

## What I Do
- Define Beanie Document models for users, links, analytics
- Create Pydantic schemas for request/response validation
- Set up MongoDB connection with Motor async driver
- Design indexes for query performance
- Configure time-series collection for analytics
- Write database initialization and migration scripts

## Collections

### users
```
Fields: username (unique), email (unique), password_hash,
        profile { full_name, bio, avatar_url },
        tier (free|pro|business),
        theme { background_color, button_style, button_color, font_family },
        created_at, updated_at
Indexes: username (unique), email (unique)
```

### links
```
Fields: user_id (ref), title, url, type (standard|affiliate_product),
        image_url (nullable), sort_order (int), is_active (bool),
        created_at
Indexes: user_id + sort_order (compound), type
```

### analytics (time-series)
```
Fields: user_id, link_id (nullable), event_type (page_view|link_click),
        metadata { referrer, device, geo_location },
        timestamp (timeField)
Indexes: user_id + timestamp (compound)
```
Requires MongoDB replica set for time-series.

## Beanie Document Examples
```python
class User(Document):
    username: str
    email: str
    password_hash: str
    profile: ProfileModel | None = None
    tier: Literal["free", "pro", "business"] = "free"
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"
        indexes = [
            "username",  # unique
            "email",     # unique
        ]
```

## Important
- Use `field(default_factory=...)` for defaults, not mutable objects
- Index all fields used in queries (user_id, username, timestamp)
- Time-series collection must be created before app starts
- Use `before_event` handlers for `updated_at` auto-update
- Connection string with authSource=admin when using auth
- Pool size: maxPoolSize=10 per service
