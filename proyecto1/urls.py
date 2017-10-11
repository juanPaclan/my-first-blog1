from django.conf.urls import url
from proyecto1.views import (
    cliente_detalle, cliente_new ,
    #cli_editar,
    logout_view,
    compra_articulo,
    ArticulosListView,
    CompraArticulo,
    ArticulosDetailView,
    ClienteNuevo,
    VentasListView,
    ClenteUpdate,
    LoginView,
    login,
    DetalleCliente,
    IndexListView)
from proyecto1.models import Articulo
urlpatterns = [
    url(r'^producto/$', IndexListView.as_view(), name='index'),
    url(r'^producto/(?P<tipo>[\w-]+)/$', ArticulosListView.as_view() ,name='articulo'),
    url(r'^producto/detalle/(?P<tipo>[a-zA-Z0-9-\s]+)/$', ArticulosDetailView.as_view(), name='detalle'),
    url(r'^registro/$', ClienteNuevo.as_view(), name= 'registroN'),
    url(r'^registro/(?P<pk>[0-9]+)/$', DetalleCliente.as_view(), name= 'cli_deta'),
    url(r'^producto/(?P<pk>[0-9]+)/edit/$', ClenteUpdate.as_view(), name='cli_edit'),
    url(r'^compras/(?P<usuario>[a-zA-Z0-9]+)/$', VentasListView.as_view(), name='carrito'),
    url(r'^compra/(?P<id_prod>[^/]+)/$', CompraArticulo.as_view(), name='compra_articulo'),
#    url(r'^login/$', LoginView.as_view(), name='login'),
#antes
#    url(r'^carrito/$', carrito, name='carrito'),
    url(r'^login/$', login, name='login'),
    url(r'^index/$', logout_view, name='logout_view'),
    #url(r'^producto/registro/$', cliente_new, name= 'cli_new'),
#    url(r'^registro/(?P<pk>[0-9]+)/$', cliente_detalle, name= 'cli_deta'),
    #url(r'^compra/(?P<id_prod>[^/]+)/$', compra_articulo, name='compra_articulo'),
#    url(r'^producto/(?P<users>[^/]+)/edit/$', cli_editar, name='cli_edit'),

]
