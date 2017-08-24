from django.shortcuts import render
from django.http import HttpResponse
from biblioteca.models import Libro

# Create your views here.
def lista_objetos(request, model):
    lista_objetos = model.objects.all()
    print(lista_objetos)
    plantilla = 'biblioteca/%s_lista.html' % model.__name__.lower()
    return render(request, plantilla, {'lista_objetos': lista_objetos})

def formulario_buscar(request):
    return render(request, 'biblioteca/formulario_buscar.html')

def buscar(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Por favor introdusca un termino de busquda.')
        elif len(q)> 10:#se utiliza este elif para delimitar el tama;o de la busqueda
            errors.append('Por favor introdusca un termino de busqueda menor a 10 caracteres.')
        else:
            libros = Libro.objects.filter(titulo__icontains=q)
            return render(request, 'biblioteca/resultados.html', {'libros': libros, 'query': q})
    return render(request, 'biblioteca/formulario_buscar.html', {'errors':errors })
