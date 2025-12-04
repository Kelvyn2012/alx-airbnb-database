# Quick Start Guide

Get the Airbnb Clone running in 5 minutes!

## Prerequisites Check

Make sure you have:
- ✅ Python 12.x + installed (`python --version`)
- ✅ Node.js 14+ installed (`node --version`)
- ✅ PostgreSQL running
- ✅ Redis running (optional, for messaging)

## Quick Setup

### 1. Backend Setup (2 minutes)

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env

# Create database
createdb airbnb_db

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

Backend now running at: http://localhost:8000

### 2. Frontend Setup (1 minute)

Open a new terminal:

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Create environment
echo "REACT_APP_API_URL=http://localhost:8000" > .env

# Start server
npm start
```

Frontend now running at: http://localhost:3000

## First Steps

1. **Visit** http://localhost:3000
2. **Register** a new account (choose "Host" to list properties)
3. **Explore** the application!

### As a Guest:
- Browse properties
- Make bookings
- Write reviews
- Send messages

### As a Host:
- Add properties
- Upload property images
- Manage bookings
- View dashboard

### As Admin:
- Access admin panel at http://localhost:8000/admin/
- Manage all data

## API Documentation

Visit http://localhost:8000/swagger/ for interactive API docs

## Common Issues

### Port already in use?
```bash
# Backend (change port)
python manage.py runserver 8001

# Frontend (change in package.json or use different port)
PORT=3001 npm start
```

### Database connection error?
- Check PostgreSQL is running
- Verify database credentials in `.env`

### Redis error (messaging)?
- Install Redis: `brew install redis` (macOS) or `sudo apt install redis` (Ubuntu)
- Start Redis: `redis-server`

## Sample Data

Want to populate with sample data?

```bash
cd backend
python manage.py shell

# Then run:
from apps.users.models import User
from apps.properties.models import Property

# Create sample host
host = User.objects.create_user(
    email='host@example.com',
    password='password123',
    first_name='John',
    last_name='Doe',
    role='host'
)

# Create sample property
Property.objects.create(
    host=host,
    name='Beautiful Beach House',
    description='Amazing ocean view property',
    location='Miami, USA',
    pricepernight=200,
    bedrooms=3,
    bathrooms=2,
    max_guests=6,
    amenities='WiFi, Pool, Beach Access'
)
```

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [database-script-0x01/schema.sql](database-script-0x01/schema.sql) for database schema
- Explore the API at http://localhost:8000/swagger/

## Need Help?

- Check the main README.md
- Review API documentation
- Open an issue on GitHub

Happy coding! 🚀
