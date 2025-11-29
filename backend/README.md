# Airbnb Clone - Full Stack Application

A full-featured Airbnb clone with Django REST Framework backend and React frontend, featuring property listings, bookings, reviews, real-time messaging, and OAuth authentication.

## Features

### Core Features
- **User Authentication**: JWT-based authentication with OAuth (Google & Facebook)
- **Property Management**: Create, read, update, and delete property listings
- **Booking System**: Complete booking flow with availability checking
- **Reviews & Ratings**: Property reviews with star ratings
- **Real-time Messaging**: WebSocket-based chat between hosts and guests
- **Payment Integration**: Stripe payment processing
- **Dark Mode**: Beautiful dark/light theme toggle
- **Responsive Design**: Mobile-friendly UI

### User Roles
- **Guest**: Browse and book properties, write reviews
- **Host**: List properties, manage bookings, respond to messages
- **Admin**: Full administrative access

## Tech Stack

### Backend
- Django 5.2.8
- Django REST Framework 3.14.0
- Django Channels (WebSocket support)
- PostgreSQL/MySQL
- JWT Authentication
- Redis (for WebSocket support)
- Stripe API

### Frontend
- React 18
- React Router v6
- Axios
- Context API (State Management)
- CSS3 with animations

## Project Structure

```
alx-airbnb-database/
├── backend/
│   ├── airbnb_project/          # Project settings
│   ├── apps/
│   │   ├── users/               # User authentication & profiles
│   │   ├── properties/          # Property listings
│   │   ├── bookings/            # Booking management
│   │   ├── reviews/             # Reviews & ratings
│   │   ├── payments/            # Payment processing
│   │   └── messages/            # Real-time messaging
│   ├── manage.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/          # Reusable components
│   │   ├── pages/               # Page components
│   │   ├── context/             # Context providers
│   │   ├── services/            # API services
│   │   └── styles/              # CSS files
│   └── package.json
├── database-schema-diagrams/    # ER diagrams
├── normalization.md
└── README.md
```

## Installation & Setup

### Prerequisites
- Python 3.13+
- Node.js 18+
- PostgreSQL or MySQL
- Redis (for WebSocket support)

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver 8001
   ```

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Configure environment variables**
   ```bash
   # Create .env file with:
   REACT_APP_API_URL=http://localhost:8001
   ```

4. **Run development server**
   ```bash
   PORT=3001 npm start
   ```

## Environment Variables

### Backend (.env)
```env
# Database
DATABASE_NAME=airbnb_db
DATABASE_USER=your_user
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# JWT
JWT_SECRET_KEY=your-jwt-secret-key

# OAuth
GOOGLE_OAUTH2_CLIENT_ID=your_google_client_id
GOOGLE_OAUTH2_CLIENT_SECRET=your_google_client_secret
FACEBOOK_APP_ID=your_facebook_app_id
FACEBOOK_APP_SECRET=your_facebook_app_secret

# Stripe
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key

# Redis
REDIS_URL=redis://localhost:6379
```

### Frontend (.env)
```env
REACT_APP_API_URL=http://localhost:8001
```

## API Documentation

The API documentation is available at:
- Swagger UI: `http://localhost:8001/swagger/`
- ReDoc: `http://localhost:8001/redoc/`

### Main Endpoints

#### Authentication
- `POST /api/users/register/` - User registration
- `POST /api/users/login/` - User login
- `GET /api/users/auth/google/` - Google OAuth
- `GET /api/users/auth/facebook/` - Facebook OAuth

#### Properties
- `GET /api/properties/` - List all properties
- `POST /api/properties/` - Create property (host only)
- `GET /api/properties/{id}/` - Get property details
- `PUT /api/properties/{id}/` - Update property (host only)
- `DELETE /api/properties/{id}/` - Delete property (host only)

#### Bookings
- `GET /api/bookings/` - List user bookings
- `POST /api/bookings/` - Create booking
- `GET /api/bookings/{id}/` - Get booking details
- `PATCH /api/bookings/{id}/` - Update booking status

#### Reviews
- `GET /api/reviews/property/{id}/` - Get property reviews
- `POST /api/reviews/` - Create review
- `PUT /api/reviews/{id}/` - Update review
- `DELETE /api/reviews/{id}/` - Delete review

#### Payments
- `POST /api/payments/create-payment-intent/` - Create Stripe payment
- `GET /api/payments/booking/{id}/` - Get payment details

## OAuth Setup

See [OAUTH_SETUP.md](OAUTH_SETUP.md) for detailed instructions on setting up Google and Facebook OAuth.

## Database Schema

The database follows a normalized structure with the following main entities:
- Users (with roles: guest, host, admin)
- Properties
- Bookings
- Reviews
- Payments
- Messages

See [normalization.md](normalization.md) for detailed normalization documentation.

## Features in Detail

### Dark Mode
- Toggle between light and dark themes
- Persistent theme preference (localStorage)
- Smooth transitions across all components

### OAuth Authentication
- Google Sign In
- Facebook Sign In
- Automatic JWT token generation
- Seamless integration with existing auth system

### Real-time Messaging
- WebSocket-based chat
- Instant message delivery
- Online/offline status
- Message history

### Property Search & Filters
- Search by location
- Filter by bedrooms, bathrooms
- Sort by price, rating
- Pagination support

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

### Backend (Django)
1. Set `DEBUG=False` in production
2. Configure proper `ALLOWED_HOSTS`
3. Use PostgreSQL in production
4. Set up Redis for channels
5. Configure HTTPS
6. Use gunicorn/uvicorn for ASGI support

### Frontend (React)
1. Build production bundle: `npm run build`
2. Deploy to static hosting (Netlify, Vercel, S3)
3. Configure environment variables

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

## License

This project is for educational purposes as part of the ALX Backend Specialization program.

## Support

For issues and questions, please open an issue on GitHub.

## Acknowledgments

- ALX Africa for the project requirements
- Django and React communities
- All contributors
