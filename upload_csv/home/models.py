from django.db import models

# Create your models here.

class UploaderFile(models.Model):
    file = models.FileField(upload_to='uploade_file/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
