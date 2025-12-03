# Render Deployment Quick Fix Guide

## Issues Fixed

### 1. Python Version Issue ✅
**Error:** `ImportError: undefined symbol: _PyInterpreterState_Get`

**Fix Applied:**
- Updated [backend/runtime.txt](backend/runtime.txt) to `python-3.12.0`
- Created [backend/.python-version](backend/.python-version) with `3.12.0`
- Created [.python-version](.python-version) with `3.12.0`
- Updated [render.yaml](render.yaml) with `PYTHON_VERSION=3.12.0`

### 2. CORS Trailing Slash Issue ✅
**Error:** `corsheaders.E014) Origin 'https://.../' in CORS_ALLOWED_ORIGINS should not have path`

**Fix Applied:**
- Updated [settings.py:187-192](backend/airbnb_project/settings.py#L187-L192) to automatically strip trailing slashes

### 3. Django Allauth Deprecation Warnings ✅
**Warning:** `ACCOUNT_AUTHENTICATION_METHOD is deprecated`

**Fix Applied:**
- Updated [settings.py:239-240](backend/airbnb_project/settings.py#L239-L240) to use new settings:
  - `ACCOUNT_LOGIN_METHODS = {'email'}`
  - `ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']`

## Commit and Deploy

```bash
# Add all changes
git add .

# Commit with descriptive message
git commit -m "Fix Render deployment issues: Python 3.12, CORS, and allauth settings"

# Push to trigger Render deployment
git push origin main
```

## Environment Variables to Set in Render

### Critical - Set These First:

```bash
PYTHON_VERSION=3.12.0
SECRET_KEY=<generate-using-command-below>
DEBUG=False
DATABASE_URL=<provided-by-render-database>
ALLOWED_HOSTS=<your-backend>.onrender.com
```

**Generate SECRET_KEY:**
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### CORS - IMPORTANT:

```bash
# DO NOT include trailing slashes!
# ✅ CORRECT:
CORS_ALLOWED_ORIGINS=https://your-frontend.onrender.com,http://localhost:3000

# ❌ WRONG:
CORS_ALLOWED_ORIGINS=https://your-frontend.onrender.com/,http://localhost:3000/
```

### Optional (for full functionality):

```bash
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
GOOGLE_OAUTH2_CLIENT_ID=...
GOOGLE_OAUTH2_CLIENT_SECRET=...
FACEBOOK_APP_ID=...
FACEBOOK_APP_SECRET=...
REDIS_URL=redis://...  # Only for paid plans
```

## After Deployment

### 1. Create Superuser

In Render Shell (click "Shell" button in dashboard):
```bash
python manage.py createsuperuser
```

### 2. Verify Deployment

**Backend:**
```bash
# Test admin page
curl https://your-backend.onrender.com/admin/

# Test API
curl https://your-backend.onrender.com/api/properties/
```

**Frontend:**
Visit: `https://your-frontend.onrender.com`

### 3. Check Logs

If issues persist:
1. Go to Render Dashboard
2. Click on your service
3. Click "Logs" tab
4. Look for errors in Build or Web logs

## Common Issues After These Fixes

### Issue: 502 Bad Gateway

**Cause:** Gunicorn not binding to correct port

**Solution:** Verify start command in render.yaml:
```bash
gunicorn airbnb_project.wsgi:application --bind 0.0.0.0:$PORT
```

### Issue: Database Connection Error

**Cause:** Using External instead of Internal database URL

**Solution:**
1. Go to Render Dashboard → Database
2. Copy **Internal Database URL** (not External)
3. Set as `DATABASE_URL` environment variable

### Issue: Static Files 404

**Cause:** Static files not collected or WhiteNoise misconfigured

**Solution:** Already configured correctly, but verify build.sh runs:
```bash
python manage.py collectstatic --no-input
```

### Issue: CORS Errors in Browser

**Cause:** Frontend URL not in CORS_ALLOWED_ORIGINS

**Solution:** Update backend environment variable:
```bash
CORS_ALLOWED_ORIGINS=https://your-actual-frontend.onrender.com
```
⚠️ **No trailing slash!**

## Deployment Checklist

Before deploying, ensure:

- [ ] All changes committed and pushed to GitHub
- [ ] Python version set to 3.12.0
- [ ] CORS_ALLOWED_ORIGINS has NO trailing slashes
- [ ] DATABASE_URL uses Internal URL from Render
- [ ] SECRET_KEY is generated and set
- [ ] DEBUG=False
- [ ] ALLOWED_HOSTS includes your .onrender.com domain
- [ ] Frontend REACT_APP_API_URL points to backend

## Getting Help

If you still have issues:

1. Check [RENDER_TROUBLESHOOTING.md](RENDER_TROUBLESHOOTING.md) for detailed solutions
2. Check [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md) for full deployment guide
3. Review Render logs for specific error messages
4. Visit [Render Community Forum](https://community.render.com)

---

**Last Updated:** December 2025
