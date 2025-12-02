# Postman Collection - Quick Start

## 📦 What's Included

This folder contains a complete Postman collection for testing your Airbnb Clone API:

1. **Airbnb_API.postman_collection.json** - Complete API test collection
2. **Airbnb_Local.postman_environment.json** - Local development environment
3. **Airbnb_Production.postman_environment.json** - Production environment
4. **POSTMAN_TESTING_GUIDE.md** - Comprehensive testing guide
5. **API_ENDPOINTS_REFERENCE.md** - Quick reference for all endpoints

## 🚀 Quick Start (3 Steps)

### Step 1: Import into Postman

1. Open Postman desktop app
2. Click **Import** button
3. Select all `.json` files from this folder
4. Click **Import**

### Step 2: Select Environment

- Top-right corner → Select **Airbnb Local Environment**

### Step 3: Start Testing

1. Start your Django server:
   ```bash
   python3.12 manage.py runserver
   ```

2. Open collection → **Authentication** folder
3. Run **Register User** request
4. Start testing other endpoints!

## 📋 Collection Overview

The collection includes **40+ requests** organized in 9 folders:

```
Airbnb Clone API/
├── Authentication (4 requests)
│   ├── Register User
│   ├── Login User
│   ├── Refresh Token
│   └── ...
│
├── Users (3 requests)
│   ├── Get Profile
│   ├── Update Profile
│   └── Get User Detail
│
├── Properties (7 requests)
│   ├── List All Properties
│   ├── Create Property
│   ├── Get Property Detail
│   ├── Update Property
│   ├── Delete Property
│   ├── Get My Properties
│   └── Upload Images
│
├── Bookings (5 requests)
│   ├── List My Bookings
│   ├── Create Booking
│   ├── Get Booking Detail
│   ├── Update Booking
│   ├── Cancel Booking
│   └── Host Bookings
│
├── Payments (3 requests)
│   ├── List Payments
│   ├── Create Payment
│   └── Get Payment Detail
│
├── Reviews (5 requests)
│   ├── Get Property Reviews
│   ├── Create Review
│   ├── Get Review Detail
│   ├── Update Review
│   └── Delete Review
│
├── Messages (4 requests)
│   ├── List Messages
│   ├── Create Message
│   ├── Get Conversation
│   └── Get Message Detail
│
├── OAuth (2 requests)
│   ├── Google Login
│   └── Facebook Login
│
└── API Documentation (2 requests)
    ├── Swagger UI
    └── ReDoc
```

## ✨ Smart Features

### 1. Auto-Save Tokens
Login/Register requests automatically save your access token:
```javascript
// No manual copy-paste needed!
pm.collectionVariables.set('access_token', jsonData.access);
```

### 2. Auto-Save IDs
Created resource IDs are automatically saved:
- `property_id` - After creating property
- `booking_id` - After creating booking
- `payment_id` - After creating payment
- `review_id` - After creating review
- `message_id` - After creating message

### 3. Built-in Authentication
Collection-level Bearer Token auth:
- Set once, works everywhere
- Automatically uses `{{access_token}}`
- Some public endpoints override (e.g., property listing)

### 4. Environment Variables
Switch between local and production instantly:
```
{{base_url}} automatically changes
Local:      http://localhost:8000
Production: https://your-backend.vercel.app
```

## 🧪 Testing Workflow

### For First-Time Testing:

```
1. Register User       → Saves access_token
2. Create Property     → Saves property_id
3. Create Booking      → Saves booking_id
4. Create Payment      → Saves payment_id
5. Create Review       → Saves review_id
6. Test other endpoints...
```

### For Returning Tests:

```
1. Login User          → Updates access_token
2. Continue testing...
```

## 📊 Response Examples

Every request includes example responses. To view:

1. Click on a request
2. Look for **Examples** tab
3. See sample successful responses

## 🔧 Customization

### Change Base URL

**Local Environment:**
```json
"base_url": "http://localhost:8000"
```

**Production Environment:**
```json
"base_url": "https://your-backend.vercel.app"
```

### Update After Deployment

1. Click environment dropdown
2. Click edit icon
3. Update `base_url` to your Vercel URL
4. Save

## 🎯 Common Use Cases

### Test as Guest User

```
1. Register (role: "guest")
2. Browse Properties
3. Create Booking
4. Make Payment
5. Leave Review
```

### Test as Host User

```
1. Register (role: "host")
2. Create Property
3. Upload Images
4. Check Bookings
5. View Reviews
```

### Test Messaging

```
1. Register User A
2. Register User B
3. Login as User A
4. Send Message to User B
5. Login as User B
6. View Conversation
```

## 📝 Important Notes

### Authentication Required

Most endpoints require authentication. Look for 🔒 icon in Postman.

### User Roles Matter

- **Guest**: Can book, review, message
- **Host**: Can do everything guest can + create/manage properties
- **Admin**: Full access

### Test Stripe Token

For development, use: `"stripe_token": "tok_visa"`

### Date Format

Always use: `"YYYY-MM-DD"` (e.g., `"2024-12-15"`)

## 🐛 Troubleshooting

### "401 Unauthorized"
- **Solution**: Run Login request again
- Access token may have expired

### "403 Forbidden"
- **Solution**: Check if you have correct role
- Example: Creating property requires host role

### "404 Not Found"
- **Solution**: Verify the resource ID exists
- Check `{{property_id}}` variable is set

### Variables Not Updating
- **Solution**: Check the **Tests** tab on requests
- Scripts should be saving variables automatically

### CORS Errors
- **Solution**: Use Postman desktop app
- Not the web version

## 📚 Documentation

For detailed information, see:

1. **POSTMAN_TESTING_GUIDE.md** - Complete testing guide
2. **API_ENDPOINTS_REFERENCE.md** - All endpoints reference
3. **Swagger**: http://localhost:8000/swagger/
4. **ReDoc**: http://localhost:8000/redoc/

## 💡 Pro Tips

### Run Collection
Test all endpoints at once:
1. Click collection name
2. Click **Run** button
3. Select requests to run
4. Click **Run Airbnb Clone API**

### Share with Team
Share the collection:
1. Right-click collection
2. **Export**
3. Share `.json` file
4. Team imports into their Postman

### Save Example Responses
After successful request:
1. Click **Save Response**
2. Name it (e.g., "Success - Property Created")
3. Example saved for reference

### Use Console
View all requests:
1. Open Postman Console (bottom left)
2. See request/response details
3. Debug issues

## 🎬 Getting Started Video Tutorial

1. Import collection ✅
2. Select environment ✅
3. Start server ✅
4. Run "Register User" ✅
5. Check response ✅
6. View saved variables ✅
7. Test other endpoints ✅

## 🆘 Need Help?

1. Check **POSTMAN_TESTING_GUIDE.md** for detailed steps
2. View **API_ENDPOINTS_REFERENCE.md** for endpoint details
3. Check Django server logs for errors
4. Visit http://localhost:8000/swagger/ for API docs

## 🌟 What's Next?

After testing locally:
1. Deploy to Vercel (see DEPLOYMENT_GUIDE.md)
2. Update Production environment base_url
3. Test production endpoints
4. Share collection with frontend team

---

**Happy Testing!** 🚀

If you find any issues or have suggestions, feel free to update the collection!
