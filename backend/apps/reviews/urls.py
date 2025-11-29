from django.urls import path
from .views import (
    ReviewListView,
    ReviewCreateView,
    ReviewDetailView
)

urlpatterns = [
    path('property/<uuid:property_id>/', ReviewListView.as_view(), name='review-list'),
    path('create/', ReviewCreateView.as_view(), name='review-create'),
    path('<uuid:review_id>/', ReviewDetailView.as_view(), name='review-detail'),
]
