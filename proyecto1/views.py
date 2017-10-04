#nuevo
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, FormView
from django.core.urlresolvers import reverse
#login
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

#antes
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

class IndexListView(ListView):
    """Es el index de la paguina con una lista de articulor """
    model = Articulo
    context_object_name = "list_producto"
    template_name = "index.html"

    def get_queryset(self, *args, **kwargs):
        articulos = {'CELULAR', 'COMPUTADORA', 'TABLET' }
        queryset= []
        for x in articulos:
            articulo= Articulo.objects.filter(producto=x).order_by('?')[:4]
            queryset.append(articulo)
        return queryset

#vista de articulos
class ArticulosListView(ListView):
    """Muestra las plantillas de los articulos"""
    model= Articulo
    context_object_name = "datos_articulos"
    template_name = "cel.html"
    def get_queryset(self, *args, **kwargs):
        return Articulo.objects.filter(producto= self.kwargs['tipo'])
    def get_context_data(self, *args, **kwargs):
        context= super(ArticulosListView, self).get_context_data(**kwargs)
        context['datos'] = self.kwargs['tipo']
        return context

class ArticulosDetailView(ArticulosListView, ListView ):
    """Muestra el detalle de los articulos recibiendo el tipo de articulo o categoria """
    model = Articulo
    context_object_name = "desc_datos"
    template_name = "cel-desc.html"
    def get_queryset(self, *args, **kwargs):
        return Articulo.objects.filter(modelo= self.kwargs['tipo'])

class DetalleCliente(DetailView):
    model= Cliente
    template_name = "cli-date.html"

class ClienteNuevo(CreateView):
    form_class = CliForm
    template_name = "registro.html"

class Login(FormView):

    template_name= 'login.html'
    form_class = AuthenticationForm
    success_url =  reverse_lazy("index")
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)
    # def form_valid(self, form):
    #     login(self.request, form.get_user())
    #     return super(Login, self).form_valid(form)

# Create your views here.
def desc_arti(request,model, tipo):
    desc_dato = model.objects.filter(modelo=tipo)
    dato = tipo
    return render(request, 'cel-desc.html', {'datos':dato, 'desc_datos': desc_dato})


def pro1(request):
    url = request.build_absolute_uri()
    articulo = Articulo.objects.filter(producto='CELULAR').order_by('?')[:4]
    articulo1 = Articulo.objects.filter(producto='CELULAR').order_by('?')[:4]
    articulo2 = Articulo.objects.filter(producto='TABLET').order_by('?')[:4]
    dato = [articulo,articulo1, articulo2]
    return render(request, 'index.html',{ 'rutas':url, 'datos':dato})

def articulo(request, model, tipo):
    datos_articulo = model.objects.filter(producto=tipo)
    dato = tipo.lower()
    return render(request,'cel.html', {'datos':dato,'datos_articulos':datos_articulo})

########################################
@login_required
def carrito(request):
    if request.user.is_authenticated:
        usuario= Cliente.objects.get(usuario=request.user)
        datos_carrito = Venta.objects.filter(cliente=usuario)
        total_venta= datos_carrito.count
        total=0
        for datos in datos_carrito:
            for precio_totales in datos.articulos.all():
                total+=precio_totales.precio
        return render(request, 'compras.html',{ 'totales':total,'total_vetas':total_venta ,'datos_carritos': datos_carrito} )

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
        #    users = User.objects.filter(username = nombre_usuario)
        #    token, created = Token.objects.get_or_create(user=users)
        #    print(users, token.key)
        #    sesion = request.session['member_id']=token.key
            django_login(request, acceso)
            return render(request, 'index.html', {'accesos':acceso})
            #return redirect('logout_view')
        else:
            return HttpResponse("Usuario /password incorrectos.")
    else:
        form = LoginForm()
    var = { "form":form}
    return render(request, 'login.html', var)

def cliente_detalle(request, pk):
    dato = get_object_or_404(Cliente, pk =pk)
    nombre = dato.usuario
    return render(request, 'cli-date.html', { 'nombres':nombre ,'datos' : dato})

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

def cli_editar(request, users):
    post = get_object_or_404(Cliente, usuario=users)
    if request.method == "POST":
        form = CliForm(request.POST, instance= post)
        if form.is_valid():
            post = form.save(commit= False)
            post.save()
            return redirect('cli_deta', pk= post.pk)
    else:
        form = CliForm(instance= post)
    return render(request, 'registro.html', {'form': form})
