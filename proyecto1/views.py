from django.shortcuts import render
from django.http import HttpResponse, Http404
from proyecto1.models import Articulo
import datetime
# Create your views here.
def pro1(request):
    articulo = Articulo.objects.filter(producto='CELULAR').order_by('?')[:4]
    articulo1 = Articulo.objects.filter(producto='CELULAR').order_by('?')[:4]
    articulo2 = Articulo.objects.filter(producto='CELULAR').order_by('?')[:4]
    dato = [articulo,articulo1, articulo2]
    return render(request, 'index.html',{ 'datos':dato})
def articulo(request, model, tipo):
    datos_articulo = model.objects.filter(producto=tipo)
    dato = tipo
    return render(request,'cel.html', {'datos':dato,'datos_articulos':datos_articulo})
def desc_arti(request,model, tipo):
    desc_dato = model.objects.filter(modelo=tipo)
    dato = tipo
    return render(request, 'cel-desc.html', {'datos':dato, 'desc_datos': desc_dato})
