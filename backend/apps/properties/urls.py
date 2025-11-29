from django.urls import path
from .views import (
    PropertyListView,
    PropertyCreateView,
    PropertyDetailView,
    MyPropertiesView,
    PropertyImageUploadView
)

urlpatterns = [
    path('', PropertyListView.as_view(), name='property-list'),
    path('create/', PropertyCreateView.as_view(), name='property-create'),
    path('my-properties/', MyPropertiesView.as_view(), name='my-properties'),
    path('<uuid:property_id>/', PropertyDetailView.as_view(), name='property-detail'),
    path('<uuid:property_id>/images/', PropertyImageUploadView.as_view(), name='property-image-upload'),
]
