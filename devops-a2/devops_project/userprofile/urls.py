from django.urls import path
from userprofile import views

urlpatterns = [
    path("view/", views.view_profile, name="view_profile"),
]
