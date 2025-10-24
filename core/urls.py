from django.urls import path
from .views import home_view  # importamos nuestra función de vista

app_name = "core"  # namespace de la app

urlpatterns = [
    path("", home_view, name="home"),  # muestra el home ,significa: cuando la URL es /, ejecutá home_view.
]                                      # app_name te permite luego llamar la URL así: 
                                       # {% url 'core:home' %} desde cualquier template.
