from django.urls import path
from .views import servicios_view # importamos nuestras funciones de vista

app_name = "servicios"  # namespace de la app

urlpatterns = [
    path("servicios/", servicios_view, name="servicios"),
]