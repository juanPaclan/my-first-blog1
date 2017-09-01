from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from proyecto1.models import Articulo, Cliente
from .forms import CliForm
from django.shortcuts import redirect
# Create your views here.
def pro1(request):
    articulo = Articulo.objects.filter(producto='CELULAR').order_by('?')[:4]
    articulo1 = Articulo.objects.filter(producto='CELULAR').order_by('?')[:4]
    articulo2 = Articulo.objects.filter(producto='TABLET').order_by('?')[:4]
    dato = [articulo,articulo1, articulo2]
    return render(request, 'index.html',{ 'datos':dato})
def articulo(request, model, tipo):
    datos_articulo = model.objects.filter(producto=tipo)
    dato = tipo.lower()
    return render(request,'cel.html', {'datos':dato,'datos_articulos':datos_articulo})
def desc_arti(request,model, tipo):
    desc_dato = model.objects.filter(modelo=tipo)
    dato = tipo
    return render(request, 'cel-desc.html', {'datos':dato, 'desc_datos': desc_dato})

def cli_deta(request, pk):
    dato = get_object_or_404(Post, pk = pk)
    nombre = dato.usuario
    return render(request, 'cli-date.html', {'nombre': nombre ,'datos' : dato})
def cli_new(request):
    print('formulario')
    form = CliForm()
    return render(request, 'cli-edic.html', {'form': form})
# def cli_edit(request, pk):
#     post = get_object_or_404(Post, pk = pk)
#     if request.method == "POST":
#         form = CliForm(request.POST, instance= post)
#         if form.is_valid():
#             post = form.save(commit= False)
#             post.save()
#             return redirect('cli_deta', pk= post.pk)
#     else:
#         form = CliForm(instance= post)
#     return render(request, 'cli-edic.html', {'form': form})
