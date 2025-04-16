from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("download-readme/", views.download_readme, name="download_readme"),
]