from django.urls import path
from django.views.generic.base import TemplateView
from processfiles import views

urlpatterns = [
    path("process/", TemplateView.as_view(template_name='process_files.html'), name='home'),
    path("load/", views.load_file, name="load_file"),
]
