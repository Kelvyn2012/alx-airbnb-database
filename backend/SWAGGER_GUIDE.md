# Swagger API Testing Guide

## Quick Start

Your Airbnb Clone API now has interactive Swagger documentation for easy endpoint testing!

### Access Swagger UI

**Local Development:**
- Swagger UI: http://localhost:8001/swagger/
- Alternative: http://localhost:8001/docs/
- ReDoc: http://localhost:8001/redoc/
- API Root: http://localhost:8001/

**Production:**
- Swagger UI: https://alx-airbnb-clone.onrender.com/swagger/
- ReDoc: https://alx-airbnb-clone.onrender.com/redoc/

## How to Test Endpoints with Swagger

### Step 1: Access Swagger UI
Open your browser and navigate to http://localhost:8001/swagger/

### Step 2: Register a New User (First Time)

1. Find the **POST /api/users/register/** endpoint
2. Click "Try it out"
3. Fill in the request body:
```json
{
  "email": "test@example.com",
  "username": "testuser",
  "password": "SecurePass123!",
  "first_name": "Test",
  "last_name": "User",
  "role": "guest"
}
```
4. Click "Execute"
5. Copy the `access` token from the response

### Step 3: Authenticate Your Requests

1. Click the **Authorize** button (🔒) at the top right of Swagger UI
2. In the "Value" field, enter: `Bearer YOUR_ACCESS_TOKEN`
   - Replace `YOUR_ACCESS_TOKEN` with the token from Step 2
   - Example: `Bearer eyJ0eXAiOiJKV1QiLCJhbGc...`
3. Click "Authorize"
4. Click "Close"

### Step 4: Test Protected Endpoints

Now you can test any endpoint! All your requests will include the authentication token automatically.

**Examples to try:**

- **GET /api/users/profile/** - Get your profile
- **GET /api/properties/** - List all properties
- **POST /api/properties/** - Create a new property
- **GET /api/bookings/** - View your bookings

### Step 5: Login (Returning Users)

1. Find the **POST /api/users/login/** endpoint
2. Click "Try it out"
3. Fill in your credentials:
```json
{
  "email": "test@example.com",
  "password": "SecurePass123!"
}
```
4. Click "Execute"
5. Copy the new `access` token
6. Use the Authorize button to update your token

## Common Testing Workflows

### Testing Property Creation

1. Authenticate as a host user
2. POST /api/properties/ with property details:
```json
{
  "name": "Cozy Beach House",
  "description": "Beautiful oceanfront property",
  "location": "123 Beach Ave, Miami, FL",
  "price_per_night": 150.00,
  "latitude": 25.7617,
  "longitude": -80.1918
}
```

### Testing Booking Flow

1. Authenticate as a guest user
2. GET /api/properties/ to find a property
3. POST /api/bookings/ to create a booking:
```json
{
  "property_id": "property-uuid-here",
  "start_date": "2025-12-10",
  "end_date": "2025-12-15",
  "guests": 2
}
```

### Testing Reviews

1. Complete a booking
2. POST /api/reviews/ to add a review:
```json
{
  "property_id": "property-uuid-here",
  "rating": 5,
  "comment": "Amazing stay! Highly recommend."
}
```

## Token Management

### Access Token Expired?

When your access token expires (after 1 hour), use the refresh token:

1. Find **POST /api/users/token/refresh/**
2. Enter your refresh token:
```json
{
  "refresh": "your-refresh-token-here"
}
```
3. Get a new access token
4. Update the Authorize section with the new token

### Token Lifetime Settings

- Access Token: 1 hour
- Refresh Token: 7 days
- After 7 days, you'll need to login again

## Features Available in Swagger

- **Try it out**: Test any endpoint directly from the browser
- **Request body schema**: See required/optional fields with descriptions
- **Response examples**: View sample responses for each endpoint
- **Authentication**: Built-in JWT token management
- **Filters & Pagination**: Test query parameters
- **Multiple formats**: Download OpenAPI spec in JSON/YAML

## Troubleshooting

### "401 Unauthorized" Error
- Your token expired or is invalid
- Re-authenticate using the Authorize button
- Make sure you included "Bearer " before the token

### "403 Forbidden" Error
- You don't have permission for this action
- Check if your user role matches the endpoint requirements
- Hosts can create properties, guests can make bookings

### "400 Bad Request" Error
- Check the request body format
- Ensure all required fields are included
- Validate data types (strings, numbers, dates)

### Server Not Running
```bash
cd backend
source venv/bin/activate
python manage.py runserver 8001
```

## Advanced Testing

### Testing File Uploads
Some endpoints accept file uploads (property images):
1. Click "Try it out"
2. Use the file upload button
3. Select your image file
4. Execute the request

### Testing Filters
Many list endpoints support filtering:
- GET /api/properties/?location=Miami
- GET /api/properties/?min_price=100&max_price=500
- GET /api/bookings/?status=pending

### Testing Pagination
List endpoints are paginated (20 items per page):
- GET /api/properties/?page=1
- GET /api/properties/?page=2

## Alternative: ReDoc Documentation

For a different view of your API:
- Visit http://localhost:8001/redoc/
- ReDoc provides a cleaner, more readable documentation format
- Great for sharing with frontend developers
- No interactive testing (read-only)

## Exporting API Documentation

Download OpenAPI specification:
- JSON: http://localhost:8001/swagger.json/
- YAML: http://localhost:8001/swagger.yaml/

Use these files with:
- Postman (import OpenAPI spec)
- Insomnia (import OpenAPI spec)
- Code generation tools
- API gateway configuration

## Production Testing

When testing on Render (production):

1. Use HTTPS URLs: https://alx-airbnb-clone.onrender.com/swagger/
2. Set environment variables on Render:
   - DEBUG=False
   - BACKEND_URL=https://alx-airbnb-clone.onrender.com
3. CSRF tokens are required in production
4. Same authentication flow as local development

## Tips for Efficient Testing

1. **Create test data sets**: Register multiple users (guest, host, admin)
2. **Save tokens**: Keep a text file with your test user tokens
3. **Use browser DevTools**: Monitor network requests for debugging
4. **Test edge cases**: Try invalid data, missing fields, wrong types
5. **Check error messages**: Swagger shows detailed error responses

## Next Steps

- Test all user endpoints (register, login, profile)
- Create properties as a host user
- Make bookings as a guest user
- Test payment workflows with Stripe
- Try real-time messaging features
- Leave reviews on properties

Happy Testing! 🚀
