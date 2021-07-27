from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view

from .models import Photo, Catalog
from .serializers import PhotoSerializer, CatalogSerializer, ContactSerializer

from django.core.mail import send_mail

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

def formatEmail(name, email, message):
    return "From:{email}\nName:{name}\n\n{message}".format(name=name, email=email, message=message)


# i know this is dogshit code but 
# i needed something quickly to focus
# on the frontend
@api_view(['POST'])
def handleContactForm(request):
    if request.method == 'POST':
        if (request.GET.get('phone', "") == ""):
            send_mail(
                    'droniu.pl - Message from ' + request.data['name'],
                    formatEmail(request.data['name'], request.data['email'], request.data['message']),
                    None,
                    ['dron.official@yahoo.com'],
                    fail_silently=False,
            )
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)