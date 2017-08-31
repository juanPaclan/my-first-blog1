from django.shortcuts import render
from django.http import HttpResponse, Http404
from proyecto1.models import Articulo
import datetime
# Create your views here.
def pro1(request):
    articulo = Articulo.objects.all()
    return render(request, 'index.html',{'articulos': articulo})
def articulo(request, model, tipo):
    datos_articulo = model.objects.filter(producto=tipo)
    dato = tipo
    return render(request,'cel.html', {'datos':dato,'datos_articulos':datos_articulo})
def desc_arti(request,model, tipo):
    desc_dato = model.objects.filter(modelo=tipo)
    dato = tipo
    return render(request, 'cel-desc.html', {'datos':dato, 'desc_datos': desc_dato})
