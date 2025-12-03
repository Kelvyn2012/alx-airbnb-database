# Project Dependencies

Complete list of dependencies for the Airbnb Clone Backend API.

## Summary

- **Total Packages:** 43
- **Python Version:** 3.12+
- **Django Version:** 5.2.8
- **Last Updated:** December 3, 2025

---

## Core Framework (4 packages)

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 5.2.8 | Core web framework |
| djangorestframework | 3.14.0 | RESTful API framework |
| django-cors-headers | 4.3.0 | Handle Cross-Origin Resource Sharing |
| django-filter | 23.3 | Advanced filtering for APIs |

---

## Authentication & Security (9 packages)

| Package | Version | Purpose |
|---------|---------|---------|
| djangorestframework-simplejwt | 5.3.0 | JWT authentication for DRF |
| PyJWT | 2.10.1 | JSON Web Token implementation |
| django-allauth | 65.13.1 | Authentication, registration, account management |
| social-auth-app-django | 5.6.0 | Social authentication integration |
| social-auth-core | 4.8.1 | Core social auth functionality |
| oauthlib | 3.3.1 | OAuth 1.0 and 2.0 implementation |
| requests-oauthlib | 2.0.0 | OAuth support for requests |
| python3-openid | 3.2.0 | OpenID support |
| cryptography | 46.0.3 | Cryptographic operations |

**Features:**
- JWT token-based authentication
- Google OAuth2 integration
- Facebook OAuth2 integration
- User registration and login
- Token refresh mechanism

---

## Database (2 packages)

| Package | Version | Purpose |
|---------|---------|---------|
| psycopg2-binary | 2.9.9 | PostgreSQL database adapter |
| dj-database-url | 2.1.0 | Database URL parsing |

**Database Support:**
- PostgreSQL (primary)
- Neon serverless PostgreSQL (production)
- Local PostgreSQL (development)

---

## Real-time Features (3 packages)

| Package | Version | Purpose |
|---------|---------|---------|
| channels | 4.0.0 | WebSocket and async support |
| channels-redis | 4.1.0 | Redis backend for Channels |
| redis | 7.1.0 | Redis client |

**Features:**
- Real-time messaging between users
- WebSocket connections
- Async task handling

---

## Static & Media Files (2 packages)

| Package | Version | Purpose |
|---------|---------|---------|
| whitenoise | 6.6.0 | Serve static files efficiently |
| pillow | 12.0.0 | Image processing and handling |

**Features:**
- Compressed static file serving
- Property image uploads
- Profile picture handling
- Image optimization

---

## API Services (2 packages)

| Package | Version | Purpose |
|---------|---------|---------|
| drf-yasg | 1.21.7 | Swagger/OpenAPI documentation |
| stripe | 7.4.0 | Payment processing |

**Features:**
- Interactive API documentation (Swagger UI)
- ReDoc documentation
- Stripe payment integration
- Payment tracking and management

---

## HTTP & Networking (5 packages)

| Package | Version | Purpose |
|---------|---------|---------|
| requests | 2.32.5 | HTTP library |
| urllib3 | 2.5.0 | HTTP client |
| certifi | 2025.11.12 | SSL certificates |
| charset-normalizer | 3.4.4 | Character encoding detection |
| idna | 3.11 | Internationalized domain names |

---

## Data Processing (4 packages)

| Package | Version | Purpose |
|---------|---------|---------|
| PyYAML | 6.0.3 | YAML parser |
| msgpack | 1.1.2 | MessagePack serialization |
| inflection | 0.5.1 | String transformations |
| pytz | 2025.2 | Timezone handling |

---

## Security & Parsing (2 packages)

| Package | Version | Purpose |
|---------|---------|---------|
| defusedxml | 0.7.1 | Secure XML parsing |
| sqlparse | 0.5.4 | SQL statement parsing |

---

## Configuration (1 package)

| Package | Version | Purpose |
|---------|---------|---------|
| python-decouple | 3.8 | Environment variable management |

---

## Core Dependencies (7 packages)

| Package | Version | Purpose |
|---------|---------|---------|
| asgiref | 3.11.0 | ASGI specification |
| cffi | 2.0.0 | C Foreign Function Interface |
| pycparser | 2.23 | C parser |
| packaging | 25.0 | Package version handling |
| typing_extensions | 4.15.0 | Backported typing features |
| uritemplate | 4.2.0 | URI template parsing |
| setuptools | 80.9.0 | Package installation |
| wheel | 0.45.1 | Built package format |

---

## Installation

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```cmd
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
pip check
```

Expected output: `No broken requirements found.`

---

## Environment Variables

Required environment variables for the application:

### Development

```env
# Django
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=airbnb_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3001
```

### Production

```env
# Django
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,.vercel.app

# Database (Neon)
DATABASE_URL=postgresql://user:password@host:5432/database

# Stripe
STRIPE_PUBLIC_KEY=pk_live_...
STRIPE_SECRET_KEY=sk_live_...

# OAuth
GOOGLE_OAUTH2_CLIENT_ID=your-google-client-id
GOOGLE_OAUTH2_CLIENT_SECRET=your-google-secret
FACEBOOK_APP_ID=your-facebook-app-id
FACEBOOK_APP_SECRET=your-facebook-secret
```

---

## Dependency Updates

### Check for Updates

```bash
pip list --outdated
```

### Update a Package

```bash
pip install --upgrade package-name
```

### Update All Packages

```bash
pip install --upgrade -r requirements.txt
```

### Freeze Updated Dependencies

```bash
pip freeze > requirements.txt
```

---

## Troubleshooting

### Common Issues

#### 1. psycopg2 Installation Error

**macOS:**
```bash
brew install postgresql
pip install psycopg2-binary
```

**Ubuntu/Debian:**
```bash
sudo apt-get install libpq-dev python3-dev
pip install psycopg2-binary
```

#### 2. Pillow Installation Error

**macOS:**
```bash
brew install libjpeg
pip install pillow
```

**Ubuntu/Debian:**
```bash
sudo apt-get install libjpeg-dev zlib1g-dev
pip install pillow
```

#### 3. Redis Connection Error

Ensure Redis is running:

**macOS:**
```bash
brew services start redis
```

**Ubuntu/Debian:**
```bash
sudo systemctl start redis
```

---

## Security Considerations

### Package Security

Run security checks regularly:

```bash
pip install safety
safety check
```

### Keeping Dependencies Updated

- Review security advisories: https://pypi.org/project/django/
- Subscribe to Django security mailing list
- Use Dependabot or similar tools for automated updates

---

## Production Deployment

### Required Packages for Production

All packages in requirements.txt are needed for production except:
- `wheel` (build-time only)
- `setuptools` (build-time only)

### Performance Optimization

1. **Use Production WSGI Server:**
   ```bash
   pip install gunicorn
   gunicorn airbnb_project.wsgi:application
   ```

2. **Enable Caching:**
   - Redis for session storage
   - Redis for cache backend
   - WhiteNoise for static files

3. **Database Connection Pooling:**
   - Already configured with `conn_max_age=600`
   - Uses `conn_health_checks=True`

---

## License Compatibility

All dependencies are compatible with commercial use:
- Django: BSD License
- DRF: BSD License
- Most packages: MIT or BSD License

Review individual package licenses: https://pypi.org/

---

## Support

For dependency-related issues:
1. Check package documentation
2. Search GitHub issues for the package
3. Consult Django/DRF documentation
4. Ask in Django community forums

---

**Last Updated:** December 3, 2025
**Maintained By:** Development Team
**Status:** ✓ Production Ready
