from django.conf.urls import url
from proyecto1.views import pro1, articulo, desc_arti, cli_deta, cli_new , cli_edit, login
from proyecto1.models import Articulo
urlpatterns = [
# Ejemplos:
# url(r'^$', 'misitio.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
    url(r'^producto/$', pro1, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^producto/(?P<tipo>[^/]+)$', articulo,{'model': Articulo}, name='articulo'),
    url(r'^producto/registro/$', cli_new, name= 'cli_new'),
    url(r'^producto/(?P<tipo>[^/]+)/$', desc_arti,{'model': Articulo}, name='desc_arti'),
    url(r'^registro/(?P<pk>[0-9]+)/$', cli_deta, name= 'cli_deta'),
    url(r'^producto/(?P<pk>[0-9]+)/edit/$', cli_edit, name='cli_edit'),


]
