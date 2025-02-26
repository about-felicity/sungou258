from django.shortcuts import render
from .models import Message

def chat_view(request):
    # 获取所有消息
    messages = Message.objects.all()
    return render(request, 'chat_message.html', {'messages': messages})
