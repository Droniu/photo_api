from django.db import models
import uuid

def photo_path(instance, filename):
    return '{0}/{1}.jpg'.format(instance.catalog.id, instance.id)
def cover_path(instance, filename):
    return 'covers/{0}.jpg'.format(instance.id)


# Create your models here.
class Catalog(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    cover = models.ImageField(upload_to=cover_path)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)


class Photo(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to=photo_path, null=True)