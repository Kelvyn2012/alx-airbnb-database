from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id', 'booking', 'amount', 'payment_method',
                  'transaction_id', 'payment_date', 'is_successful']
        read_only_fields = ['payment_id', 'payment_date']


class PaymentCreateSerializer(serializers.ModelSerializer):
    booking_id = serializers.UUIDField()

    class Meta:
        model = Payment
        fields = ['booking_id', 'amount', 'payment_method']
