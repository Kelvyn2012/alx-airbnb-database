import os
import django
import sys
from pathlib import Path

# Setup Django
sys.path.append(str(Path(__file__).resolve().parent))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airbnb_project.settings')
django.setup()

from apps.users.models import User
from apps.properties.models import Property, PropertyImage
from decimal import Decimal

def create_sample_properties():
    print("Creating sample properties...")

    # Create a host user if doesn't exist
    host_email = "host@example.com"
    try:
        host = User.objects.get(email=host_email)
        print(f"Host user already exists: {host.email}")
    except User.DoesNotExist:
        host = User.objects.create_user(
            email=host_email,
            password="HostPassword123!",
            first_name="John",
            last_name="Host",
            role="host"
        )
        print(f"Created host user: {host.email}")

    # Sample properties data
    properties_data = [
        {
            "name": "Luxurious Beachfront Villa",
            "description": "Wake up to stunning ocean views in this beautiful beachfront villa. Features a private pool, spacious deck, and direct beach access. Perfect for families or groups looking for a relaxing getaway.",
            "location": "Malibu, California",
            "pricepernight": Decimal("450.00"),
            "bedrooms": 4,
            "bathrooms": 3,
            "max_guests": 8,
            "amenities": "WiFi, Pool, Beach Access, Parking, Kitchen, Air Conditioning, TV, Washer, Dryer",
            "image_url": "https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800"
        },
        {
            "name": "Modern Downtown Loft",
            "description": "Stylish loft in the heart of downtown. Walking distance to restaurants, bars, and entertainment. Floor-to-ceiling windows with city views. Perfect for business travelers or couples.",
            "location": "New York, New York",
            "pricepernight": Decimal("250.00"),
            "bedrooms": 2,
            "bathrooms": 2,
            "max_guests": 4,
            "amenities": "WiFi, Elevator, Gym, Kitchen, Air Conditioning, TV, Workspace",
            "image_url": "https://images.unsplash.com/photo-1502672260066-6bc35f0a44fd?w=800"
        },
        {
            "name": "Cozy Mountain Cabin",
            "description": "Escape to nature in this charming mountain cabin. Surrounded by pine trees with mountain views. Features a fireplace, hot tub, and large deck. Ideal for a peaceful retreat.",
            "location": "Aspen, Colorado",
            "pricepernight": Decimal("320.00"),
            "bedrooms": 3,
            "bathrooms": 2,
            "max_guests": 6,
            "amenities": "WiFi, Fireplace, Hot Tub, Parking, Kitchen, Heating, TV, Mountain View",
            "image_url": "https://images.unsplash.com/photo-1587061949409-02df41d5e562?w=800"
        },
        {
            "name": "Tropical Paradise Bungalow",
            "description": "Experience island living in this beautiful tropical bungalow. Surrounded by lush gardens with ocean breezes. Close to beaches, restaurants, and local attractions.",
            "location": "Honolulu, Hawaii",
            "pricepernight": Decimal("380.00"),
            "bedrooms": 3,
            "bathrooms": 2,
            "max_guests": 6,
            "amenities": "WiFi, Garden, Parking, Kitchen, Air Conditioning, TV, Outdoor Shower, BBQ",
            "image_url": "https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=800"
        },
        {
            "name": "Historic Brownstone Apartment",
            "description": "Charming apartment in a beautifully restored brownstone. Original hardwood floors, high ceilings, and modern amenities. Located in a quiet, tree-lined neighborhood.",
            "location": "Boston, Massachusetts",
            "pricepernight": Decimal("210.00"),
            "bedrooms": 2,
            "bathrooms": 1,
            "max_guests": 4,
            "amenities": "WiFi, Kitchen, Heating, TV, Washer, Dryer, Street Parking",
            "image_url": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800"
        },
        {
            "name": "Lakefront Retreat",
            "description": "Stunning lakefront property with private dock and kayaks. Perfect for fishing, swimming, and water sports. Large windows overlooking the lake, outdoor fire pit, and spacious deck.",
            "location": "Lake Tahoe, Nevada",
            "pricepernight": Decimal("395.00"),
            "bedrooms": 4,
            "bathrooms": 3,
            "max_guests": 8,
            "amenities": "WiFi, Lake Access, Dock, Kayaks, Parking, Kitchen, Fireplace, BBQ, Fire Pit",
            "image_url": "https://images.unsplash.com/photo-1499696010180-025ef6e1a8f9?w=800"
        },
        {
            "name": "Urban Studio Apartment",
            "description": "Compact and efficient studio in a trendy neighborhood. Perfect for solo travelers or couples. Walking distance to cafes, shops, and public transportation.",
            "location": "Seattle, Washington",
            "pricepernight": Decimal("120.00"),
            "bedrooms": 1,
            "bathrooms": 1,
            "max_guests": 2,
            "amenities": "WiFi, Kitchen, Heating, TV, Workspace, Public Transport",
            "image_url": "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=800"
        },
        {
            "name": "Vineyard Estate",
            "description": "Luxurious estate in wine country. Surrounded by vineyards with stunning views. Features a gourmet kitchen, wine cellar, and outdoor entertaining areas. Perfect for special occasions.",
            "location": "Napa Valley, California",
            "pricepernight": Decimal("650.00"),
            "bedrooms": 5,
            "bathrooms": 4,
            "max_guests": 10,
            "amenities": "WiFi, Pool, Wine Cellar, Parking, Gourmet Kitchen, Air Conditioning, TV, Vineyard View, BBQ",
            "image_url": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800"
        },
        {
            "name": "Desert Oasis",
            "description": "Contemporary desert home with stunning mountain views. Features a saltwater pool, outdoor kitchen, and modern desert landscaping. Perfect for relaxation and stargazing.",
            "location": "Scottsdale, Arizona",
            "pricepernight": Decimal("340.00"),
            "bedrooms": 3,
            "bathrooms": 3,
            "max_guests": 6,
            "amenities": "WiFi, Pool, Outdoor Kitchen, Parking, Kitchen, Air Conditioning, TV, Desert View, Fire Pit",
            "image_url": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800"
        },
        {
            "name": "Charming Cottage by the Sea",
            "description": "Quaint cottage just steps from the beach. Features a cozy fireplace, ocean views, and a private garden. Perfect for romantic getaways or small families.",
            "location": "Cape Cod, Massachusetts",
            "pricepernight": Decimal("280.00"),
            "bedrooms": 2,
            "bathrooms": 1,
            "max_guests": 4,
            "amenities": "WiFi, Beach Access, Garden, Parking, Kitchen, Fireplace, TV, Ocean View",
            "image_url": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800"
        }
    ]

    created_count = 0
    for prop_data in properties_data:
        # Check if property already exists
        if not Property.objects.filter(name=prop_data["name"]).exists():
            # Extract image URL before creating property
            image_url = prop_data.pop("image_url")

            # Create property
            property_obj = Property.objects.create(
                host=host,
                **prop_data
            )

            print(f"Created property: {property_obj.name} - ${property_obj.pricepernight}/night in {property_obj.location}")
            print(f"  Image URL: {image_url}")
            created_count += 1
        else:
            print(f"Property already exists: {prop_data['name']}")

    print(f"\nTotal properties created: {created_count}")
    print(f"Total properties in database: {Property.objects.count()}")

    # Display summary
    print("\n=== Property Summary ===")
    for prop in Property.objects.all().order_by('-created_at'):
        print(f"- {prop.name}")
        print(f"  Location: {prop.location}")
        print(f"  Price: ${prop.pricepernight}/night")
        print(f"  Bedrooms: {prop.bedrooms}, Bathrooms: {prop.bathrooms}, Max Guests: {prop.max_guests}")
        print()

if __name__ == "__main__":
    create_sample_properties()
