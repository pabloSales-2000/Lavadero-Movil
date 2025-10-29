from django.urls import path
from .views import galeria_view

app_name = "galeria"  # namespace de la app

urlpatterns = [
    path("galeria/", galeria_view, name="galeria"),  
]