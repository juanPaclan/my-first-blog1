from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
# Create your views here.
def pro1(request):
    return render(request, 'index.html')
def fecha_actual(request):
    ahora = datetime.datetime.now()
    return render(request, 'prueba/fecha.html', {'fecha_actual': ahora})
# Create your views here.
