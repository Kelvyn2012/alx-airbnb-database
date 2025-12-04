from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.properties.models import Property
from decimal import Decimal

User = get_user_model()


class Command(BaseCommand):
    help = 'Seeds the database with sample properties'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding properties...')

        # Get or create a host user
        host_user, created = User.objects.get_or_create(
            email='host@example.com',
            defaults={
                'first_name': 'John',
                'last_name': 'Host',
                'role': 'host',
                'phone_number': '+1234567890'
            }
        )
        if created:
            host_user.set_password('HostPass123!')
            host_user.save()
            self.stdout.write(self.style.SUCCESS(f'Created host user: {host_user.email}'))
        else:
            self.stdout.write(f'Using existing host user: {host_user.email}')

        # Sample properties data
        properties_data = [
            {
                'name': 'Luxury Beach Villa',
                'description': 'Beautiful oceanfront villa with stunning sunset views. Perfect for families and groups looking for a relaxing beach vacation.',
                'location': 'Miami Beach, Florida',
                'pricepernight': Decimal('299.00'),
                'bedrooms': 4,
                'bathrooms': 3,
                'max_guests': 8,
                'amenities': 'WiFi, Pool, Beach Access, Air Conditioning, Kitchen, Parking, BBQ Grill'
            },
            {
                'name': 'Cozy Mountain Cabin',
                'description': 'Rustic cabin nestled in the mountains with breathtaking views. Ideal for hiking enthusiasts and nature lovers.',
                'location': 'Aspen, Colorado',
                'pricepernight': Decimal('199.00'),
                'bedrooms': 3,
                'bathrooms': 2,
                'max_guests': 6,
                'amenities': 'WiFi, Fireplace, Heating, Kitchen, Mountain View, Hiking Trails'
            },
            {
                'name': 'Downtown Studio Apartment',
                'description': 'Modern studio in the heart of the city. Walking distance to restaurants, shops, and entertainment.',
                'location': 'New York, NY',
                'pricepernight': Decimal('149.00'),
                'bedrooms': 1,
                'bathrooms': 1,
                'max_guests': 2,
                'amenities': 'WiFi, Air Conditioning, Kitchen, Gym Access, 24/7 Security'
            },
            {
                'name': 'Spacious Family House',
                'description': 'Large family home with backyard and play area. Great for extended stays and family gatherings.',
                'location': 'Austin, Texas',
                'pricepernight': Decimal('225.00'),
                'bedrooms': 5,
                'bathrooms': 4,
                'max_guests': 10,
                'amenities': 'WiFi, Pool, BBQ Grill, Parking, Kitchen, Backyard, Pet Friendly'
            },
            {
                'name': 'Romantic Countryside Cottage',
                'description': 'Charming cottage surrounded by vineyards and rolling hills. Perfect romantic getaway for couples.',
                'location': 'Napa Valley, California',
                'pricepernight': Decimal('275.00'),
                'bedrooms': 2,
                'bathrooms': 2,
                'max_guests': 4,
                'amenities': 'WiFi, Fireplace, Wine Tasting, Kitchen, Garden, Vineyard Views'
            },
            {
                'name': 'Modern Loft in Arts District',
                'description': 'Industrial-chic loft in trendy arts district. Exposed brick, high ceilings, and contemporary design.',
                'location': 'Portland, Oregon',
                'pricepernight': Decimal('179.00'),
                'bedrooms': 2,
                'bathrooms': 2,
                'max_guests': 4,
                'amenities': 'WiFi, Air Conditioning, Kitchen, Street Parking, Near Public Transit'
            },
            {
                'name': 'Lakefront Paradise',
                'description': 'Stunning property right on the lake with private dock. Water activities and serene natural setting.',
                'location': 'Lake Tahoe, California',
                'pricepernight': Decimal('349.00'),
                'bedrooms': 4,
                'bathrooms': 3,
                'max_guests': 8,
                'amenities': 'WiFi, Lake Access, Private Dock, Kayaks, Kitchen, Fireplace, BBQ'
            },
            {
                'name': 'Historic Townhouse',
                'description': 'Beautifully restored townhouse with original architectural details and modern amenities.',
                'location': 'Boston, Massachusetts',
                'pricepernight': Decimal('189.00'),
                'bedrooms': 3,
                'bathrooms': 2,
                'max_guests': 6,
                'amenities': 'WiFi, Heating, Kitchen, Parking, Historic District, Near T Station'
            },
            {
                'name': 'Desert Oasis Retreat',
                'description': 'Luxurious desert home with infinity pool and panoramic mountain views. Ultimate relaxation.',
                'location': 'Scottsdale, Arizona',
                'pricepernight': Decimal('319.00'),
                'bedrooms': 3,
                'bathrooms': 3,
                'max_guests': 6,
                'amenities': 'WiFi, Pool, Air Conditioning, Kitchen, Patio, Mountain Views, Golf Nearby'
            },
            {
                'name': 'Charming Garden Bungalow',
                'description': 'Quaint bungalow with beautiful garden and outdoor seating. Peaceful neighborhood setting.',
                'location': 'Seattle, Washington',
                'pricepernight': Decimal('159.00'),
                'bedrooms': 2,
                'bathrooms': 1,
                'max_guests': 4,
                'amenities': 'WiFi, Garden, Kitchen, Parking, Pet Friendly, Near Parks'
            },
            # Additional 20 properties
            {
                'name': 'Oceanview Penthouse',
                'description': 'Spectacular penthouse with 360-degree ocean views. Floor-to-ceiling windows and rooftop terrace.',
                'location': 'San Diego, California',
                'pricepernight': Decimal('449.00'),
                'bedrooms': 3,
                'bathrooms': 3,
                'max_guests': 6,
                'amenities': 'WiFi, Pool, Gym, Concierge, Ocean View, Rooftop Terrace, Parking'
            },
            {
                'name': 'Ski-In Ski-Out Chalet',
                'description': 'Luxury mountain chalet with direct ski slope access. Hot tub and stunning alpine views.',
                'location': 'Park City, Utah',
                'pricepernight': Decimal('599.00'),
                'bedrooms': 5,
                'bathrooms': 4,
                'max_guests': 10,
                'amenities': 'WiFi, Hot Tub, Fireplace, Ski Storage, Heated Floors, Mountain View'
            },
            {
                'name': 'Urban Warehouse Loft',
                'description': 'Converted warehouse with exposed beams and industrial charm. In the heart of downtown.',
                'location': 'Chicago, Illinois',
                'pricepernight': Decimal('195.00'),
                'bedrooms': 2,
                'bathrooms': 2,
                'max_guests': 4,
                'amenities': 'WiFi, Air Conditioning, Kitchen, Elevator, Street Parking'
            },
            {
                'name': 'Tropical Island Bungalow',
                'description': 'Authentic beach bungalow steps from white sand beaches. Perfect island escape.',
                'location': 'Key West, Florida',
                'pricepernight': Decimal('265.00'),
                'bedrooms': 2,
                'bathrooms': 1,
                'max_guests': 4,
                'amenities': 'WiFi, Beach Access, Outdoor Shower, Hammock, Bike Rental'
            },
            {
                'name': 'Wine Country Estate',
                'description': 'Elegant estate in the heart of wine country. Private vineyard and wine cellar.',
                'location': 'Sonoma, California',
                'pricepernight': Decimal('525.00'),
                'bedrooms': 4,
                'bathrooms': 4,
                'max_guests': 8,
                'amenities': 'WiFi, Pool, Wine Cellar, Vineyard, Chef Kitchen, Patio'
            },
            {
                'name': 'River House Retreat',
                'description': 'Peaceful riverside home with private fishing dock. Nature lovers paradise.',
                'location': 'Asheville, North Carolina',
                'pricepernight': Decimal('215.00'),
                'bedrooms': 3,
                'bathrooms': 2,
                'max_guests': 6,
                'amenities': 'WiFi, Fishing Dock, Canoe, Fire Pit, River View, BBQ'
            },
            {
                'name': 'Gothic Victorian Mansion',
                'description': 'Restored Victorian mansion with period furniture and modern comforts. Historic charm.',
                'location': 'San Francisco, California',
                'pricepernight': Decimal('385.00'),
                'bedrooms': 4,
                'bathrooms': 3,
                'max_guests': 8,
                'amenities': 'WiFi, Library, Garden, Parking, Historic Home, Bay Views'
            },
            {
                'name': 'Minimalist Japanese Studio',
                'description': 'Zen-inspired studio with Japanese soaking tub. Peaceful and modern aesthetic.',
                'location': 'Los Angeles, California',
                'pricepernight': Decimal('169.00'),
                'bedrooms': 1,
                'bathrooms': 1,
                'max_guests': 2,
                'amenities': 'WiFi, Japanese Tub, Meditation Space, Kitchen, Parking'
            },
            {
                'name': 'Ranch Style Farmhouse',
                'description': 'Authentic ranch farmhouse with horse stables. Experience country living.',
                'location': 'Fredericksburg, Texas',
                'pricepernight': Decimal('289.00'),
                'bedrooms': 4,
                'bathrooms': 3,
                'max_guests': 8,
                'amenities': 'WiFi, Horse Stables, Fire Pit, BBQ, Farm Animals, Hiking'
            },
            {
                'name': 'Cliffside Mediterranean Villa',
                'description': 'Stunning villa perched on cliffs overlooking the Pacific. Infinity pool and sunset views.',
                'location': 'Malibu, California',
                'pricepernight': Decimal('799.00'),
                'bedrooms': 5,
                'bathrooms': 5,
                'max_guests': 10,
                'amenities': 'WiFi, Infinity Pool, Ocean View, Wine Cellar, Chef Kitchen, Gym'
            },
            {
                'name': 'Cozy A-Frame Cabin',
                'description': 'Classic A-frame cabin in the woods. Perfect for couples seeking solitude.',
                'location': 'Big Bear, California',
                'pricepernight': Decimal('185.00'),
                'bedrooms': 1,
                'bathrooms': 1,
                'max_guests': 2,
                'amenities': 'WiFi, Fireplace, Forest View, Wood Stove, Hiking Trails'
            },
            {
                'name': 'Southern Plantation Home',
                'description': 'Grand plantation home with wrap-around porch. Southern hospitality at its finest.',
                'location': 'Charleston, South Carolina',
                'pricepernight': Decimal('425.00'),
                'bedrooms': 5,
                'bathrooms': 4,
                'max_guests': 10,
                'amenities': 'WiFi, Pool, Garden, Porch, Historic Home, Parking'
            },
            {
                'name': 'Mountain View Glamping Dome',
                'description': 'Luxury glamping dome with panoramic mountain views. Unique outdoor experience.',
                'location': 'Moab, Utah',
                'pricepernight': Decimal('245.00'),
                'bedrooms': 1,
                'bathrooms': 1,
                'max_guests': 2,
                'amenities': 'WiFi, Stargazing, Outdoor Shower, Kitchenette, Hiking Access'
            },
            {
                'name': 'Bayfront Condo',
                'description': 'Modern condo with private balcony overlooking the bay. Steps from downtown.',
                'location': 'Tampa, Florida',
                'pricepernight': Decimal('205.00'),
                'bedrooms': 2,
                'bathrooms': 2,
                'max_guests': 4,
                'amenities': 'WiFi, Pool, Gym, Bay View, Parking, Elevator'
            },
            {
                'name': 'Artist Live-Work Loft',
                'description': 'Inspiring loft space with high ceilings and natural light. Perfect for creatives.',
                'location': 'Brooklyn, New York',
                'pricepernight': Decimal('235.00'),
                'bedrooms': 2,
                'bathrooms': 1,
                'max_guests': 4,
                'amenities': 'WiFi, Natural Light, Workspace, Kitchen, Near Subway'
            },
            {
                'name': 'Rustic Log Cabin',
                'description': 'Traditional log cabin with stone fireplace. Authentic wilderness experience.',
                'location': 'Jackson Hole, Wyoming',
                'pricepernight': Decimal('325.00'),
                'bedrooms': 3,
                'bathrooms': 2,
                'max_guests': 6,
                'amenities': 'WiFi, Fireplace, Hot Tub, Mountain View, Wildlife, Hiking'
            },
            {
                'name': 'Boho Beachfront Cottage',
                'description': 'Eclectic beach cottage with bohemian décor. Direct beach access.',
                'location': 'Venice Beach, California',
                'pricepernight': Decimal('275.00'),
                'bedrooms': 2,
                'bathrooms': 2,
                'max_guests': 4,
                'amenities': 'WiFi, Beach Access, Outdoor Shower, Patio, Bike Storage'
            },
            {
                'name': 'Smart Home Apartment',
                'description': 'Fully automated smart home with voice controls. Ultra-modern conveniences.',
                'location': 'San Jose, California',
                'pricepernight': Decimal('199.00'),
                'bedrooms': 2,
                'bathrooms': 2,
                'max_guests': 4,
                'amenities': 'WiFi, Smart Home, Voice Control, Kitchen, Gym, Parking'
            },
            {
                'name': 'Converted Church Loft',
                'description': 'Unique loft in a converted historic church. Soaring ceilings and stained glass.',
                'location': 'Philadelphia, Pennsylvania',
                'pricepernight': Decimal('295.00'),
                'bedrooms': 2,
                'bathrooms': 2,
                'max_guests': 4,
                'amenities': 'WiFi, Historic Building, High Ceilings, Kitchen, Parking'
            },
            {
                'name': 'Treehouse Hideaway',
                'description': 'Luxury treehouse nestled in ancient oaks. Magical forest retreat.',
                'location': 'Savannah, Georgia',
                'pricepernight': Decimal('255.00'),
                'bedrooms': 1,
                'bathrooms': 1,
                'max_guests': 2,
                'amenities': 'WiFi, Treehouse, Forest View, Deck, Kitchenette, Nature Trails'
            },
        ]

        created_count = 0
        for property_data in properties_data:
            # Check if property already exists
            if not Property.objects.filter(name=property_data['name']).exists():
                Property.objects.create(host=host_user, **property_data)
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Created property: {property_data["name"]}'))
            else:
                self.stdout.write(f'Property already exists: {property_data["name"]}')

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully seeded {created_count} properties!'))
        self.stdout.write(self.style.SUCCESS(f'Host credentials: {host_user.email} / HostPass123!'))
