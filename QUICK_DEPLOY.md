# Quick Deploy Checklist

Use this as a quick reference while deploying. For detailed instructions, see DEPLOYMENT_GUIDE.md.

## ☐ Pre-Deployment (Done! ✅)
- ✅ Migrations run locally
- ✅ Requirements.txt updated
- ✅ Settings.py configured
- ✅ Vercel config files created
- ✅ Static files collected

## ☐ 1. Neon Database Setup (5 mins)

```bash
# 1. Go to https://neon.tech
# 2. Create new project: "airbnb-backend"
# 3. Copy connection string
```

**Connection string format:**
```
postgres://username:password@ep-xxx-xxx.region.aws.neon.tech/dbname?sslmode=require
```

**Run migrations to Neon:**
```bash
cd backend
echo "DATABASE_URL=<paste-neon-url-here>" >> .env.production
source venv/bin/activate
export $(cat .env.production | xargs)
python3.12 manage.py migrate
```

## ☐ 2. Push to GitHub (2 mins)

```bash
git add .
git commit -m "Configure backend for Vercel + Neon deployment"
git push origin main
```

## ☐ 3. Deploy Backend to Vercel (5 mins)

1. Go to: https://vercel.com/new
2. Import your GitHub repo
3. Configure:
   - Framework: **Other**
   - Root Directory: **backend**
   - Build Command: **bash build_files.sh**
   - Output Directory: **staticfiles**

4. Click **Deploy** (don't add env vars yet - do next step first)

## ☐ 4. Add Backend Environment Variables (3 mins)

Go to: Project → Settings → Environment Variables

**Minimum required:**
```
DATABASE_URL=<your-neon-connection-string>
SECRET_KEY=<generate-new-secret-key>
DEBUG=False
ALLOWED_HOSTS=.vercel.app,.neon.tech
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3001
```

**Generate new SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Optional (add if you use them):**
```
STRIPE_PUBLIC_KEY=<your-key>
STRIPE_SECRET_KEY=<your-key>
GOOGLE_OAUTH2_CLIENT_ID=<your-id>
GOOGLE_OAUTH2_CLIENT_SECRET=<your-secret>
FACEBOOK_APP_ID=<your-id>
FACEBOOK_APP_SECRET=<your-secret>
```

After adding, click: **Redeploy** button

## ☐ 5. Test Backend (2 mins)

Your backend URL: `https://your-project-name.vercel.app`

Test these endpoints:
```bash
# Admin panel
curl https://your-project-name.vercel.app/admin/

# API root
curl https://your-project-name.vercel.app/api/

# Check if it returns HTML/JSON without errors
```

## ☐ 6. Update Frontend Config (3 mins)

**In your frontend code:**

Create/update `.env.local`:
```bash
NEXT_PUBLIC_API_URL=https://your-backend-name.vercel.app
```

**Update API calls** (if needed):
```javascript
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
```

Commit changes:
```bash
git add .
git commit -m "Update API URL for production"
git push origin main
```

## ☐ 7. Deploy Frontend to Vercel (5 mins)

1. Go to: https://vercel.com/new
2. Import same GitHub repo
3. Configure:
   - Framework: **Auto-detect** (Next.js/React/etc)
   - Root Directory: **frontend**
   - Build Command: **Auto**
   - Output Directory: **Auto**

4. Add environment variable:
   ```
   NEXT_PUBLIC_API_URL=https://your-backend-name.vercel.app
   ```

5. Click **Deploy**

## ☐ 8. Update CORS Settings (2 mins)

After frontend deploys, get its URL: `https://your-frontend.vercel.app`

**Update backend CORS:**
1. Go to backend project in Vercel
2. Settings → Environment Variables
3. Update `CORS_ALLOWED_ORIGINS`:
   ```
   https://your-frontend.vercel.app,http://localhost:3000,http://localhost:3001
   ```
4. Click **Redeploy**

## ☐ 9. Final Testing (5 mins)

### Test Backend:
```bash
curl https://your-backend.vercel.app/admin/
```
Should return Django admin HTML

### Test Frontend:
Open: `https://your-frontend.vercel.app`
- Check if pages load
- Check if API calls work
- Check browser console for CORS errors

### Test Full Flow:
1. Try to register/login
2. Try to view properties
3. Try to make a booking
4. Check if data saves to database

## ☐ 10. Create Admin User (Optional, 3 mins)

**Option A: Via local environment**
```bash
cd backend
export DATABASE_URL=<your-neon-url>
source venv/bin/activate
python3.12 manage.py createsuperuser
```

**Option B: Via Django admin**
- Create a signup endpoint
- Register a user via API
- Manually set `is_staff=True` in Neon database

## 🎉 Deployment Complete!

Your URLs:
- Frontend: `https://your-frontend.vercel.app`
- Backend: `https://your-backend.vercel.app`
- Backend Admin: `https://your-backend.vercel.app/admin/`
- API Docs: `https://your-backend.vercel.app/api/docs/`

## 📊 Monitoring

**Vercel Dashboard:**
- Check deployment logs
- Monitor function executions
- View analytics

**Neon Dashboard:**
- Monitor database queries
- Check storage usage
- View connection stats

## 🚨 Common Issues & Fixes

### Issue: 500 Error on backend
**Fix:** Check Vercel function logs
```
Vercel Project → Deployments → Click deployment → View Function Logs
```

### Issue: CORS errors
**Fix:** Update CORS_ALLOWED_ORIGINS and redeploy
```
Backend Settings → Environment Variables → Update CORS → Redeploy
```

### Issue: Database connection failed
**Fix:** Verify DATABASE_URL
```
- Check it includes ?sslmode=require
- Test connection locally first
- Verify Neon database is active
```

### Issue: Static files not loading
**Fix:** Run collectstatic
```bash
python3.12 manage.py collectstatic --noinput
```
Then commit and redeploy

## 🔄 Future Deployments

After initial setup, deploying updates is simple:

```bash
git add .
git commit -m "Your changes"
git push origin main
```

Vercel auto-deploys on push! 🚀

## 📚 Full Documentation

- **Detailed Guide:** DEPLOYMENT_GUIDE.md
- **Environment Variables:** backend/VERCEL_ENV_SETUP.md
- **Summary:** DEPLOYMENT_SUMMARY.md

---

**Time Estimate:** 30-40 minutes total for first deployment

Good luck! 🎯
