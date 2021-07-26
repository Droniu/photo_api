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

@api_view(['POST'])
def handleContactForm(request):
    if request.method == 'POST':
        if (request.POST['phone'] == ""):
            send_mail(
                    'Message from droniu.pl',
                    formatEmail(request.POST['name'], request.POST['email'], request.POST['message']),
                    None,
                    ['dron.official@yahoo.com'],
                    fail_silently=False,
            )
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)