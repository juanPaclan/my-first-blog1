from django.shortcuts import render
from django.core.mail import send_mail
#from django.http import HttpResponse
#from django.http import HttpResponseRedirect
from contactos.forms import FormularioContactos

# Create your views here.
def contactos(request):
    if request.method == 'POST':
        form = FormularioContactos(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            send_mail(
                cd['asunto'],
                cd['mensaje'],
                cd.get('email', 'juan@example.com'),
                    ['siteowner@example.com'],
            )
            return HttpResponseRedirect('contactos/gracias/')
    else:
        form = FormularioContactos(initial={'asunto':'Adoro tu sitio', 'email':'exa@example.com'})
    return render(request, 'formulario-contactos.html', {'form': form })
