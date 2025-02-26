from django import forms

class MP3UploadForm(forms.Form):
    mp3_file = forms.FileField()  # 定义一个文件上传字段
