from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Photo, Catalog
from .serializers import PhotoSerializer, CatalogSerializer
from gallery import serializers

class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    lookup_field = 'id'
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = PhotoSerializer
    
class PhotoDetail(generics.RetrieveDestroyAPIView):
    queryset = Photo.objects.all()
    lookup_field = 'id'
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = PhotoSerializer
    
class CatalogList(generics.ListCreateAPIView):
    queryset = Catalog.objects.all()
    lookup_field = 'id'
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = CatalogSerializer

class CatalogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalog.objects.all()
    lookup_field = 'id'
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = CatalogSerializer