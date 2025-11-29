from django.urls import path
from .views import (
    BookingListView,
    BookingCreateView,
    BookingDetailView,
    HostBookingsView
)

urlpatterns = [
    path('', BookingListView.as_view(), name='booking-list'),
    path('create/', BookingCreateView.as_view(), name='booking-create'),
    path('host/', HostBookingsView.as_view(), name='host-bookings'),
    path('<uuid:booking_id>/', BookingDetailView.as_view(), name='booking-detail'),
]
