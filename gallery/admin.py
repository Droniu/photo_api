from django.contrib import admin

# Register your models here.
from .models import Catalog, Photo

class PhotoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Catalog)
admin.site.register(Photo, PhotoAdmin)