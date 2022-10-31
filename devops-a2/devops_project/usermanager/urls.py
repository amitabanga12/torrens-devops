from django.urls import path
from usermanager import views

urlpatterns = [
    path("add/", views.add_user, name="add_user"),
    path("list/", views.list_users, name="list_users"),
]
