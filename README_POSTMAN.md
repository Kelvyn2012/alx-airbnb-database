# 🚀 Airbnb Clone API - Postman Collection

Complete Postman collection for testing all API endpoints of the Airbnb Clone backend.

## 📦 Quick Access

All Postman files are located in the `backend/` folder:

### Postman Collection Files
- [Airbnb_API.postman_collection.json](backend/Airbnb_API.postman_collection.json) - Main collection (40+ requests)
- [Airbnb_Local.postman_environment.json](backend/Airbnb_Local.postman_environment.json) - Local environment
- [Airbnb_Production.postman_environment.json](backend/Airbnb_Production.postman_environment.json) - Production environment

### Documentation
- [POSTMAN_README.md](backend/POSTMAN_README.md) - Quick start guide
- [POSTMAN_TESTING_GUIDE.md](backend/POSTMAN_TESTING_GUIDE.md) - Comprehensive testing guide
- [API_ENDPOINTS_REFERENCE.md](backend/API_ENDPOINTS_REFERENCE.md) - API endpoints reference

## 🎯 Quick Start (3 Steps)

### 1. Import into Postman
```bash
# Open Postman → Import → Select files:
backend/Airbnb_API.postman_collection.json
backend/Airbnb_Local.postman_environment.json
backend/Airbnb_Production.postman_environment.json
```

### 2. Start Your Server
```bash
cd backend
source venv/bin/activate
python3.12 manage.py runserver
```

### 3. Start Testing
- Open collection → Authentication → Register User
- Token auto-saves!
- Test other endpoints

## 📋 What's Included

### 40+ Requests in 9 Categories

```
✅ Authentication (4)    - Register, Login, Refresh Token, OAuth
✅ Users (3)            - Profile management
✅ Properties (7)       - CRUD, Images, Filters
✅ Bookings (5)         - Create, Update, Cancel
✅ Payments (3)         - Stripe integration
✅ Reviews (5)          - Create, Update, Delete
✅ Messages (4)         - User messaging
✅ OAuth (2)            - Google, Facebook
✅ Documentation (2)    - Swagger, ReDoc
```

## ✨ Smart Features

- ✅ **Auto-save tokens** - Login once, use everywhere
- ✅ **Auto-save IDs** - Created resources automatically referenced
- ✅ **Built-in auth** - Bearer token set collection-wide
- ✅ **Environment switching** - Local ↔ Production with one click
- ✅ **Query parameters** - Pre-configured filters and pagination
- ✅ **Test scripts** - Automated variable management

## 🔍 API Coverage

### All Endpoints Tested

**Authentication & Users:**
- POST `/api/users/register/`
- POST `/api/users/login/`
- POST `/api/users/token/refresh/`
- GET/PUT `/api/users/profile/`

**Properties:**
- GET/POST `/api/properties/`
- GET/PUT/DELETE `/api/properties/{id}/`
- POST `/api/properties/{id}/images/`

**Bookings:**
- GET/POST `/api/bookings/`
- GET/PUT/DELETE `/api/bookings/{id}/`
- GET `/api/bookings/host/`

**Payments:**
- GET/POST `/api/payments/`
- GET `/api/payments/{id}/`

**Reviews:**
- GET/POST/PUT/DELETE `/api/reviews/`
- GET `/api/reviews/property/{id}/`

**Messages:**
- GET/POST `/api/messages/`
- GET `/api/messages/conversation/{user_id}/`

## 📖 Documentation

### Quick Reference
- [POSTMAN_README.md](backend/POSTMAN_README.md) - Get started in 3 steps
- [API_ENDPOINTS_REFERENCE.md](backend/API_ENDPOINTS_REFERENCE.md) - Quick API reference card

### Detailed Guide
- [POSTMAN_TESTING_GUIDE.md](backend/POSTMAN_TESTING_GUIDE.md) - Complete testing workflows

### Interactive Docs
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## 🧪 Testing Workflows

### Complete Guest Journey
```
1. Register User (guest)
2. Browse Properties
3. View Property Details
4. Create Booking
5. Process Payment
6. Leave Review
```

### Complete Host Journey
```
1. Register User (host)
2. Create Property
3. Upload Images
4. View Bookings
5. Check Reviews
```

## 🔐 Authentication

### How It Works
1. Register or Login → Access token auto-saved
2. Token used in all authenticated requests
3. Refresh when expired (1 hour default)

### Manual Setup (if needed)
```
Collection → Authorization → Bearer Token
Token: {{access_token}}
```

## 🌍 Environments

### Local Development
```json
{
  "base_url": "http://localhost:8000"
}
```

### Production (Vercel)
```json
{
  "base_url": "https://your-backend.vercel.app"
}
```

**Switch environments**: Top-right dropdown → Select environment

