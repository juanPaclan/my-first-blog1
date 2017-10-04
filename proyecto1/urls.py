from django.conf.urls import url
from proyecto1.views import (
    pro1, articulo, desc_arti,
    cliente_detalle, cliente_new , cli_editar, login,
    logout_view, compra_articulo,carrito,
    ArticulosListView,
    ArticulosDetailView,
    IndexListView)
from proyecto1.models import Articulo
urlpatterns = [
    url(r'^producto/$', IndexListView.as_view(), name='index'),
    url(r'^producto/(?P<tipo>[\w-]+)/$', ArticulosListView.as_view() ,name='articulo'),
#    url(r'^producto/(?P<pk>[^/]+)/$', ArticulosDetailView.as_view(), name='desc_arti'),
#antes
    url(r'^compras/$', carrito, name='carrito'),
    #url(r'^producto/$', pro1, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^producto/index/$', logout_view, name='logout_view'),
#    url(r'^producto/(?P<tipo>[^/]+)$', articulo,{'model': Articulo}, name='articulo'),
    url(r'^producto/registro/$', cliente_new, name= 'cli_new'),
    url(r'^producto/(?P<tipo>[^/]+)/$', desc_arti,{'model': Articulo}, name='desc_arti'),
    url(r'^registro/(?P<pk>[0-9]+)/$', cliente_detalle, name= 'cli_deta'),
    url(r'^producto/(?P<id_prod>[^/]+)/compra/$', compra_articulo, name='compra_articulo'),
    url(r'^producto/(?P<users>[^/]+)/edit/$', cli_editar, name='cli_edit'),


]
