from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
# Create your views here.
def hola(request):
    return HttpResponse("Hola mundo")
def fecha_actual(request):
    ahora = datetime.datetime.now()
    return render(request, 'prueba/fecha.html', {'fecha_actual': ahora})
def horas_adelante(request, offset):
    try:
        offset= int(offset)
    except ValueError:
        raise Http404()
    dt= datetime.datetime.now()+ datetime.timedelta(hours = offset)
    #assert False
    return render(request, 'prueba/horas_adelante.html', {'horas_adelante': dt, 'hours': offset})
