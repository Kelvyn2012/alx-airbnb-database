from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'booking', 'amount', 'payment_method', 'is_successful', 'payment_date']
    list_filter = ['payment_method', 'is_successful', 'payment_date']
    search_fields = ['transaction_id', 'booking__booking_id']
    ordering = ['-payment_date']
