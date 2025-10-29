from django.shortcuts import render

# Create your views here.
def servicios_view(request):
    """
    Vista para listar los servicios. Respeta los estilos del sitio extendiendo `base.html`.
    Recibe:
        - request: HttpRequest
    Devuelve:
        - HttpResponse con el template `core/servicios.html` y un contexto con la lista de servicios.
    """
    servicios = [
            {"nombre": "Lavado exterior", "precio": 8000},
            {"nombre": "Lavado completo", "precio": 14000},
            {"nombre": "Limpieza de tapizados", "precio": 35000}
  ]
    context = {"servicios": servicios}
    return render(request, "servicios/servicios.html", context)
