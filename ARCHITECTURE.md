# System Architecture

## Overview

This document describes the architecture of the Airbnb Clone full-stack application.

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                          CLIENT LAYER                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              React Frontend (Port 3000)                   │  │
│  │                                                            │  │
│  │  ├─ Pages (Home, Login, Properties, Bookings, etc.)      │  │
│  │  ├─ Components (Navbar, PropertyCard, etc.)              │  │
│  │  ├─ Context (AuthContext)                                │  │
│  │  ├─ Services (API Client - Axios)                        │  │
│  │  └─ Styles (CSS Modules)                                 │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              │ HTTP/HTTPS                        │
│                              │ WebSocket (Messages)              │
└──────────────────────────────┼───────────────────────────────────┘
                               │
┌──────────────────────────────┼───────────────────────────────────┐
│                          API LAYER                                │
├──────────────────────────────┼───────────────────────────────────┤
│                              ▼                                    │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │         Django REST Framework (Port 8000)                 │   │
│  │                                                            │   │
│  │  ┌────────────────────────────────────────────────────┐  │   │
│  │  │              URL Router                             │  │   │
│  │  │  /api/users/     → User endpoints                  │  │   │
│  │  │  /api/properties/→ Property endpoints              │  │   │
│  │  │  /api/bookings/  → Booking endpoints               │  │   │
│  │  │  /api/payments/  → Payment endpoints               │  │   │
│  │  │  /api/reviews/   → Review endpoints                │  │   │
│  │  │  /api/messages/  → Message endpoints               │  │   │
│  │  └────────────────────────────────────────────────────┘  │   │
│  │                                                            │   │
│  │  ┌────────────────────────────────────────────────────┐  │   │
│  │  │           Middleware                                │  │   │
│  │  │  ├─ CORS Handler                                   │  │   │
│  │  │  ├─ JWT Authentication                             │  │   │
│  │  │  ├─ Session Management                             │  │   │
│  │  │  └─ Security Headers                               │  │   │
│  │  └────────────────────────────────────────────────────┘  │   │
│  │                                                            │   │
│  │  ┌────────────────────────────────────────────────────┐  │   │
│  │  │              Apps/Modules                           │  │   │
│  │  │                                                     │  │   │
│  │  │  Users App                                         │  │   │
│  │  │  ├─ Models (Custom User)                          │  │   │
│  │  │  ├─ Serializers                                   │  │   │
│  │  │  ├─ Views (Register, Login, Profile)              │  │   │
│  │  │  └─ Permissions                                    │  │   │
│  │  │                                                     │  │   │
│  │  │  Properties App                                    │  │   │
│  │  │  ├─ Models (Property, PropertyImage)              │  │   │
│  │  │  ├─ Serializers                                   │  │   │
│  │  │  ├─ Views (CRUD, Search, Filter)                  │  │   │
│  │  │  └─ File Uploads                                   │  │   │
│  │  │                                                     │  │   │
│  │  │  Bookings App                                      │  │   │
│  │  │  ├─ Models (Booking with validation)              │  │   │
│  │  │  ├─ Serializers                                   │  │   │
│  │  │  ├─ Views (Create, List, Update)                  │  │   │
│  │  │  └─ Availability Logic                            │  │   │
│  │  │                                                     │  │   │
│  │  │  Payments App                                      │  │   │
│  │  │  ├─ Models (Payment)                              │  │   │
│  │  │  ├─ Serializers                                   │  │   │
│  │  │  └─ Views (Process Payment)                       │  │   │
│  │  │                                                     │  │   │
│  │  │  Reviews App                                       │  │   │
│  │  │  ├─ Models (Review with ratings)                  │  │   │
│  │  │  ├─ Serializers                                   │  │   │
│  │  │  └─ Views (CRUD)                                   │  │   │
│  │  │                                                     │  │   │
│  │  │  Messages App                                      │  │   │
│  │  │  ├─ Models (Message)                              │  │   │
│  │  │  ├─ Serializers                                   │  │   │
│  │  │  ├─ Views (HTTP endpoints)                        │  │   │
│  │  │  ├─ Consumers (WebSocket)                         │  │   │
│  │  │  └─ Routing (WebSocket URLs)                      │  │   │
│  │  └────────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────┘   │
│                              │                                    │
└──────────────────────────────┼────────────────────────────────────┘
                               │
