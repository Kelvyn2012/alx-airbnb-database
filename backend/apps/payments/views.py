from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer, PaymentCreateSerializer
from apps.bookings.models import Booking


class PaymentListView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(booking__user=self.request.user)


class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        booking_id = serializer.validated_data['booking_id']

        try:
            booking = Booking.objects.get(booking_id=booking_id)
        except Booking.DoesNotExist:
            return Response(
                {'error': 'Booking not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        if booking.user != request.user:
            return Response(
                {'error': 'You do not have permission to pay for this booking'},
                status=status.HTTP_403_FORBIDDEN
            )

        if booking.status != 'pending':
            return Response(
                {'error': f'Booking cannot be paid — current status is \'{booking.status}\''},
                status=status.HTTP_400_BAD_REQUEST
            )

        if serializer.validated_data['amount'] != booking.total_price:
            return Response(
                {'error': f'Payment amount must equal booking total of {booking.total_price}'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create payment
        payment = Payment.objects.create(
            booking=booking,
            amount=booking.total_price,
            payment_method=serializer.validated_data['payment_method'],
            is_successful=True  # In production, integrate with Stripe/PayPal
        )

        # Update booking status using update() to bypass full_clean overlap check
        Booking.objects.filter(pk=booking.pk).update(status='confirmed')

        return Response(
            PaymentSerializer(payment).data,
            status=status.HTTP_201_CREATED
        )


class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'payment_id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(booking__user=self.request.user)
