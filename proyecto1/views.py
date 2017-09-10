from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from proyecto1.models import Articulo, Cliente, Venta
from .forms import CliForm, LoginForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout, login as django_login
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from datetime import datetime
#from django.template import RequestContext


# Create your views here.
def pro1(request):
    url = request.build_absolute_uri()
    print('>>>>>>>>>>>>>>>'+url)
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
########################################
@login_required
def carrito(request):
    if request.user.is_authenticated:
        usuario= Cliente.objects.get(usuario=request.user)
        datos_carrito = Venta.objects.filter(cliente=usuario)
        return render(request, 'compras.html',{'datos_carritos': datos_carrito} )

@login_required
def compra_articulo(request, id_prod):
    if request.user.is_authenticated:
        fecha = datetime.now()
        formato = "%d/%m/%y"
        dato= fecha.strftime(formato)
        producto= Articulo.objects.get(id=id_prod)
        usuario =Cliente.objects.get(usuario=request.user)
        venta = Venta(fecha=fecha, cliente=usuario)#p)
        venta.save()
        venta.articulos.add(producto)
        venta.save()
        print(venta)
    return render(request, 'index.html' )
def logout_view(request):
    logout(request)
    return render(request, 'index.html' )
def login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        nombre_usuario = data.get("name_user")
        password_usuario = data.get("password_user")
        acceso= authenticate(username=nombre_usuario, password=password_usuario)
        if acceso is not None and acceso.is_active:
            users = User.objects.filter(username = nombre_usuario)
            token, created = Token.objects.get_or_create(user=users)
            print(users, token.key)
            sesion = request.session['member_id']=token.key
            django_login(request, acceso)
        #    context = RequestContext(request,{'usuario': nombre_usuario })
            #t = loader.get_template('index.html')
            return render(request, 'index.html', {'accesos':acceso})
        else:
            return HttpResponse("Usuario /password incorrectos.")
    else:
        form = LoginForm()
    var = { "form":form}
    return render(request, 'login.html', var)

def cliente_detalle(request, pk):
    dato = get_object_or_404(Cliente, pk = pk)
    #nombre = dato.usuario
    return render(request, 'cli-date.html', {'datos' : dato})

def cliente_new(request):
    if request.method == "POST":
        form = CliForm(request.POST)
        if form.is_valid():
            post = form.save(commit= False)
            post.save()
            user= User.objects.create_user(username=post.usuario, email=post.email, password=post.password)
            user.save()
            return redirect('cli_deta', pk=post.pk)
    else:
        form = CliForm()
    return render(request, 'registro.html', {'form': form})

def cli_edit(request, pk):
     post = get_object_or_404(Post, pk = pk)
     if request.method == "POST":
         form = CliForm(request.POST, instance= post)
         if form.is_valid():
             post = form.save(commit= False)
             post.save()
             return redirect('cli_deta', pk= post.pk)
     else:
         form = CliForm(instance= post)
     return render(request, 'regidtro.html', {'form': form})
