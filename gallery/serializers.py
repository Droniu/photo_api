from rest_framework import serializers
from .models import Catalog, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            "id",
            "catalog",
            "img"
        ]

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = [
            "id",
            "cover",
            "title",
            "subtitle"
        ]
        extra_kwargs = {
            "subtitle": {"required": False}
        }