## 💡 Usage Tips

### 1. Test in Order
Start with:
1. Authentication
2. Create resources (properties, bookings)
3. Test dependent endpoints

### 2. Use Collection Runner
- Click collection → Run
- Test all endpoints automatically
- Great for regression testing

### 3. Save Examples
- After successful request → Save Response
- Build example library for team

### 4. Check Variables
- Environment dropdown → Eye icon
- View all saved variables
- Verify tokens and IDs are set

## 🎨 Sample Requests

### Register User
```json
POST /api/users/register/
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "first_name": "John",
  "last_name": "Doe",
  "role": "guest"
}
```

### Create Property
```json
POST /api/properties/create/
{
  "name": "Beach House",
  "description": "Ocean view property",
  "location": "Miami, FL",
  "pricepernight": "250.00",
  "bedrooms": 3,
  "bathrooms": 2,
  "max_guests": 6,
  "amenities": "WiFi, Pool, Kitchen"
}
```

### Create Booking
```json
POST /api/bookings/create/
{
  "property_id": "{{property_id}}",
  "start_date": "2024-12-15",
  "end_date": "2024-12-20",
  "num_guests": 4
}
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| 401 Unauthorized | Login again - token expired |
| 403 Forbidden | Check user role permissions |
| 404 Not Found | Verify resource ID exists |
| CORS Error | Use Postman desktop app |
| Variables not saving | Check Test scripts tab |

## 📊 Collection Statistics

- **Total Requests**: 40+
- **Folders**: 9
- **Environments**: 2
- **Auto-Variables**: 8
- **Test Scripts**: 8
- **Coverage**: 100% of API endpoints

## 🔄 Development Workflow

### Initial Setup
```bash
# 1. Import collection
# 2. Select Local environment
# 3. Start server
cd backend
python3.12 manage.py runserver

# 4. Test in Postman
```

### After Code Changes
```bash
# 1. Restart server
# 2. Re-run collection
# 3. Verify all endpoints work
```

### Before Deployment
```bash
# 1. Test all endpoints locally
# 2. Fix any issues
# 3. Deploy to Vercel
# 4. Switch to Production environment
# 5. Test production endpoints
```

## 🚀 Deployment Testing

### After deploying to Vercel:

1. **Update Production Environment**
   ```json
   "base_url": "https://your-actual-backend.vercel.app"
   ```

2. **Switch Environment**
   - Top-right → Select "Airbnb Production Environment"

3. **Test All Endpoints**
   - Run collection or test individually
   - Verify CORS is configured
   - Check database connectivity

4. **Share with Frontend**
   - Export collection
   - Send to frontend team
   - They can test API integration

## 📁 File Structure

```
alx-airbnb-database/
├── backend/
│   ├── Airbnb_API.postman_collection.json       # Main collection
│   ├── Airbnb_Local.postman_environment.json    # Local env
│   ├── Airbnb_Production.postman_environment.json # Prod env
│   ├── POSTMAN_README.md                         # Quick start
│   ├── POSTMAN_TESTING_GUIDE.md                  # Full guide
│   └── API_ENDPOINTS_REFERENCE.md                # API reference
├── POSTMAN_COLLECTION_SUMMARY.md                 # Overview
└── README_POSTMAN.md                             # This file
```

## 🎯 Next Steps

1. ✅ Import collection into Postman
2. ✅ Read [POSTMAN_README.md](backend/POSTMAN_README.md) for quick start
3. ✅ Follow [POSTMAN_TESTING_GUIDE.md](backend/POSTMAN_TESTING_GUIDE.md) for workflows
4. ✅ Test all endpoints locally
5. ✅ Deploy backend (see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md))
6. ✅ Test production endpoints
7. ✅ Share collection with team

## 🌟 Features Highlight

### Automated Testing
- Auto-save access tokens
- Auto-save resource IDs
- Pre-configured test scripts
- One-click environment switching

### Complete Documentation
- Quick start guide
- Comprehensive testing guide
- API reference card
- Troubleshooting tips

### Production Ready
- Local and production environments
- CORS pre-configured
- Stripe test tokens included
- OAuth endpoints documented

## 💬 Support

For detailed help, see:
- [POSTMAN_README.md](backend/POSTMAN_README.md) - Quick start
- [POSTMAN_TESTING_GUIDE.md](backend/POSTMAN_TESTING_GUIDE.md) - Detailed guide
- [API_ENDPOINTS_REFERENCE.md](backend/API_ENDPOINTS_REFERENCE.md) - API reference

For deployment help:
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Full deployment guide
- [QUICK_DEPLOY.md](QUICK_DEPLOY.md) - Quick deployment checklist

---

**Ready to test your API!** 🎉

Import the collection and start testing in under 5 minutes.
