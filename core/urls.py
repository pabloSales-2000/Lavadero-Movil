from django.urls import path
from .views import home_view, contacto_view  # importamos nuestras funciones de vista

app_name = "core"  # namespace de la app
                   # app_name te permite luego llamar la URL así: 
                   # {% url 'core:home' %} desde cualquier template.

urlpatterns = [
    path("", home_view, name="home"),  # muestra el home ,significa: cuando la URL es /, ejecutá home_view.                                      
    path("contacto/", contacto_view, name="contacto"),    
]                                                        


