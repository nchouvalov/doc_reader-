import os

from django.db import models

def get_upload_path(instance, filename):
    return os.path.join(
      f"upload_{instance.upload_date.strftime('%Y-%m-%d')}", filename)

class Document(models.Model):
    title = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)
    cover = models.FileField(upload_to=get_upload_path)

    def __str__(self):
        return f'Uploaded {self.title} at {self.upload_date}'