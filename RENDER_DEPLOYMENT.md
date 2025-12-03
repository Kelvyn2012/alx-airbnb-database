# Render Deployment Guide for Airbnb Clone

This guide will walk you through deploying your fullstack Airbnb clone application to Render.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Quick Deploy (Automated)](#quick-deploy-automated)
3. [Manual Deployment](#manual-deployment)
4. [Environment Variables](#environment-variables)
5. [Post-Deployment](#post-deployment)
6. [Troubleshooting](#troubleshooting)

## Prerequisites

Before deploying, ensure you have:

- [ ] A [Render account](https://render.com) (free tier available)
- [ ] Your code pushed to a GitHub/GitLab/Bitbucket repository
- [ ] PostgreSQL database credentials (Render provides free PostgreSQL)
- [ ] Stripe API keys (for payments)
- [ ] OAuth credentials (Google, Facebook - optional)

## Quick Deploy (Automated)

### Option 1: Blueprint Deployment (Recommended)

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

2. **Deploy using Render Blueprint**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click **"New"** → **"Blueprint"**
   - Connect your repository
   - Render will automatically detect the `render.yaml` file
   - Review the services to be created:
     - Backend Web Service
     - Frontend Static Site
     - PostgreSQL Database
   - Click **"Apply"**

3. **Configure Environment Variables** (see section below)

## Manual Deployment

### Step 1: Deploy PostgreSQL Database

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New"** → **"PostgreSQL"**
3. Configure:
   - **Name**: `airbnb-postgres`
   - **Database**: `airbnb_db`
   - **User**: `airbnb_user`
   - **Region**: Choose closest to you
   - **Plan**: Free
4. Click **"Create Database"**
5. **Save the Internal Database URL** (you'll need this for the backend)

### Step 2: Deploy Backend API

1. Click **"New"** → **"Web Service"**
2. Connect your repository
3. Configure:
   - **Name**: `airbnb-backend`
   - **Region**: Same as database
   - **Branch**: `main`
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn airbnb_project.wsgi:application`
   - **Plan**: Free

4. **Add Environment Variables** (click "Advanced"):
   ```
   PYTHON_VERSION=3.12.0
   SECRET_KEY=<generate-a-secure-random-key>
   DEBUG=False
   DATABASE_URL=<paste-internal-database-url>
   ALLOWED_HOSTS=<your-backend-url>.onrender.com
   CORS_ALLOWED_ORIGINS=https://<your-frontend-url>.onrender.com
   STRIPE_PUBLIC_KEY=<your-stripe-public-key>
   STRIPE_SECRET_KEY=<your-stripe-secret-key>
   GOOGLE_OAUTH2_CLIENT_ID=<your-google-client-id>
   GOOGLE_OAUTH2_CLIENT_SECRET=<your-google-secret>
   FACEBOOK_APP_ID=<your-facebook-app-id>
   FACEBOOK_APP_SECRET=<your-facebook-secret>
   ```

5. Click **"Create Web Service"**

### Step 3: Deploy Frontend

1. Click **"New"** → **"Static Site"**
2. Connect your repository
3. Configure:
   - **Name**: `airbnb-frontend`
   - **Branch**: `main`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: `build`

4. **Add Environment Variable**:
   ```
   REACT_APP_API_URL=https://<your-backend-url>.onrender.com
   ```

5. Click **"Create Static Site"**

## Environment Variables

### Backend Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Generate using: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` |
| `DEBUG` | Debug mode | `False` (production) |
| `DATABASE_URL` | PostgreSQL connection string | Provided by Render database |
| `ALLOWED_HOSTS` | Allowed host domains | `your-app.onrender.com` |
| `CORS_ALLOWED_ORIGINS` | Frontend URLs for CORS | `https://your-frontend.onrender.com` |

### Backend Optional Variables

| Variable | Description |
|----------|-------------|
| `STRIPE_PUBLIC_KEY` | Stripe public API key |
| `STRIPE_SECRET_KEY` | Stripe secret API key |
| `GOOGLE_OAUTH2_CLIENT_ID` | Google OAuth client ID |
| `GOOGLE_OAUTH2_CLIENT_SECRET` | Google OAuth secret |
| `FACEBOOK_APP_ID` | Facebook app ID |
| `FACEBOOK_APP_SECRET` | Facebook app secret |
| `REDIS_URL` | Redis URL for WebSocket (paid plans only) |

### Frontend Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `REACT_APP_API_URL` | Backend API URL | `https://your-backend.onrender.com` |

## Post-Deployment

### 1. Create Superuser (Admin)

After the backend is deployed, create an admin user:

1. Go to your backend service in Render Dashboard
2. Click **"Shell"** (in the top right)
3. Run:
   ```bash
   python manage.py createsuperuser
   ```
4. Follow the prompts to create your admin account

### 2. Verify Deployment

Test your deployment:

1. **Backend Health Check**:
   - Visit: `https://your-backend.onrender.com/admin/`
   - You should see the Django admin login page

2. **API Endpoints**:
   - Visit: `https://your-backend.onrender.com/api/properties/`
   - Should return JSON data or empty list

3. **Frontend**:
   - Visit: `https://your-frontend.onrender.com`
   - Should load your React application

### 3. Update OAuth Redirect URIs

If using Google/Facebook OAuth, update your redirect URIs:

**Google OAuth**:
- Go to [Google Cloud Console](https://console.cloud.google.com)
- Add authorized redirect URI: `https://your-backend.onrender.com/api/auth/google/callback/`

**Facebook OAuth**:
- Go to [Facebook Developers](https://developers.facebook.com)
- Add OAuth redirect URI: `https://your-backend.onrender.com/api/auth/facebook/callback/`

## Troubleshooting

### Build Fails

**Issue**: Build command fails during deployment

**Solutions**:
1. Check that `build.sh` is executable:
   ```bash
   chmod +x backend/build.sh
   git add backend/build.sh
   git commit -m "Make build.sh executable"
   git push
   ```

2. Check Python version in `runtime.txt`:
   ```
   python-3.12
   ```

3. Verify all dependencies are in `requirements.txt`

### Database Connection Error

**Issue**: Backend can't connect to database

**Solutions**:
1. Verify `DATABASE_URL` environment variable is set correctly
2. Use the **Internal Database URL** from Render (not External)
3. Check that database is in the same region as backend

### Static Files Not Loading

**Issue**: CSS/JS files return 404

**Solutions**:
1. Verify `STATIC_ROOT` in settings.py:
   ```python
   STATIC_ROOT = BASE_DIR / 'staticfiles'
   ```

2. Check that `whitenoise` is in middleware:
   ```python
   MIDDLEWARE = [
       'django.middleware.security.SecurityMiddleware',
       'whitenoise.middleware.WhiteNoiseMiddleware',  # Must be here
       ...
   ]
   ```

3. Rebuild with:
   ```bash
   python manage.py collectstatic --no-input
   ```

### CORS Errors

**Issue**: Frontend can't connect to backend (CORS error in console)

**Solutions**:
1. Update `CORS_ALLOWED_ORIGINS` in backend settings:
   ```
   CORS_ALLOWED_ORIGINS=https://your-frontend.onrender.com
   ```

2. Verify frontend is using correct API URL:
   ```
   REACT_APP_API_URL=https://your-backend.onrender.com
   ```

3. Rebuild frontend after changing environment variables

### Free Tier Limitations

**Render Free Tier**:
- Services spin down after 15 minutes of inactivity
- First request after spin-down may take 30-60 seconds
- Database: 90 days of inactivity deletion
- Redis: Not available on free tier (WebSocket features won't work)

**Solutions**:
- Use [UptimeRobot](https://uptimerobot.com) to ping your app every 14 minutes
- Upgrade to paid plan for always-on services
- For Redis, use external service like [Redis Labs](https://redis.com) or [Upstash](https://upstash.com)

### Logs and Debugging

**View Logs**:
1. Go to your service in Render Dashboard
2. Click **"Logs"** tab
3. Filter by severity level

**Common Log Issues**:
- `SECRET_KEY` not set: Add to environment variables
- `ALLOWED_HOSTS` error: Add your `.onrender.com` domain
- Migration errors: Run migrations manually in Shell

## Environment Setup Checklist

Before going live, ensure:

- [ ] All environment variables are set
- [ ] `DEBUG=False` in production
- [ ] Database migrations are applied
- [ ] Superuser account is created
- [ ] Static files are collected
- [ ] CORS origins include your frontend URL
- [ ] OAuth redirect URIs are updated
- [ ] Stripe webhooks are configured (if applicable)
- [ ] SSL certificates are active (Render provides free SSL)

## Performance Optimization

### Backend Optimization
1. Enable database connection pooling (already configured)
2. Use `gunicorn` workers:
   ```
   gunicorn airbnb_project.wsgi:application --workers 2
   ```
3. Enable Django caching in settings.py

### Frontend Optimization
1. Build with production optimizations (already enabled)
2. Use CDN for static assets
3. Enable gzip compression (Render does this automatically)

## Scaling

### Upgrade Plans
- **Starter Plan** ($7/month): 512MB RAM, always on
- **Standard Plan** ($25/month): 2GB RAM, better performance
- **Professional Plans**: Higher resources and features

### Horizontal Scaling
- Add more web service instances
- Use Render's load balancer
- Scale database vertically for more connections

## Additional Resources

- [Render Documentation](https://render.com/docs)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [React Deployment Best Practices](https://create-react-app.dev/docs/deployment/)
- [PostgreSQL on Render](https://render.com/docs/databases)

## Support

If you encounter issues:
1. Check [Render Status Page](https://status.render.com)
2. Review [Render Community Forum](https://community.render.com)
3. Contact [Render Support](https://render.com/support)

---

**Last Updated**: December 2025

**Need Help?** Open an issue in your repository or check the existing deployment documentation files.
