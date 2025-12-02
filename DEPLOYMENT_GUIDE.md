# Deployment Guide: Vercel + Neon

This guide walks you through deploying your Airbnb backend to Vercel and connecting it to a Neon PostgreSQL database.

## Prerequisites

- GitHub account
- Vercel account (sign up at https://vercel.com)
- Neon account (sign up at https://neon.tech)

## Part 1: Set Up Neon PostgreSQL Database

### Step 1: Create a Neon Project

1. Go to https://neon.tech and sign in
2. Click "Create Project"
3. Choose a name (e.g., "airbnb-backend")
4. Select a region close to your users
5. Click "Create Project"

### Step 2: Get Database Connection String

1. In your Neon dashboard, go to your project
2. Click on "Connection Details"
3. Copy the connection string - it looks like:
   ```
   postgres://username:password@ep-xxx-xxx.region.aws.neon.tech/dbname?sslmode=require
   ```
4. Save this for later - you'll need it for Vercel environment variables

### Step 3: Run Migrations (One-time setup)

Update your local `.env` file temporarily with the Neon DATABASE_URL:

```bash
cd backend
echo "DATABASE_URL=your-neon-connection-string" >> .env
source venv/bin/activate
python3.12 manage.py migrate
```

After migrations complete, you can remove the DATABASE_URL from your local .env if you want to continue using local PostgreSQL for development.

## Part 2: Deploy Backend to Vercel

### Step 1: Prepare Your Repository

1. Make sure all changes are committed:
   ```bash
   git add .
   git commit -m "Prepare backend for Vercel deployment"
   git push origin main
   ```

### Step 2: Deploy to Vercel

1. Go to https://vercel.com/dashboard
2. Click "Add New" → "Project"
3. Import your GitHub repository
4. Configure the project:
   - **Framework Preset**: Other
   - **Root Directory**: `backend`
   - **Build Command**: `bash build_files.sh`
   - **Output Directory**: `staticfiles`

### Step 3: Set Environment Variables

In Vercel project settings, add these environment variables:

```
SECRET_KEY=your-secret-key-from-django
DEBUG=False
DATABASE_URL=your-neon-connection-string-from-step-1
ALLOWED_HOSTS=.vercel.app,.neon.tech
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://your-frontend.vercel.app
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
GOOGLE_OAUTH2_CLIENT_ID=your_google_client_id
GOOGLE_OAUTH2_CLIENT_SECRET=your_google_client_secret
FACEBOOK_APP_ID=your_facebook_app_id
FACEBOOK_APP_SECRET=your_facebook_app_secret
```

### Step 4: Deploy

Click "Deploy" and wait for the build to complete.

## Part 3: Deploy Frontend to Vercel

### Step 1: Update Frontend API URLs

1. In your frontend code, update the API base URL to point to your deployed backend:
   ```javascript
   const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'https://your-backend.vercel.app';
   ```

2. Create a `.env.local` file in your frontend:
   ```
   NEXT_PUBLIC_API_URL=https://your-backend.vercel.app
   ```

### Step 2: Deploy Frontend

1. Go to Vercel dashboard
2. Click "Add New" → "Project"
3. Import your repository again
4. Configure:
   - **Framework Preset**: Next.js (or your framework)
   - **Root Directory**: `frontend`
   - **Build Command**: Auto-detected
   - **Output Directory**: Auto-detected

### Step 3: Set Frontend Environment Variables

Add in Vercel:
```
NEXT_PUBLIC_API_URL=https://your-backend.vercel.app
```

## Part 4: Update CORS Settings

After both are deployed:

1. Get your frontend Vercel URL (e.g., `https://your-app.vercel.app`)
2. Update the `CORS_ALLOWED_ORIGINS` environment variable in your backend Vercel project:
   ```
   CORS_ALLOWED_ORIGINS=https://your-app.vercel.app,http://localhost:3000
   ```
3. Redeploy the backend

## Part 5: Post-Deployment Tasks

### Create a Superuser (Admin)

You can create a superuser using Vercel CLI:

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Login:
   ```bash
   vercel login
   ```

3. Create superuser (you'll need to use a custom management command or do this via shell):
   ```bash
   vercel env pull
   # Then run migrations and createsuperuser locally with production DATABASE_URL
   ```

Alternatively, create an admin user via Django admin after deployment.

## Testing Your Deployment

1. Test backend health:
   ```
   https://your-backend.vercel.app/admin/
   ```

2. Test API endpoints:
   ```
   https://your-backend.vercel.app/api/
   ```

3. Test frontend:
   ```
   https://your-frontend.vercel.app
   ```

## Troubleshooting

### Common Issues

1. **500 Error**: Check Vercel logs for details
   - Go to your project → Deployments → Click on deployment → View Function Logs

2. **Database Connection Error**:
   - Verify DATABASE_URL is correct in Vercel env vars
   - Make sure it includes `?sslmode=require`

3. **Static Files Not Loading**:
   - Run `python3.12 manage.py collectstatic` locally to test
   - Check WhiteNoise is in MIDDLEWARE in settings.py

4. **CORS Errors**:
   - Update CORS_ALLOWED_ORIGINS with your actual frontend URL
   - Make sure to redeploy backend after updating env vars

## Important Notes

- **Static Files**: Handled by WhiteNoise
- **Media Files**: For production, consider using AWS S3 or Cloudinary
- **WebSockets**: Vercel Serverless functions don't support WebSockets. For real-time features (Django Channels), consider deploying to Railway, Render, or AWS
- **Database Backups**: Neon provides automatic backups
- **Monitoring**: Use Vercel Analytics and Neon monitoring dashboards

## Environment Variables Reference

### Required for Backend:
- `SECRET_KEY` - Django secret key
- `DATABASE_URL` - Neon PostgreSQL connection string
- `DEBUG` - Should be `False` in production
- `ALLOWED_HOSTS` - `.vercel.app,.neon.tech`
- `CORS_ALLOWED_ORIGINS` - Your frontend URL

### Optional:
- `STRIPE_PUBLIC_KEY` / `STRIPE_SECRET_KEY` - For payments
- OAuth credentials - For social authentication
- Email settings - For email functionality

## Continuous Deployment

Vercel automatically deploys when you push to your main branch. To deploy:

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

Vercel will automatically detect changes and redeploy both frontend and backend.

## Cost Considerations

- **Vercel**: Free tier includes hobby projects
- **Neon**: Free tier includes 0.5GB storage and 3GB data transfer
- Monitor usage in both dashboards

## Need Help?

- Vercel Docs: https://vercel.com/docs
- Neon Docs: https://neon.tech/docs
- Django Deployment: https://docs.djangoproject.com/en/stable/howto/deployment/

---

Last updated: December 2025
