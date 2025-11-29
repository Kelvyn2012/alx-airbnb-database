from rest_framework import serializers
from .models import Message
from apps.users.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'recipient', 'message_body',
                  'is_read', 'sent_at']
        read_only_fields = ['message_id', 'sent_at']


class MessageCreateSerializer(serializers.ModelSerializer):
    recipient_id = serializers.UUIDField()

    class Meta:
        model = Message
        fields = ['recipient_id', 'message_body']
