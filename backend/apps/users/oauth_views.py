from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.conf import settings
from django.shortcuts import redirect
import requests
from decouple import config

User = get_user_model()

BACKEND_URL = settings.BACKEND_URL
FRONTEND_URL = settings.FRONTEND_URL


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['GET'])
@permission_classes([AllowAny])
def google_login(request):
    """Initiate Google OAuth login"""
    google_client_id = config('GOOGLE_OAUTH2_CLIENT_ID', default='')
    redirect_uri = f'{BACKEND_URL}/api/users/auth/google/callback/'
    scope = 'openid email profile'

    google_auth_url = (
        f'https://accounts.google.com/o/oauth2/v2/auth?'
        f'client_id={google_client_id}&'
        f'redirect_uri={redirect_uri}&'
        f'response_type=code&'
        f'scope={scope}'
    )

    return redirect(google_auth_url)


@api_view(['GET'])
@permission_classes([AllowAny])
def google_callback(request):
    """Handle Google OAuth callback"""
    code = request.GET.get('code')

    if not code:
        return redirect(f'{FRONTEND_URL}/login?error=oauth_failed')

    redirect_uri = f'{BACKEND_URL}/api/users/auth/google/callback/'
    token_url = 'https://oauth2.googleapis.com/token'
    data = {
        'code': code,
        'client_id': config('GOOGLE_OAUTH2_CLIENT_ID', default=''),
        'client_secret': config('GOOGLE_OAUTH2_CLIENT_SECRET', default=''),
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }

    token_response = requests.post(token_url, data=data)
    token_json = token_response.json()
    access_token = token_json.get('access_token')

    if not access_token:
        return redirect(f'{FRONTEND_URL}/login?error=oauth_failed')

    user_info_url = 'https://www.googleapis.com/oauth2/v2/userinfo'
    headers = {'Authorization': f'Bearer {access_token}'}
    user_info_response = requests.get(user_info_url, headers=headers)
    user_info = user_info_response.json()

    email = user_info.get('email')
    first_name = user_info.get('given_name', '')
    last_name = user_info.get('family_name', '')

    user, created = User.objects.get_or_create(
        email=email,
        defaults={
            'first_name': first_name,
            'last_name': last_name,
            'role': 'guest',
        }
    )

    tokens = get_tokens_for_user(user)
    return redirect(f"{FRONTEND_URL}/oauth-callback?access={tokens['access']}&refresh={tokens['refresh']}")


@api_view(['GET'])
@permission_classes([AllowAny])
def facebook_login(request):
    """Initiate Facebook OAuth login"""
    facebook_app_id = config('FACEBOOK_APP_ID', default='')
    redirect_uri = f'{BACKEND_URL}/api/users/auth/facebook/callback/'
    scope = 'email,public_profile'

    facebook_auth_url = (
        f'https://www.facebook.com/v13.0/dialog/oauth?'
        f'client_id={facebook_app_id}&'
        f'redirect_uri={redirect_uri}&'
        f'scope={scope}'
    )

    return redirect(facebook_auth_url)


@api_view(['GET'])
@permission_classes([AllowAny])
def facebook_callback(request):
    """Handle Facebook OAuth callback"""
    code = request.GET.get('code')

    if not code:
        return redirect(f'{FRONTEND_URL}/login?error=oauth_failed')

    redirect_uri = f'{BACKEND_URL}/api/users/auth/facebook/callback/'
    token_url = 'https://graph.facebook.com/v13.0/oauth/access_token'
    params = {
        'code': code,
        'client_id': config('FACEBOOK_APP_ID', default=''),
        'client_secret': config('FACEBOOK_APP_SECRET', default=''),
        'redirect_uri': redirect_uri,
    }

    token_response = requests.get(token_url, params=params)
    token_json = token_response.json()
    access_token = token_json.get('access_token')

    if not access_token:
        return redirect(f'{FRONTEND_URL}/login?error=oauth_failed')

    user_info_url = 'https://graph.facebook.com/me'
    params = {
        'fields': 'id,email,first_name,last_name',
        'access_token': access_token
    }
    user_info_response = requests.get(user_info_url, params=params)
    user_info = user_info_response.json()

    email = user_info.get('email')
    if not email:
        return redirect(f'{FRONTEND_URL}/login?error=no_email')

    first_name = user_info.get('first_name', '')
    last_name = user_info.get('last_name', '')

    user, created = User.objects.get_or_create(
        email=email,
        defaults={
            'first_name': first_name,
            'last_name': last_name,
            'role': 'guest',
        }
    )

    tokens = get_tokens_for_user(user)
    return redirect(f"{FRONTEND_URL}/oauth-callback?access={tokens['access']}&refresh={tokens['refresh']}")
