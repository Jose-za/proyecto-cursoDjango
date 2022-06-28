from django.shortcuts import render, HttpResponse

# Create your views here.



def paginaPrincipal(request):
    
    return render( request, "inicio/principal.html")

def cursos(request):
    return render( request, "inicio/cursos.html")
    
def contacto(request):
    return render( request, "inicio/contacto.html")