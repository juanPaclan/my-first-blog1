from django.shortcuts import render
from django.http import HttpResponse, Http404
from proyecto1.models import Articulo
import datetime
# Create your views here.
def pro1(request):
    return render(request, 'index.html')
def articulo(request, model):
    datos_articulo = model.objects.all()
    print(datos_articulo)
    return render(request,'cel.html', {'datos_articulos':datos_articulo})
