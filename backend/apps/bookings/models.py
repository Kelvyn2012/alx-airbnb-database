import uuid
from django.db import models
from django.core.exceptions import ValidationError
from apps.users.models import User
from apps.properties.models import Property


class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    )

    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booking_property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='bookings', db_column='property_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    guests = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bookings'
        indexes = [
            models.Index(fields=['booking_property']),
            models.Index(fields=['user']),
            models.Index(fields=['start_date', 'end_date']),
        ]

    def __str__(self):
        return f"Booking {self.booking_id} - {self.booking_property.name}"

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError('End date must be after start date')

        # Check for overlapping bookings
        overlapping = Booking.objects.filter(
            booking_property=self.booking_property,
            status__in=['pending', 'confirmed']
        ).exclude(booking_id=self.booking_id).filter(
            models.Q(start_date__lte=self.end_date) &
            models.Q(end_date__gte=self.start_date)
        )

        if overlapping.exists():
            raise ValidationError('This property is already booked for the selected dates')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def nights(self):
        return (self.end_date - self.start_date).days
