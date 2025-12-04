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

        # Return unique placeholder images as a list
        image_map = {
            # Beach/Coastal Properties
            "Luxury Beach Villa": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=1200&q=80",
            "Charming Cottage by the Sea": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=80",
            "Tropical Island Bungalow": "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=1200&q=80",
            "Boho Beachfront Cottage": "https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?w=1200&q=80",

            # Mountain/Cabin Properties
            "Cozy Mountain Cabin": "https://images.unsplash.com/photo-1587061949409-02df41d5e562?w=1200&q=80",
            "Ski-In Ski-Out Chalet": "https://images.unsplash.com/photo-1502784444187-359ac186c5bb?w=1200&q=80",
            "Cozy A-Frame Cabin": "https://images.unsplash.com/photo-1542718610-a1d656d1884c?w=1200&q=80",
            "Rustic Log Cabin": "https://images.unsplash.com/photo-1449158743715-0a90ebb6d2d8?w=1200&q=80",
            "Mountain View Glamping Dome": "https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=1200&q=80",

            # Urban/City Properties
            "Downtown Studio Apartment": "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=1200&q=80",
            "Modern Loft in Arts District": "https://images.unsplash.com/photo-1536376072261-38c75010e6c9?w=1200&q=80",
            "Historic Townhouse": "https://images.unsplash.com/photo-1523217582562-09d0def993a6?w=1200&q=80",
            "Urban Warehouse Loft": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=1200&q=80",
            "Oceanview Penthouse": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "Bayfront Condo": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
            "Artist Live-Work Loft": "https://images.unsplash.com/photo-1484154218962-a197022b5858?w=1200&q=80",
            "Minimalist Japanese Studio": "https://images.unsplash.com/photo-1540518614846-7eded433c457?w=1200&q=80",
            "Smart Home Apartment": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1200&q=80",
            "Converted Church Loft": "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=1200&q=80",

            # House/Family Properties
            "Spacious Family House": "https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=1200&q=80",
            "Ranch Style Farmhouse": "https://images.unsplash.com/photo-1560185127-6a7e5a0f0e12?w=1200&q=80",
            "Southern Plantation Home": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=1200&q=80",
            "Gothic Victorian Mansion": "https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=1200&q=80",

            # Countryside/Rural Properties
            "Romantic Countryside Cottage": "https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=1200&q=80",
            "Charming Garden Bungalow": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80",
            "Wine Country Estate": "https://images.unsplash.com/photo-1580587771525-78b9dba3b914?w=1200&q=80",
            "River House Retreat": "https://images.unsplash.com/photo-1505916349660-8d91a99c3e23?w=1200&q=80",
            "Treehouse Hideaway": "https://images.unsplash.com/photo-1587061949409-02df41d5e562?w=1200&q=80",

            # Lake/Water Properties
            "Lakefront Paradise": "https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=1200&q=80",
            "Cliffside Mediterranean Villa": "https://images.unsplash.com/photo-1613977257363-707ba9348227?w=1200&q=80",

            # Desert/Southwest Properties
            "Desert Oasis Retreat": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
        }

        placeholder_url = image_map.get(obj.name, "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=1200&q=80")

        return [{
            'image_id': None,
            'image': placeholder_url,
            'is_primary': True
        }]


class PropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['property_id', 'name', 'description', 'location', 'pricepernight',
                  'bedrooms', 'bathrooms', 'max_guests', 'amenities']
        read_only_fields = ['property_id']


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

        # Return unique placeholder images based on property name
        image_map = {
            # Beach/Coastal Properties
            "Luxury Beach Villa": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=1200&q=80",
            "Charming Cottage by the Sea": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=80",
            "Tropical Island Bungalow": "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=1200&q=80",
            "Boho Beachfront Cottage": "https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?w=1200&q=80",

            # Mountain/Cabin Properties
            "Cozy Mountain Cabin": "https://images.unsplash.com/photo-1587061949409-02df41d5e562?w=1200&q=80",
            "Ski-In Ski-Out Chalet": "https://images.unsplash.com/photo-1502784444187-359ac186c5bb?w=1200&q=80",
            "Cozy A-Frame Cabin": "https://images.unsplash.com/photo-1542718610-a1d656d1884c?w=1200&q=80",
            "Rustic Log Cabin": "https://images.unsplash.com/photo-1449158743715-0a90ebb6d2d8?w=1200&q=80",
            "Mountain View Glamping Dome": "https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=1200&q=80",

            # Urban/City Properties
            "Downtown Studio Apartment": "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=1200&q=80",
            "Modern Loft in Arts District": "https://images.unsplash.com/photo-1536376072261-38c75010e6c9?w=1200&q=80",
            "Historic Townhouse": "https://images.unsplash.com/photo-1523217582562-09d0def993a6?w=1200&q=80",
            "Urban Warehouse Loft": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=1200&q=80",
            "Oceanview Penthouse": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "Bayfront Condo": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=1200&q=80",
            "Artist Live-Work Loft": "https://images.unsplash.com/photo-1484154218962-a197022b5858?w=1200&q=80",
            "Minimalist Japanese Studio": "https://images.unsplash.com/photo-1540518614846-7eded433c457?w=1200&q=80",
            "Smart Home Apartment": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=1200&q=80",
            "Converted Church Loft": "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=1200&q=80",

            # House/Family Properties
            "Spacious Family House": "https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=1200&q=80",
            "Ranch Style Farmhouse": "https://images.unsplash.com/photo-1560185127-6a7e5a0f0e12?w=1200&q=80",
            "Southern Plantation Home": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=1200&q=80",
            "Gothic Victorian Mansion": "https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=1200&q=80",

            # Countryside/Rural Properties
            "Romantic Countryside Cottage": "https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=1200&q=80",
            "Charming Garden Bungalow": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80",
            "Wine Country Estate": "https://images.unsplash.com/photo-1580587771525-78b9dba3b914?w=1200&q=80",
            "River House Retreat": "https://images.unsplash.com/photo-1505916349660-8d91a99c3e23?w=1200&q=80",
            "Treehouse Hideaway": "https://images.unsplash.com/photo-1587061949409-02df41d5e562?w=1200&q=80",

            # Lake/Water Properties
            "Lakefront Paradise": "https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=1200&q=80",
            "Cliffside Mediterranean Villa": "https://images.unsplash.com/photo-1613977257363-707ba9348227?w=1200&q=80",

            # Desert/Southwest Properties
            "Desert Oasis Retreat": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
        }

        return image_map.get(obj.name, "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=1200&q=80")
