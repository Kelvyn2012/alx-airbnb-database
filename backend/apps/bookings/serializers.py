from rest_framework import serializers
from .models import Booking
from apps.properties.serializers import PropertyListSerializer
from apps.users.serializers import UserSerializer


class BookingSerializer(serializers.ModelSerializer):
    property = PropertyListSerializer(source='booking_property', read_only=True)
    user = UserSerializer(read_only=True)
    nights = serializers.ReadOnlyField()

    class Meta:
        model = Booking
        fields = ['booking_id', 'property', 'user', 'start_date', 'end_date',
                  'total_price', 'status', 'guests', 'nights', 'created_at']
        read_only_fields = ['booking_id', 'created_at']


class BookingCreateSerializer(serializers.ModelSerializer):
    property_id = serializers.UUIDField()

    class Meta:
        model = Booking
        fields = ['property_id', 'start_date', 'end_date', 'guests']

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("End date must be after start date")
        return data


class BookingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['status']
