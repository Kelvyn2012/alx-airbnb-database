# Postman API Testing Guide

This guide will help you test your Airbnb Clone API using the provided Postman collection.

## 📦 Files Included

1. **Airbnb_API.postman_collection.json** - Complete API collection with all endpoints
2. **Airbnb_Local.postman_environment.json** - Local development environment
3. **Airbnb_Production.postman_environment.json** - Production environment (Vercel)

## 🚀 Getting Started

### Step 1: Import Collection and Environments

1. Open Postman
2. Click **Import** button (top left)
3. Drag and drop or select these files:
   - `Airbnb_API.postman_collection.json`
   - `Airbnb_Local.postman_environment.json`
   - `Airbnb_Production.postman_environment.json`

### Step 2: Select Environment

1. In the top-right corner, click the environment dropdown
2. Select **Airbnb Local Environment** for local testing
3. Or select **Airbnb Production Environment** for production testing

### Step 3: Start Your Local Server

```bash
cd backend
source venv/bin/activate
python3.12 manage.py runserver
```

Your API should now be running at `http://localhost:8000`

## 📋 Collection Structure

The collection is organized into these folders:

1. **Authentication** - Register, Login, Token Refresh
2. **Users** - User profile management
3. **Properties** - Property listings CRUD operations
4. **Bookings** - Booking management
5. **Payments** - Payment processing
6. **Reviews** - Property reviews
7. **Messages** - User messaging
8. **OAuth** - Google and Facebook authentication
9. **API Documentation** - Swagger and ReDoc

## 🧪 Testing Workflow

### Complete Test Flow (Recommended Order):

#### 1. Authentication Flow

**A. Register a Guest User**
```
POST /api/users/register/
```
- Use the "Register User" request
- The collection will automatically save the access token
- Default role: "guest"

**B. Register a Host User** (for creating properties)
- Modify the registration request
- Change `"role": "guest"` to `"role": "host"`
- Use a different email

**C. Login**
```
POST /api/users/login/
```
- Login with your registered credentials
- Access token is auto-saved

**D. Refresh Token**
```
POST /api/users/token/refresh/
```
- Use when your access token expires
- Automatically updates the access token

#### 2. User Management

**Get User Profile**
```
GET /api/users/profile/
```
- View current user's profile
- Requires authentication

**Update Profile**
```
PUT /api/users/profile/
```
- Update user information
- Requires authentication

#### 3. Properties Flow

**A. Create Property** (requires host role)
```
POST /api/properties/create/
```
- Login as a host user first
- Property ID is auto-saved to `{{property_id}}`

**B. List All Properties**
```
GET /api/properties/
```
- No authentication required
- Supports filtering by location, price, bedrooms

**C. Get Property Detail**
```
GET /api/properties/{{property_id}}/
```
- View single property details

**D. Upload Property Images**
```
POST /api/properties/{{property_id}}/images/
```
- Upload images for your property
- Requires authentication (must be property owner)

**E. Get My Properties**
```
GET /api/properties/my-properties/
```
- View all properties you've created

#### 4. Bookings Flow

**A. Create Booking** (requires guest account)
```
POST /api/bookings/create/
```
- Must have a valid property_id
- Booking ID is auto-saved

**B. List My Bookings**
```
GET /api/bookings/
```
- View all your bookings

**C. Host - View Property Bookings**
```
GET /api/bookings/host/
```
- Login as host to see bookings for your properties

**D. Update Booking**
```
PUT /api/bookings/{{booking_id}}/
```
- Modify booking dates or guest count

**E. Cancel Booking**
```
DELETE /api/bookings/{{booking_id}}/
```

#### 5. Payments Flow

**A. Create Payment**
```
POST /api/payments/create/
```
- Requires booking_id
- Use test Stripe token: `tok_visa`
- Payment ID is auto-saved

**B. List Payments**
```
GET /api/payments/
```
- View all your payments

**C. Get Payment Detail**
```
GET /api/payments/{{payment_id}}/
```

#### 6. Reviews Flow

**A. Create Review**
```
POST /api/reviews/create/
```
- Must have completed booking
- Rating: 1-5
- Review ID is auto-saved

**B. Get Property Reviews**
```
GET /api/reviews/property/{{property_id}}/
```
- View all reviews for a property
- No authentication required

**C. Update Review**
```
PUT /api/reviews/{{review_id}}/
```
- Only review author can update

**D. Delete Review**
```
DELETE /api/reviews/{{review_id}}/
```

#### 7. Messages Flow

**A. Send Message**
```
POST /api/messages/create/
```
- Send message to another user
- Requires recipient_id

**B. View All Messages**
```
GET /api/messages/
```
- Get all your messages

**C. Get Conversation**
```
GET /api/messages/conversation/{{user_id}}/
```
- View message thread with specific user

## 🔐 Authentication

### JWT Token Authentication

The collection uses Bearer Token authentication:
- Automatically set after login/register
- Stored in `{{access_token}}` variable
- Token expires after 1 hour (default)
- Use refresh token endpoint to get new access token

### Manual Token Setup (if needed)

1. Copy your access token from login response
2. Go to Collection → Authorization tab
3. Select "Bearer Token"
4. Paste token in the Token field

Or update the environment variable:
1. Click environment dropdown
2. Click the eye icon
3. Edit `access_token` value

## 📝 Variables

The collection uses these variables (auto-updated):

