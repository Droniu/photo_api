from django.contrib import admin
from .models import Catalog, Photo
# Register your models here.

class PhotoInline(admin.TabularInline):
    model = Photo

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass