from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'booking_property', 'user', 'start_date', 'end_date', 'status', 'total_price']
    list_filter = ['status', 'created_at']
    search_fields = ['booking_property__name', 'user__email']
    ordering = ['-created_at']
