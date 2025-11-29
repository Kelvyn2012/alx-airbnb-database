from rest_framework import serializers
from .models import Review
from apps.users.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    property = serializers.UUIDField(source='review_property.property_id', read_only=True)

    class Meta:
        model = Review
        fields = ['review_id', 'property', 'user', 'rating', 'comment',
                  'created_at', 'updated_at']
        read_only_fields = ['review_id', 'created_at', 'updated_at']


class ReviewCreateSerializer(serializers.ModelSerializer):
    property_id = serializers.UUIDField()

    class Meta:
        model = Review
        fields = ['property_id', 'rating', 'comment']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5")
        return value
