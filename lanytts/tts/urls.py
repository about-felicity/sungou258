from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('generate_speech/', views.generate_speech, name='generate_speech'),
    #path('upload_mp3/', views.upload_mp3, name='upload_mp3'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)