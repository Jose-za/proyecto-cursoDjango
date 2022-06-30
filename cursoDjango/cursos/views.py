from django.shortcuts import render
from .models import Cursos

# Create your views here.

def cursos(request):
    cursos=Cursos.objects.all()
    return render(request, "cursos/principal.html", {'cursos':cursos})
#Indicamos el lugar donde se renderizará el resultado de esta vista