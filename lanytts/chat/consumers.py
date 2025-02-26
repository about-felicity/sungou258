import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.room_name = f"chat_{self.user.id}"
        self.room_group_name = f"chat_{self.user.id}"

        # 加入聊天房间
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # 离开房间
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        receiver_username = data["receiver"]
        content = data["content"]

        # 获取接收者用户
        receiver = User.objects.get(username=receiver_username)

        # 保存消息到数据库
        message = Message.objects.create(sender=self.user, receiver=receiver, content=content)

        # 将消息发送到房间
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": content,
                "sender": self.user.username,
                "receiver": receiver.username,
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]
        receiver = event["receiver"]

        # 发送消息到 WebSocket
        await self.send(text_data=json.dumps({
            "message": message,
            "sender": sender,
            "receiver": receiver,
        }))
