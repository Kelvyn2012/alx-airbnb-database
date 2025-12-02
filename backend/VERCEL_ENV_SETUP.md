# Vercel Environment Variables Setup

This is a quick reference for setting up environment variables in Vercel for your backend deployment.

## How to Add Environment Variables in Vercel

1. Go to your Vercel project dashboard
2. Click on **Settings** tab
3. Navigate to **Environment Variables** section
4. Add each variable below

## Required Environment Variables

Copy and paste these into Vercel (update the values):

### Database Configuration
```
DATABASE_URL
```
Value: Get from Neon dashboard (e.g., `postgres://user:pass@host.neon.tech/db?sslmode=require`)

### Django Core Settings
```
SECRET_KEY
```
Value: Your Django secret key from local .env

```
DEBUG
```
Value: `False`

```
ALLOWED_HOSTS
```
Value: `.vercel.app,.neon.tech,your-custom-domain.com`

### CORS Configuration
```
CORS_ALLOWED_ORIGINS
```
Value: `https://your-frontend.vercel.app,http://localhost:3000`
(Update after you deploy your frontend)

## Optional Environment Variables

### Payment Integration (Stripe)
```
STRIPE_PUBLIC_KEY
```
Value: Your Stripe publishable key

```
STRIPE_SECRET_KEY
```
Value: Your Stripe secret key

### OAuth - Google
```
GOOGLE_OAUTH2_CLIENT_ID
```
Value: Your Google OAuth client ID

```
GOOGLE_OAUTH2_CLIENT_SECRET
```
Value: Your Google OAuth client secret

### OAuth - Facebook
```
FACEBOOK_APP_ID
```
Value: Your Facebook app ID

```
FACEBOOK_APP_SECRET
```
Value: Your Facebook app secret

## Environment Scopes

For each variable, select the appropriate scope:
- ✅ **Production** - Always select this
- ✅ **Preview** - Select for testing branches
- ⬜ **Development** - Usually not needed

## After Adding Variables

1. Click **Save**
2. Go to **Deployments** tab
3. Click the **⋮** menu on the latest deployment
4. Select **Redeploy**

This ensures your app picks up the new environment variables.

## Verification

After deployment, you can verify environment variables are loaded:
- Check Vercel Function Logs for any environment variable errors
- Test API endpoints to ensure database connectivity
- Verify CORS by testing frontend-backend communication

## Security Best Practices

- ✅ Never commit `.env` files to Git
- ✅ Use different `SECRET_KEY` for production vs development
- ✅ Set `DEBUG=False` in production
- ✅ Rotate secrets regularly
- ✅ Use strong, random values for secret keys
- ✅ Limit `ALLOWED_HOSTS` to your actual domains

## Generating a New Django Secret Key

If you need a new secret key for production:

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

**Note**: Changes to environment variables require redeploying your application to take effect.
