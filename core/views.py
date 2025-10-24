from django.shortcuts import render
from datetime import date

# 🔹 Function-Based View para la página de inicio
def home_view(request):
    """
    Vista principal (home) del sitio Lavadero Móvil.
    Recibe un request, prepara datos y renderiza el template.
    """
    context = {
        "titulo": "Lavadero Móvil",
        "subtitulo": "Lavados a domicilio en Jujuy",
        "hoy": date.today(),
        "servicios_destacados": [
            {"nombre": "Lavado exterior", "precio": 6000},
            {"nombre": "Lavado completo", "precio": 12000},
            {"nombre": "Limpieza de tapizados", "precio": 18000},
        ]
    }
    # render(request, template, contexto)
    # Parámetros y tipos esperados por django.shortcuts.render:
    # - request: objeto HttpRequest (instancia enviada por Django al llamar la view).
    # - template: string con la ruta/nombre del template (por ejemplo "core/home.html").
    # - context (opcional): diccionario Python (dict) con pares clave:valor que estarán
    #   disponibles en el template. Puede ser None o un dict vacío. Los valores dentro
    #   del dict pueden ser cualquier tipo serializable por Django en templates
    #   (strings, números, fechas, listas, dicts, QuerySets, objetos, etc.).
    # La función devuelve un objeto HttpResponse ya renderizado.
    return render(request, "core/home.html", context)


