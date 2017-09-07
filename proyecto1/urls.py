from django.conf.urls import url
from proyecto1.views import pro1, articulo, desc_arti, cliente_detalle, cliente_new , cli_edit, login, logout_view
from proyecto1.models import Articulo
urlpatterns = [
# Ejemplos:
# url(r'^$', 'misitio.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
    url(r'^producto/$', pro1, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^producto/index/$', logout_view, name='logout_view'),
    url(r'^producto/(?P<tipo>[^/]+)$', articulo,{'model': Articulo}, name='articulo'),
    url(r'^producto/registro/$', cliente_new, name= 'cli_new'),
    url(r'^producto/(?P<tipo>[^/]+)/$', desc_arti,{'model': Articulo}, name='desc_arti'),
    url(r'^registro/(?P<pk>[0-9]+)/$', cliente_detalle, name= 'cli_deta'),
    url(r'^producto/(?P<pk>[0-9]+)/edit/$', cli_edit, name='cli_edit'),


]
