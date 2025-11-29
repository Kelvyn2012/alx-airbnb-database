from django.contrib import admin
from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'host', 'location', 'pricepernight', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at', 'location']
    search_fields = ['name', 'description', 'location']
    ordering = ['-created_at']
    inlines = [PropertyImageInline]


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ['property', 'is_primary', 'created_at']
    list_filter = ['is_primary', 'created_at']
