from django.urls import path
from . import views

urlpatterns = [
    path("photos/", views.PhotoList.as_view()),
    path("photos/<uuid:id>", views.PhotoDetail.as_view()),
    path("catalogs/", views.CatalogList.as_view()),
    path("catalogs/<uuid:id>", views.CatalogDetail.as_view()),
    path("contact/", views.handleContactForm),
]