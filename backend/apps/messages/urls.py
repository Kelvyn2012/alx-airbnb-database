from django.urls import path
from .views import (
    MessageListView,
    ConversationView,
    MessageCreateView,
    MessageDetailView
)

urlpatterns = [
    path('', MessageListView.as_view(), name='message-list'),
    path('create/', MessageCreateView.as_view(), name='message-create'),
    path('conversation/<uuid:user_id>/', ConversationView.as_view(), name='conversation'),
    path('<uuid:message_id>/', MessageDetailView.as_view(), name='message-detail'),
]
