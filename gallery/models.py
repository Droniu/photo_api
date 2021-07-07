from django.db import models

# Create your models here.
class Photo(models.Model):
    title=models.CharField(max_length=255)
    static_url=models.CharField(max_length=255)