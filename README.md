# Airbnb Clone - Full Stack Application

A full-featured Airbnb clone built with Django REST Framework backend and React frontend, featuring property listings, bookings, reviews, payments, and real-time messaging.

## Features

### Backend (Django REST Framework)
- **User Authentication**: JWT-based authentication with role management (Guest, Host, Admin)
- **Property Management**: CRUD operations for properties with image uploads
- **Booking System**: Property booking with availability checking and validation
- **Payment Integration**: Payment processing endpoints (Stripe-ready)
- **Review System**: Users can rate and review properties
- **Messaging System**: Real-time messaging between users using Django Channels
- **Admin Panel**: Comprehensive Django admin interface
- **API Documentation**: Swagger/ReDoc API documentation

### Frontend (React)
- **User Authentication**: Login, registration, and profile management
- **Property Browsing**: Search, filter, and view properties
- **Booking Management**: Create and manage bookings with calendar interface
- **Host Dashboard**: Property management and booking overview for hosts
- **Reviews**: Read and write property reviews
- **Messaging**: Real-time chat interface
- **Responsive Design**: Mobile-friendly UI

## Technology Stack

### Backend
- Python 3.8+
- Django 4.2
- Django REST Framework
- PostgreSQL
- Django Channels (WebSockets)
- Redis (for channels)
- JWT Authentication

### Frontend
- React 18
- React Router
- Axios
- CSS3

## Project Structure

```
alx-airbnb-database/
├── backend/
│   ├── airbnb_project/          # Django project settings
│   ├── apps/
│   │   ├── users/               # User management
│   │   ├── properties/          # Property listings
│   │   ├── bookings/            # Booking system
│   │   ├── payments/            # Payment processing
│   │   ├── reviews/             # Review system
│   │   └── messages/            # Messaging system
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/          # Reusable components
│   │   ├── pages/               # Page components
│   │   ├── context/             # React context
│   │   ├── services/            # API services
│   │   └── styles/              # CSS files
│   └── package.json
├── database-script-0x01/        # Database schema
├── database-script-0x02/        # Seed data
└── README.md
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Node.js 14 or higher
- PostgreSQL 12 or higher
- Redis (for real-time messaging)

### Backend Setup

1. **Navigate to the backend directory**
```bash
cd backend
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up PostgreSQL database**
```bash
# Create database
createdb airbnb_db

# Or using psql
psql -U postgres
CREATE DATABASE airbnb_db;
\q
```

5. **Configure environment variables**
```bash
cp .env.example .env
```

Edit `.env` with your settings:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=airbnb_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

STRIPE_PUBLIC_KEY=your-stripe-public-key
STRIPE_SECRET_KEY=your-stripe-secret-key
```

6. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Create a superuser**
```bash
python manage.py createsuperuser
```

8. **Start the development server**
```bash
python manage.py runserver
```

The backend API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to the frontend directory**
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Create environment file**
```bash
# Create .env file in frontend directory
echo "REACT_APP_API_URL=http://localhost:8000" > .env
```

4. **Start the development server**
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

### Redis Setup (for real-time messaging)

**On macOS:**
```bash
brew install redis
brew services start redis
```

**On Ubuntu/Debian:**
```bash
sudo apt-get install redis-server
sudo systemctl start redis
```

**On Windows:**
Download from https://redis.io/download

## API Endpoints

### Authentication
- `POST /api/users/register/` - Register new user
- `POST /api/users/login/` - Login user
- `POST /api/users/token/refresh/` - Refresh JWT token
- `GET /api/users/profile/` - Get current user profile
- `PATCH /api/users/profile/` - Update user profile

### Properties
- `GET /api/properties/` - List all properties
- `POST /api/properties/create/` - Create new property (Host only)
- `GET /api/properties/<id>/` - Get property details
- `PATCH /api/properties/<id>/` - Update property (Host only)
- `DELETE /api/properties/<id>/` - Delete property (Host only)
- `GET /api/properties/my-properties/` - Get user's properties
- `POST /api/properties/<id>/images/` - Upload property images

### Bookings
- `GET /api/bookings/` - List user's bookings
- `POST /api/bookings/create/` - Create new booking
- `GET /api/bookings/<id>/` - Get booking details
- `PATCH /api/bookings/<id>/` - Update booking status
- `GET /api/bookings/host/` - List host's property bookings

### Payments
- `GET /api/payments/` - List user's payments
- `POST /api/payments/create/` - Process payment
- `GET /api/payments/<id>/` - Get payment details

### Reviews
- `GET /api/reviews/property/<property_id>/` - List property reviews
- `POST /api/reviews/create/` - Create review
- `GET /api/reviews/<id>/` - Get review details
- `PATCH /api/reviews/<id>/` - Update review
- `DELETE /api/reviews/<id>/` - Delete review

### Messages
- `GET /api/messages/` - List user's messages
- `POST /api/messages/create/` - Send message
- `GET /api/messages/conversation/<user_id>/` - Get conversation with user

## API Documentation

Once the backend is running, visit:
- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

## Admin Panel

Access the Django admin panel at `http://localhost:8000/admin/`

Use the superuser credentials you created during setup.

## Database Schema

The application uses the following main models:

- **User**: Custom user model with roles (guest, host, admin)
- **Property**: Property listings with details and pricing
- **PropertyImage**: Property images (multiple per property)
- **Booking**: Property bookings with dates and status
- **Payment**: Payment records for bookings
- **Review**: Property reviews with ratings
- **Message**: Direct messages between users

See [database-script-0x01/schema.sql](database-script-0x01/schema.sql) for the complete schema.

## Running with Docker (Optional)

Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: airbnb_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:6
    ports:
      - "6379:6379"

  backend:
    build: ./backend
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis

  frontend:
    build: ./frontend
    command: npm start
    volumes:
      - ./frontend:/app
    ports:
      - "3000:3000"
    depends_on:
      - backend

volumes:
  postgres_data:
```

Run with:
```bash
docker-compose up
```

## Testing

### Backend Tests
```bash
cd backend
python manage.py test
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Deployment

### Backend Deployment (Heroku Example)

1. Install Heroku CLI
2. Create Heroku app
```bash
heroku create your-app-name
```

3. Add PostgreSQL addon
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

4. Set environment variables
```bash
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
```

5. Deploy
```bash
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Frontend Deployment (Netlify/Vercel)

1. Build the frontend
```bash
cd frontend
npm run build
```

2. Deploy the `build` folder to your hosting service

## User Roles

- **Guest**: Can browse properties, make bookings, write reviews, send messages
- **Host**: All guest permissions + create/manage properties, manage bookings
- **Admin**: Full access to all features and admin panel

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Support

For issues and questions, please open an issue on the GitHub repository.

## Acknowledgments

- Built as part of the ALX Software Engineering Program
- Database design based on Airbnb's core functionality
- UI/UX inspired by modern booking platforms
