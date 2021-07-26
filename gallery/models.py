from django.db import models
import uuid

from django.db.models.aggregates import Max

def photo_path(instance, filename):
    return '{0}/{1}.jpg'.format(instance.catalog.id, instance.id)
def cover_path(instance, filename):
    return 'covers/{0}.jpg'.format(instance.id)


# Create your models here.
class Catalog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cover = models.ImageField(upload_to=cover_path)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to=photo_path, null=True)
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    message = models.TextField