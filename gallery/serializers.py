from rest_framework import serializers
from .models import Catalog, Contact, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

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
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'