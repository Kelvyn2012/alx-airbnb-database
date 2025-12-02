# API Endpoints Quick Reference

## Base URL
- **Local**: `http://localhost:8000`
- **Production**: `https://your-backend.vercel.app`

## Authentication 🔐

All authenticated endpoints require:
```
Authorization: Bearer <access_token>
```

---

## 👤 Authentication & Users

### Register User
```http
POST /api/users/register/
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "first_name": "John",
  "last_name": "Doe",
  "role": "guest"  // or "host"
}
```

### Login
```http
POST /api/users/login/
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

### Refresh Token
```http
POST /api/users/token/refresh/
Content-Type: application/json

{
  "refresh": "<refresh_token>"
}
```

### Get Profile (Auth Required)
```http
GET /api/users/profile/
```

### Update Profile (Auth Required)
```http
PUT /api/users/profile/
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe Updated"
}
```

### Get User Detail
```http
GET /api/users/{user_id}/
```

---

## 🏠 Properties

### List All Properties (Public)
```http
GET /api/properties/
GET /api/properties/?location=Miami&min_price=100&max_price=300
```

### Create Property (Auth Required - Host)
```http
POST /api/properties/create/
Content-Type: application/json

{
  "name": "Beach House",
  "description": "Beautiful ocean view",
  "location": "Miami, FL",
  "pricepernight": "250.00",
  "bedrooms": 3,
  "bathrooms": 2,
  "max_guests": 6,
  "amenities": "WiFi, Pool, Kitchen"
}
```

### Get Property Detail (Public)
```http
GET /api/properties/{property_id}/
```

### Update Property (Auth Required - Owner)
```http
PUT /api/properties/{property_id}/
Content-Type: application/json

{
  "name": "Updated Beach House",
  "pricepernight": "275.00"
}
```

### Delete Property (Auth Required - Owner)
```http
DELETE /api/properties/{property_id}/
```

### Get My Properties (Auth Required - Host)
```http
GET /api/properties/my-properties/
```

### Upload Property Images (Auth Required - Owner)
```http
POST /api/properties/{property_id}/images/
Content-Type: multipart/form-data

image: <file>
is_primary: true
```

---

## 📅 Bookings

### List My Bookings (Auth Required)
```http
GET /api/bookings/
```

### Create Booking (Auth Required)
```http
POST /api/bookings/create/
Content-Type: application/json

{
  "property_id": "<uuid>",
  "start_date": "2024-12-15",
  "end_date": "2024-12-20",
  "num_guests": 4
}
```

### Get Booking Detail (Auth Required)
```http
GET /api/bookings/{booking_id}/
```

### Update Booking (Auth Required - Owner)
```http
PUT /api/bookings/{booking_id}/
Content-Type: application/json

{
  "start_date": "2024-12-16",
  "end_date": "2024-12-21"
}
```

### Cancel Booking (Auth Required - Owner)
```http
DELETE /api/bookings/{booking_id}/
```

### Host - Get Property Bookings (Auth Required - Host)
```http
GET /api/bookings/host/
```

---

## 💳 Payments

### List Payments (Auth Required)
```http
GET /api/payments/
```

### Create Payment (Auth Required)
```http
POST /api/payments/create/
Content-Type: application/json

{
  "booking_id": "<uuid>",
  "amount": "1250.00",
  "payment_method": "stripe",
  "stripe_token": "tok_visa"
}
```

### Get Payment Detail (Auth Required)
```http
GET /api/payments/{payment_id}/
```

---

## ⭐ Reviews

### Get Property Reviews (Public)
```http
GET /api/reviews/property/{property_id}/
```

### Create Review (Auth Required)
```http
POST /api/reviews/create/
Content-Type: application/json

{
  "property_id": "<uuid>",
  "booking_id": "<uuid>",
  "rating": 5,
  "comment": "Amazing property!"
}
```

### Get Review Detail (Public)
```http
GET /api/reviews/{review_id}/
```

### Update Review (Auth Required - Owner)
```http
PUT /api/reviews/{review_id}/
Content-Type: application/json

{
  "rating": 4,
  "comment": "Updated review text"
}
```

### Delete Review (Auth Required - Owner)
```http
DELETE /api/reviews/{review_id}/
```

---

## 💬 Messages

### List Messages (Auth Required)
```http
GET /api/messages/
```

### Create Message (Auth Required)
```http
POST /api/messages/create/
Content-Type: application/json

{
  "recipient_id": "<uuid>",
  "message_body": "Hi! I'm interested in your property."
}
```

### Get Conversation (Auth Required)
```http
GET /api/messages/conversation/{user_id}/
```

### Get Message Detail (Auth Required)
```http
GET /api/messages/{message_id}/
```

---

## 🔗 OAuth

### Google Login
```http
GET /api/users/auth/google/
```
Redirects to Google OAuth flow (use in browser)

### Google Callback
```http
GET /api/users/auth/google/callback/
```

### Facebook Login
```http
GET /api/users/auth/facebook/
```
Redirects to Facebook OAuth flow (use in browser)

### Facebook Callback
```http
GET /api/users/auth/facebook/callback/
```

---

## 📚 Documentation

### Swagger UI (Interactive API Docs)
```http
GET /swagger/
```

### ReDoc (Alternative API Docs)
```http
GET /redoc/
```

### Django Admin
```http
GET /admin/
```

---

## 🔍 Query Parameters

### Pagination (Most List Endpoints)
```
?page=1&page_size=20
```

### Property Filters
```
?location=Miami
?min_price=100
?max_price=300
?bedrooms=2
?bathrooms=2
```

---

## 📝 Response Codes

| Code | Status | Description |
|------|--------|-------------|
| 200 | OK | Success (GET, PUT) |
| 201 | Created | Success (POST) |
| 204 | No Content | Success (DELETE) |
| 400 | Bad Request | Invalid data |
| 401 | Unauthorized | Not authenticated |
| 403 | Forbidden | No permission |
| 404 | Not Found | Resource not found |
| 500 | Server Error | Backend error |

---

## 🎯 Common Workflows

### Complete Booking Flow
```
1. POST /api/users/register/        # Register guest
2. GET  /api/properties/            # Browse properties
3. GET  /api/properties/{id}/       # View property details
4. POST /api/bookings/create/       # Create booking
5. POST /api/payments/create/       # Process payment
6. POST /api/reviews/create/        # Leave review
```

### Host Property Management
```
1. POST /api/users/register/        # Register as host
2. POST /api/properties/create/     # Create property
3. POST /api/properties/{id}/images/# Upload images
4. GET  /api/bookings/host/         # Check bookings
5. GET  /api/reviews/property/{id}/ # View reviews
```

### Messaging Flow
```
1. POST /api/messages/create/       # Send message
2. GET  /api/messages/              # View all messages
3. GET  /api/messages/conversation/{user_id}/ # View thread
```

---

## 🔐 User Roles

### Guest
- Can book properties
- Can leave reviews
- Can send messages
- Cannot create properties

### Host
- All guest permissions
- Can create properties
- Can view property bookings
- Can manage their properties

### Admin
- All permissions
- Access to Django admin panel

---

## 💡 Testing Tips

### Test Stripe Token (Development)
```json
{
  "stripe_token": "tok_visa"
}
```

### Date Format
```
YYYY-MM-DD
Example: "2024-12-15"
```

### UUID Format
```
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Example: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
```

---

## 📞 Support

- **API Docs**: http://localhost:8000/swagger/
- **Django Admin**: http://localhost:8000/admin/
- **Postman Collection**: See `POSTMAN_TESTING_GUIDE.md`

---

**Last Updated**: December 2024
