from django.urls import path
from .views import (
    PaymentListView,
    PaymentCreateView,
    PaymentDetailView
)

urlpatterns = [
    path('', PaymentListView.as_view(), name='payment-list'),
    path('create/', PaymentCreateView.as_view(), name='payment-create'),
    path('<uuid:payment_id>/', PaymentDetailView.as_view(), name='payment-detail'),
]
