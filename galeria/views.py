from django.shortcuts import render

# Create your views here.

def galeria_view(request):
       
       context = {
          
       }

       return render(request, "galeria/galeria.html", context)