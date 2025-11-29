from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from .models import Booking
from .serializers import (
    BookingSerializer,
    BookingCreateSerializer,
    BookingUpdateSerializer
)
from apps.properties.models import Property


class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        property_id = serializer.validated_data['property_id']
        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']
        guests = serializer.validated_data['guests']

        try:
            property_obj = Property.objects.get(property_id=property_id)
        except Property.DoesNotExist:
            return Response(
                {'error': 'Property not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Check availability
        overlapping = Booking.objects.filter(
            booking_property=property_obj,
            status__in=['pending', 'confirmed']
        ).filter(
            Q(start_date__lte=end_date) &
            Q(end_date__gte=start_date)
        )

        if overlapping.exists():
            return Response(
                {'error': 'Property is not available for selected dates'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Calculate total price
        nights = (end_date - start_date).days
        total_price = property_obj.pricepernight * nights

        booking = Booking.objects.create(
            booking_property=property_obj,
            user=request.user,
            start_date=start_date,
            end_date=end_date,
            guests=guests,
            total_price=total_price,
            status='pending'
        )

        return Response(
            BookingSerializer(booking).data,
            status=status.HTTP_201_CREATED
        )


class BookingDetailView(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    lookup_field = 'booking_id'
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return BookingUpdateSerializer
        return BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(
            Q(user=self.request.user) | Q(property__host=self.request.user)
        )


class HostBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(property__host=self.request.user)
