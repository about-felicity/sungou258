from django.urls import path
from . import consumers
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    # 你的 WebSocket 连接路径
    path("ws/chat/", consumers.ChatConsumer.as_asgi()),
    
]