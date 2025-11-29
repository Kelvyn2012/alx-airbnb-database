from rest_framework import serializers
from .models import Property, PropertyImage
from apps.users.serializers import UserSerializer


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['image_id', 'image', 'is_primary', 'created_at']
        read_only_fields = ['image_id', 'created_at']


class PropertySerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    images = serializers.SerializerMethodField()
    average_rating = serializers.ReadOnlyField()

    class Meta:
        model = Property
        fields = ['property_id', 'host', 'name', 'description', 'location',
                  'pricepernight', 'bedrooms', 'bathrooms', 'max_guests',
                  'amenities', 'is_active', 'images', 'average_rating',
                  'created_at', 'updated_at']
        read_only_fields = ['property_id', 'created_at', 'updated_at']

    def get_images(self, obj):
        # If property has uploaded images, return them
        if obj.images.exists():
            return PropertyImageSerializer(obj.images.all(), many=True).data

        # Return placeholder image as a single-item list
        image_map = {
            "Luxurious Beachfront Villa": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800",
            "Modern Downtown Loft": "https://images.unsplash.com/photo-1536376072261-38c75010e6c9?w=800",
            "Cozy Mountain Cabin": "https://images.unsplash.com/photo-1587061949409-02df41d5e562?w=800",
            "Tropical Paradise Bungalow": "https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=800",
            "Historic Brownstone Apartment": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800",
            "Lakefront Retreat": "https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=800",
            "Urban Studio Apartment": "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=800",
            "Vineyard Estate": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800",
            "Desert Oasis": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800",
            "Charming Cottage by the Sea": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800",
        }

        placeholder_url = image_map.get(obj.name, "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=800")

        return [{
            'image_id': None,
            'image': placeholder_url,
            'is_primary': True
        }]


class PropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['name', 'description', 'location', 'pricepernight',
                  'bedrooms', 'bathrooms', 'max_guests', 'amenities']


class PropertyListSerializer(serializers.ModelSerializer):
    host_name = serializers.CharField(source='host.full_name', read_only=True)
    average_rating = serializers.ReadOnlyField()
    primary_image = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = ['property_id', 'name', 'location', 'pricepernight',
                  'bedrooms', 'bathrooms', 'max_guests', 'host_name',
                  'primary_image', 'average_rating']

    def get_primary_image(self, obj):
        primary = obj.images.filter(is_primary=True).first()
        if primary:
            return self.context['request'].build_absolute_uri(primary.image.url)
        first_image = obj.images.first()
        if first_image:
            return self.context['request'].build_absolute_uri(first_image.image.url)

        # Return placeholder image based on property name/location
        image_map = {
            "Luxurious Beachfront Villa": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800",
            "Modern Downtown Loft": "https://images.unsplash.com/photo-1536376072261-38c75010e6c9?w=800",
            "Cozy Mountain Cabin": "https://images.unsplash.com/photo-1587061949409-02df41d5e562?w=800",
            "Tropical Paradise Bungalow": "https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=800",
            "Historic Brownstone Apartment": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800",
            "Lakefront Retreat": "https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=800",
            "Urban Studio Apartment": "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=800",
            "Vineyard Estate": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800",
            "Desert Oasis": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800",
            "Charming Cottage by the Sea": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800",
        }

        return image_map.get(obj.name, "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=800")
