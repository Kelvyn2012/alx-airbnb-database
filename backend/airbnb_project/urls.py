from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

def api_root(request):
    """API root endpoint with links to documentation and main endpoints"""
    return JsonResponse({
        'message': 'Welcome to Airbnb Clone API',
        'version': 'v1',
        'documentation': {
            'swagger': request.build_absolute_uri('/swagger/'),
            'redoc': request.build_absolute_uri('/redoc/'),
        },
        'endpoints': {
            'users': request.build_absolute_uri('/api/users/'),
            'properties': request.build_absolute_uri('/api/properties/'),
            'bookings': request.build_absolute_uri('/api/bookings/'),
            'payments': request.build_absolute_uri('/api/payments/'),
            'reviews': request.build_absolute_uri('/api/reviews/'),
            'messages': request.build_absolute_uri('/api/messages/'),
        },
        'authentication': {
            'login': request.build_absolute_uri('/api/users/login/'),
            'register': request.build_absolute_uri('/api/users/register/'),
            'token_refresh': request.build_absolute_uri('/api/users/token/refresh/'),
        }
    })

schema_view = get_schema_view(
   openapi.Info(
      title="Airbnb Clone API",
      default_version='v1',
      description="""
# Airbnb Clone API Documentation

Complete REST API for an Airbnb-like property rental platform.

## Authentication
This API uses JWT (JSON Web Token) authentication. To access protected endpoints:

1. Register or login to get access and refresh tokens
2. Click the 'Authorize' button (🔒) at the top right
3. Enter your token in the format: `Bearer <your_access_token>`
4. Click 'Authorize' and close the dialog

## Features
- User authentication and profiles
- Property listings and management
- Booking system
- Payment processing with Stripe
- Reviews and ratings
- Real-time messaging
      """,
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@airbnb.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[],
)

urlpatterns = [
    # Root API endpoint
    path('', api_root, name='api-root'),
    path('api/', api_root, name='api-root-alt'),

    # Admin
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/users/', include('apps.users.urls')),
    path('api/properties/', include('apps.properties.urls')),
    path('api/bookings/', include('apps.bookings.urls')),
    path('api/payments/', include('apps.payments.urls')),
    path('api/reviews/', include('apps.reviews.urls')),
    path('api/messages/', include('apps.messages.urls')),

    # API Documentation
    path('swagger<str:format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-alt'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