| Variable | Description | Auto-Updated |
|----------|-------------|--------------|
| `base_url` | API base URL | No |
| `access_token` | JWT access token | Yes (on login/register) |
| `refresh_token` | JWT refresh token | Yes (on login/register) |
| `user_id` | Current user ID | Yes (on login/register) |
| `property_id` | Last created property | Yes (on property create) |
| `booking_id` | Last created booking | Yes (on booking create) |
| `payment_id` | Last created payment | Yes (on payment create) |
| `review_id` | Last created review | Yes (on review create) |
| `message_id` | Last created message | Yes (on message create) |

## 🧪 Testing Scenarios

### Scenario 1: Guest Books a Property

1. Register as guest
2. Browse properties (List All Properties)
3. View property details
4. Create booking
5. Create payment
6. Leave review

### Scenario 2: Host Manages Property

1. Register as host
2. Create property
3. Upload property images
4. View my properties
5. Check incoming bookings (Host Bookings)

### Scenario 3: User Communication

1. Register two users
2. Login as user 1
3. Send message to user 2
4. Login as user 2
5. View conversation
6. Reply to message

## 🔍 Query Parameters

### Properties Filtering

```
GET /api/properties/?location=Miami&min_price=100&max_price=300&bedrooms=2
```

Available filters:
- `location` - Filter by location
- `min_price` - Minimum price per night
- `max_price` - Maximum price per night
- `bedrooms` - Number of bedrooms
- `page` - Page number (default: 1)
- `page_size` - Items per page (default: 20)

### Pagination

Most list endpoints support pagination:
```
GET /api/bookings/?page=1&page_size=10
```

## 🐛 Troubleshooting

### 401 Unauthorized

**Problem:** Getting 401 errors on authenticated endpoints

**Solutions:**
1. Check if you're logged in
2. Verify access token is set
3. Check if token expired (refresh it)
4. Ensure Authorization header is set to Bearer Token

### 403 Forbidden

**Problem:** Getting 403 errors

**Solutions:**
1. Verify you have the correct role (e.g., host for creating properties)
2. Check if you own the resource you're trying to modify
3. Ensure you're using the correct user account

### 404 Not Found

**Problem:** Endpoint returns 404

**Solutions:**
1. Check the URL is correct
2. Verify the resource ID exists
3. Ensure trailing slashes match the API endpoints

### CORS Errors (when testing from browser)

**Problem:** CORS policy blocking requests

**Solution:**
- Use Postman desktop app instead of web version
- Or add your origin to `CORS_ALLOWED_ORIGINS` in settings.py

### Token Expired

**Problem:** "Token is invalid or expired"

**Solution:**
Use the "Refresh Token" endpoint:
```
POST /api/users/token/refresh/
Body: { "refresh": "{{refresh_token}}" }
```

## 📊 Response Status Codes

| Code | Meaning | Common Scenarios |
|------|---------|------------------|
| 200 | OK | Successful GET, PUT, PATCH |
| 201 | Created | Successful POST (resource created) |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Invalid data sent |
| 401 | Unauthorized | Not logged in or token expired |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Backend error (check logs) |

## 🔄 Environment Switching

### Local Development
```
base_url = http://localhost:8000
```

### Production (Vercel)
```
base_url = https://your-backend.vercel.app
```

To switch:
1. Click environment dropdown
2. Select desired environment
3. All requests will use that base URL

## 📱 Testing OAuth (Google/Facebook)

OAuth endpoints require browser interaction:

1. Use "Google Login" or "Facebook Login" requests
2. Copy the URL from Postman
3. Paste in browser
4. Complete OAuth flow
5. You'll be redirected with tokens in URL

Note: Configure OAuth credentials in your `.env` file first.

## 💡 Pro Tips

1. **Use Collection Runner** for automated testing:
   - Click on collection → Run
   - Select requests to run
   - See all tests execute automatically

2. **Save Responses** for reference:
   - Click "Save Response" after request
   - Create examples for different scenarios

3. **Use Pre-request Scripts** for dynamic data:
   - Already configured for token management
   - Automatically saves IDs from responses

4. **Environment Variables** for team sharing:
   - Share collection and environment files
   - Each team member can have their own tokens

5. **Test Scripts** are included:
   - Auto-save tokens on login
   - Auto-save IDs on resource creation
   - Check response status codes

## 📚 Additional Resources

- **Swagger UI**: http://localhost:8000/swagger/
- **ReDoc**: http://localhost:8000/redoc/
- **Django Admin**: http://localhost:8000/admin/

## 🆘 Need Help?

1. Check API documentation at `/swagger/`
2. View Django server logs for errors
3. Verify database has data (use Django admin)
4. Check environment variables are set correctly

## 📝 Sample Test Data

### Guest User
```json
{
  "email": "guest@example.com",
  "password": "GuestPassword123!",
  "first_name": "Jane",
  "last_name": "Doe",
  "role": "guest"
}
```

### Host User
```json
{
  "email": "host@example.com",
  "password": "HostPassword123!",
  "first_name": "John",
  "last_name": "Host",
  "role": "host"
}
```

### Sample Property
```json
{
  "name": "Cozy Beach House",
  "description": "Beautiful beachfront property",
  "location": "Miami, FL",
  "pricepernight": "150.00",
  "bedrooms": 2,
  "bathrooms": 2,
  "max_guests": 4,
  "amenities": "WiFi, Pool, Kitchen, AC"
}
```

---

Happy Testing! 🚀
