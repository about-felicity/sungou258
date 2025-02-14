# tts/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from fish_audio_sdk import Session, TTSRequest
from django.conf import settings
import os


def home(request):
    return render(request, 'model_output.html')


def generate_speech(request):
    # 从 GET 请求获取用户输入的文本
    text = request.GET.get('text', None)  # 获取 'text' 参数，如果没有则为 None

    if not text:
        return JsonResponse({
            'success': False,
            'error_message': 'No text provided.'
        })

    session = Session("9ed7aa73658d4c168f83030cca4a80bf")  # 用你自己的 API key 替换

    try:
        # 设置音频文件的保存路径
        audio_path = os.path.join(settings.MEDIA_ROOT, 'output1.mp3')

        # 调用 TTS API 并生成语音文件
        with open(audio_path, "wb") as f:
            for chunk in session.tts(TTSRequest(
                reference_id="e80ea225770f42f79d50aa98be3cedfc",  # 用你选择的模型 ID
                text=text  # 用户输入的文本
            )):
                f.write(chunk)

        # 返回音频文件的 URL
        audio_url = os.path.join(settings.MEDIA_URL, 'output1.mp3')

        return JsonResponse({
            'success': True,
            'audio_url': audio_url  # 返回音频文件的 URL
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error_message': str(e)
        })

