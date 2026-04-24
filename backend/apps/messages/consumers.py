import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message
from apps.users.models import User


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Reject unauthenticated connections
        user = self.scope.get('user')
        if not user or not user.is_authenticated:
            await self.close(code=4001)
            return

        self.authenticated_user = user

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
            recipient_id = text_data_json['recipient_id']
        except (json.JSONDecodeError, KeyError):
            await self.send(text_data=json.dumps({'error': 'Invalid message format'}))
            return

        # Always use the authenticated user as sender — never trust client-supplied sender_id
        sender_id = str(self.authenticated_user.user_id)

        saved = await self.save_message(sender_id, recipient_id, message)
        if not saved:
            await self.send(text_data=json.dumps({'error': 'Recipient not found'}))
            return

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': sender_id
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender_id = event['sender_id']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender_id': sender_id
        }))

    @database_sync_to_async
    def save_message(self, sender_id, recipient_id, message_body):
        try:
            sender = User.objects.get(user_id=sender_id)
            recipient = User.objects.get(user_id=recipient_id)
        except User.DoesNotExist:
            return False
        Message.objects.create(
            sender=sender,
            recipient=recipient,
            message_body=message_body
        )
        return True
