from django.urls import path
from . import views

urlpatterns = [
    path("photos/", views.PhotoList.as_view()),
    path("photos/<int:id>", views.PhotoDetail.as_view())
]