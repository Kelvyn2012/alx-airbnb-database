from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['review_id', 'review_property', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['review_property__name', 'user__email', 'comment']
    ordering = ['-created_at']