┌──────────────────────────────┼────────────────────────────────────┐
│                       DATA LAYER                                   │
├──────────────────────────────┼────────────────────────────────────┤
│                              ▼                                     │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │              PostgreSQL Database                         │     │
│  │                                                           │     │
│  │  Tables:                                                 │     │
│  │  ├─ users           (User authentication & profiles)    │     │
│  │  ├─ properties      (Property listings)                 │     │
│  │  ├─ property_images (Property photos)                   │     │
│  │  ├─ bookings        (Reservations)                      │     │
│  │  ├─ payments        (Payment records)                   │     │
│  │  ├─ reviews         (Property reviews)                  │     │
│  │  └─ messages        (User messages)                     │     │
│  │                                                           │     │
│  │  Indexes:                                                │     │
│  │  ├─ idx_user_email                                      │     │
│  │  ├─ idx_property_host                                   │     │
│  │  ├─ idx_booking_property                                │     │
│  │  └─ ... (optimized for queries)                         │     │
│  └─────────────────────────────────────────────────────────┘     │
│                                                                    │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │              Redis (Session & WebSocket)                 │     │
│  │                                                           │     │
│  │  ├─ Channel Layers (for Django Channels)                │     │
│  │  ├─ WebSocket connections                               │     │
│  │  └─ Real-time message routing                           │     │
│  └─────────────────────────────────────────────────────────┘     │
│                                                                    │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │              File Storage                                │     │
│  │                                                           │     │
│  │  /media/                                                 │     │
│  │  ├─ profiles/      (User profile pictures)              │     │
│  │  └─ properties/    (Property images)                    │     │
│  └─────────────────────────────────────────────────────────┘     │
└────────────────────────────────────────────────────────────────────┘
```

## Data Flow

### 1. User Registration Flow
```
User Input → React Form → Axios POST /api/users/register/
→ Django Serializer Validation → Create User in DB
→ Generate JWT Tokens → Return to Frontend
→ Store in localStorage → Redirect to Home
```

### 2. Property Listing Flow
```
Page Load → React useEffect → Axios GET /api/properties/
→ Django View (with filters) → Query PostgreSQL
→ Serialize Data → Return JSON → Update React State → Render Cards
```

### 3. Booking Creation Flow
```
User Selects Dates → Submit Form → Axios POST /api/bookings/create/
→ Django View → Check Availability (DB Query)
→ Validate Dates → Calculate Price → Create Booking
→ Return Booking Data → Update UI
```

### 4. Real-time Messaging Flow
```
User Types Message → WebSocket Send
→ Django Consumer → Save to DB → Broadcast to Channel
→ Redis Layer → Send to Recipient → Update Chat UI
```

## Component Architecture

### Frontend Component Hierarchy
```
App
├── Navbar
├── Routes
│   ├── Home
│   │   └── PropertyCard (multiple)
│   ├── PropertyDetail
│   │   ├── Image Gallery
│   │   ├── Booking Form
│   │   └── Review List
│   ├── Bookings
│   │   └── Booking Card (multiple)
│   ├── HostDashboard
│   │   ├── Stats Cards
│   │   ├── Property Table
│   │   └── Booking Table
│   ├── Messages
│   │   ├── Conversation List
│   │   └── Message Thread
│   ├── Login
│   ├── Register
│   ├── Profile
│   └── CreateProperty
```

### Backend App Structure
```
Django Project
├── airbnb_project (settings, URLs, ASGI/WSGI)
└── apps/
    ├── users/
    │   ├── models.py (User)
    │   ├── serializers.py
    │   ├── views.py
    │   └── admin.py
    ├── properties/
    │   ├── models.py (Property, PropertyImage)
    │   ├── serializers.py
    │   ├── views.py
    │   └── admin.py
    ├── bookings/
    │   ├── models.py (Booking)
    │   ├── serializers.py
    │   ├── views.py
    │   └── admin.py
    ├── payments/
    │   ├── models.py (Payment)
    │   ├── serializers.py
    │   ├── views.py
    │   └── admin.py
    ├── reviews/
    │   ├── models.py (Review)
    │   ├── serializers.py
    │   ├── views.py
    │   └── admin.py
    └── messages/
        ├── models.py (Message)
        ├── serializers.py
        ├── views.py
        ├── consumers.py (WebSocket)
        ├── routing.py
        └── admin.py
```

## Security Architecture

### Authentication Flow
```
1. User Login → Credentials
2. Backend validates → User model
3. Generate JWT tokens (access + refresh)
4. Return tokens to frontend
5. Store in localStorage
6. Include in Authorization header for API calls
7. Backend validates JWT on each request
8. Refresh token when access token expires
```

### Authorization Levels
```
Public:
- View properties
- View reviews

Authenticated (Guest):
- Create bookings
- Submit reviews
- Send messages
- View own bookings

Authenticated (Host):
- All Guest permissions
- Create properties
- Manage own properties
- View host dashboard
- Manage property bookings

Admin:
- Full system access
- Django admin panel
- Manage all users/data
```

## Database Schema Relationships

```
User (1) ──────── (N) Property (host_id)
User (1) ──────── (N) Booking (user_id)
User (1) ──────── (N) Review (user_id)
User (1) ──────── (N) Message (sender_id)
User (1) ──────── (N) Message (recipient_id)

Property (1) ──── (N) PropertyImage
Property (1) ──── (N) Booking
Property (1) ──── (N) Review

Booking (1) ───── (N) Payment
```

## Technology Decisions

### Why Django REST Framework?
- Powerful ORM for database operations
- Built-in authentication
- Excellent serialization
- Auto-generated API documentation
- Large ecosystem

### Why React?
- Component-based architecture
- Virtual DOM for performance
- Large community and ecosystem
- Easy state management
- Reusable components

### Why PostgreSQL?
- Robust relational database
- ACID compliance
- Great for complex queries
- JSON support
- Scalable

### Why JWT?
- Stateless authentication
- Scalable across multiple servers
- Secure token-based auth
- Works well with SPAs
- Industry standard

### Why Redis?
- Fast in-memory data store
- Perfect for WebSocket channels
- Session management
- Caching capabilities

## Performance Considerations

### Database Optimization
- Indexes on foreign keys
- Efficient queries with select_related
- Pagination for large datasets

### Frontend Optimization
- Code splitting
- Lazy loading images
- Efficient state updates
- Debounced search

### API Optimization
- Pagination
- Field filtering
- Query optimization
- Caching (future)

## Scalability

### Horizontal Scaling
- Stateless API (JWT)
- Load balancer ready
- Database connection pooling
- Static file CDN (future)

### Vertical Scaling
- Optimized queries
- Efficient indexing
- Redis caching
- Image optimization

---

This architecture is designed to be:
- **Modular**: Easy to add/remove features
- **Scalable**: Can handle growth
- **Maintainable**: Clean code structure
- **Secure**: Multiple security layers
- **Performant**: Optimized queries and rendering
