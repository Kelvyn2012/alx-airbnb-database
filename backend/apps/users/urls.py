from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
    UserDetailView
)
from .oauth_views import (
    google_login,
    google_callback,
    facebook_login,
    facebook_callback,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('<uuid:user_id>/', UserDetailView.as_view(), name='user-detail'),

    # OAuth endpoints
    path('auth/google/', google_login, name='google-login'),
    path('auth/google/callback/', google_callback, name='google-callback'),
    path('auth/facebook/', facebook_login, name='facebook-login'),
    path('auth/facebook/callback/', facebook_callback, name='facebook-callback'),
]
