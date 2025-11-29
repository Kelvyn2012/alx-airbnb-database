import os
import django
import sys
from pathlib import Path
from random import choice, randint

# Setup Django
sys.path.append(str(Path(__file__).resolve().parent))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airbnb_project.settings')
django.setup()

from apps.users.models import User
from apps.properties.models import Property
from apps.reviews.models import Review

def create_sample_reviews():
    print("Creating sample reviews...")

    # Create some guest users if they don't exist
    guests_data = [
        {"email": "sarah.johnson@example.com", "first_name": "Sarah", "last_name": "Johnson"},
        {"email": "mike.chen@example.com", "first_name": "Mike", "last_name": "Chen"},
        {"email": "emma.davis@example.com", "first_name": "Emma", "last_name": "Davis"},
        {"email": "james.wilson@example.com", "first_name": "James", "last_name": "Wilson"},
        {"email": "lisa.anderson@example.com", "first_name": "Lisa", "last_name": "Anderson"},
    ]

    guests = []
    for guest_data in guests_data:
        guest, created = User.objects.get_or_create(
            email=guest_data["email"],
            defaults={
                "first_name": guest_data["first_name"],
                "last_name": guest_data["last_name"],
                "role": "guest"
            }
        )
        if created:
            guest.set_password("GuestPassword123!")
            guest.save()
            print(f"Created guest: {guest.email}")
        guests.append(guest)

    # Sample review comments
    positive_comments = [
        "Amazing place! The location was perfect and the host was very responsive.",
        "We had a wonderful time. The property exceeded our expectations in every way.",
        "Beautiful home with all the amenities we needed. Highly recommend!",
        "Stunning views and a very comfortable stay. Would definitely come back!",
        "Perfect getaway! Everything was clean and well-maintained.",
        "Great location, beautiful property, and excellent host communication.",
        "This place is a hidden gem! Loved every minute of our stay.",
        "Exceeded all expectations. The photos don't do it justice!",
        "Wonderful experience from start to finish. Five stars!",
        "Best vacation rental we've ever stayed at. Absolutely perfect!",
    ]

    good_comments = [
        "Nice property in a great location. Had a good time overall.",
        "Good stay, clean and comfortable. A few minor issues but nothing major.",
        "Enjoyed our visit. The place was as described and the host was helpful.",
        "Solid choice for the price. Would stay again.",
        "Pleasant stay with good amenities. Recommended!",
        "Good value for money. Location was convenient.",
        "Had a nice time. Property was clean and comfortable.",
        "Decent place, met our needs for the trip.",
    ]

    # Add reviews to properties
    properties = Property.objects.all()
    review_count = 0

    for property in properties:
        # Add 2-4 reviews per property
        num_reviews = randint(2, 4)
        selected_guests = choice([guests[:num_reviews], guests[-num_reviews:]])

        for guest in selected_guests[:num_reviews]:
            # Skip if review already exists
            if Review.objects.filter(review_property=property, user=guest).exists():
                continue

            # Randomly assign ratings (more likely to be positive)
            rating = choice([5, 5, 5, 4, 4, 3])

            if rating == 5:
                comment = choice(positive_comments)
            elif rating == 4:
                comment = choice(positive_comments + good_comments)
            else:
                comment = choice(good_comments)

            review = Review.objects.create(
                review_property=property,
                user=guest,
                rating=rating,
                comment=comment
            )

            print(f"Added {rating}-star review for '{property.name}' by {guest.first_name} {guest.last_name}")
            review_count += 1

    print(f"\nTotal reviews created: {review_count}")

    # Display summary
    print("\n=== Reviews Summary ===")
    for property in properties:
        reviews = property.reviews.all()
        avg_rating = property.average_rating
        print(f"{property.name}: {reviews.count()} reviews, Avg Rating: {avg_rating:.1f}")

if __name__ == "__main__":
    create_sample_reviews()
