# OAuth Setup Guide for Airbnb Clone

## Features Implemented

### 1. OAuth Authentication
- **Google OAuth 2.0** - Sign in with Google
- **Facebook OAuth** - Sign in with Facebook
- Seamless JWT token generation after OAuth success
- Automatic user creation on first OAuth login

### 2. Back Button
- Beautiful "← Back to Home" button on Login and Register pages
- Smooth hover animations with left slide effect
- Dark mode compatible styling

### 3. Night Mode (Dark Theme)
- Complete dark mode implementation across all pages
- Animated theme toggle button (🌙/☀️) in navbar
- Smooth transitions between light and dark themes
- localStorage persistence for theme preference

## Setting Up OAuth (Required for Production)

### Google OAuth Setup

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/

2. **Create a New Project**
   - Click "Select a project" → "New Project"
   - Name it (e.g., "Airbnb Clone")
   - Click "Create"

3. **Enable Google+ API**
   - Go to "APIs & Services" → "Library"
   - Search for "Google+ API"
   - Click "Enable"

4. **Create OAuth 2.0 Credentials**
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "OAuth client ID"
   - Application type: "Web application"
   - Name: "Airbnb Clone Web Client"
   - Authorized redirect URIs:
     - `http://localhost:8001/api/users/auth/google/callback/`
     - `http://127.0.0.1:8001/api/users/auth/google/callback/`
   - Click "Create"

5. **Copy Credentials**
   - Copy the **Client ID** and **Client Secret**

6. **Add to .env file**
   ```env
   GOOGLE_OAUTH2_CLIENT_ID=your_google_client_id_here
   GOOGLE_OAUTH2_CLIENT_SECRET=your_google_client_secret_here
   ```

### Facebook OAuth Setup

1. **Go to Facebook Developers**
   - Visit: https://developers.facebook.com/

2. **Create an App**
   - Click "My Apps" → "Create App"
   - Select "Consumer" → Click "Next"
   - App Name: "Airbnb Clone"
   - App Contact Email: your email
   - Click "Create App"

3. **Add Facebook Login**
   - In the dashboard, find "Facebook Login"
   - Click "Set Up"
   - Choose "Web"
   - Skip the quickstart

4. **Configure OAuth Redirect URIs**
   - Go to "Settings" → "Basic"
   - Add your domain: `localhost`
   - Go to "Facebook Login" → "Settings"
   - Valid OAuth Redirect URIs:
     - `http://localhost:8001/api/users/auth/facebook/callback/`
     - `http://127.0.0.1:8001/api/users/auth/facebook/callback/`
   - Save Changes

5. **Copy App Credentials**
   - In "Settings" → "Basic"
   - Copy **App ID** and **App Secret**

6. **Add to .env file**
   ```env
   FACEBOOK_APP_ID=your_facebook_app_id_here
   FACEBOOK_APP_SECRET=your_facebook_app_secret_here
   ```

## Testing OAuth (Development Mode)

For development testing without real OAuth credentials:

1. The OAuth buttons will appear on Login and Register pages
2. Clicking them will redirect to OAuth provider (will fail without credentials)
3. Users can still use email/password login normally

## How OAuth Works

1. **User clicks OAuth button** (Google or Facebook)
2. **Redirects to OAuth provider** for authentication
3. **User authorizes the app** at OAuth provider
4. **Provider redirects back** to our callback URL with auth code
5. **Backend exchanges code** for access token
6. **Backend fetches user info** from OAuth provider
7. **Creates/finds user** in database
8. **Generates JWT tokens** for our app
9. **Redirects to frontend** with tokens in URL
10. **Frontend stores tokens** and logs user in

## Features Overview

### OAuth Login Buttons
- Styled with provider branding (Google blue, Facebook blue)
- SVG icons for professional appearance
- Smooth hover animations
- Dark mode compatible

### Back Button
- Positioned top-left of auth cards
- "← Back to Home" with left slide animation on hover
- Navigates to homepage (/)
- Fully accessible with aria-label

### Night Mode
- Toggle button in navbar
- Persists across page reloads
- Smooth color transitions
- All components support both themes:
  - PropertyCard
  - PropertyDetail
  - Bookings
  - Login/Register forms
  - Navbar

## API Endpoints

### OAuth Endpoints
- `GET /api/users/auth/google/` - Initiate Google login
- `GET /api/users/auth/google/callback/` - Google callback
- `GET /api/users/auth/facebook/` - Initiate Facebook login
- `GET /api/users/auth/facebook/callback/` - Facebook callback

### Frontend Routes
- `/oauth-callback` - Handles OAuth redirect and token storage

## Security Notes

1. **HTTPS Required in Production** - OAuth providers require HTTPS
2. **Environment Variables** - Never commit OAuth secrets to git
3. **Redirect URI Matching** - Must exactly match configured URIs
4. **Token Security** - JWT tokens stored in localStorage

## Troubleshooting

### OAuth buttons not working?
- Check if .env variables are set correctly
- Verify redirect URIs match exactly in provider console
- Check browser console for errors

### Dark mode not persisting?
- Check localStorage in browser DevTools
- Clear cache and reload

### Back button not appearing?
- Refresh the page
- Check Auth.css is loading correctly

## Next Steps

1. Get OAuth credentials from Google and Facebook
2. Add them to your `.env` file
3. Restart the Django server
4. Test OAuth login flow
5. Deploy to production with HTTPS
