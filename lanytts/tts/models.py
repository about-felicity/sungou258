'''
from django.db import models

class MP3File(models.Model):
    file = models.BinaryField()  # 存储 MP3 文件的二进制数据
    uploaded_at = models.DateTimeField(auto_now_add=True)  # 上传时间

    def __str__(self):
        return f"File uploaded at {self.uploaded_at}"
'''
