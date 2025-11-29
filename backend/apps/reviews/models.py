import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.users.models import User
from apps.properties.models import Property


class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    review_property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews', db_column='property_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reviews'
        unique_together = ['review_property', 'user']
        indexes = [
            models.Index(fields=['review_property']),
            models.Index(fields=['user']),
        ]

    def __str__(self):
        return f"Review by {self.user.full_name} for {self.review_property.name}"
