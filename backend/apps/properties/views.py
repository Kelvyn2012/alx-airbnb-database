from rest_framework import generics, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Property, PropertyImage
from .serializers import (
    PropertySerializer,
    PropertyCreateSerializer,
    PropertyListSerializer,
    PropertyImageSerializer
)


class PropertyListView(generics.ListAPIView):
    queryset = Property.objects.filter(is_active=True)
    serializer_class = PropertyListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['location', 'bedrooms', 'bathrooms']
    search_fields = ['name', 'description', 'location', 'amenities']
    ordering_fields = ['pricepernight', 'created_at']
    ordering = ['-created_at']


class PropertyCreateView(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)


class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'property_id'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.host != request.user:
            return Response(
                {'error': 'You do not have permission to edit this property'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.host != request.user:
            return Response(
                {'error': 'You do not have permission to delete this property'},
                status=status.HTTP_403_FORBIDDEN
            )
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MyPropertiesView(generics.ListAPIView):
    serializer_class = PropertyListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Property.objects.filter(host=self.request.user)


class PropertyImageUploadView(generics.CreateAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        property_id = self.kwargs.get('property_id')
        property_obj = Property.objects.get(property_id=property_id)

        if property_obj.host != self.request.user:
            return Response(
                {'error': 'You do not have permission to add images to this property'},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer.save(property=property_obj)
