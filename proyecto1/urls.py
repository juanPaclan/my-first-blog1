from django.conf.urls import url
from proyecto1.views import pro1, articulo, desc_arti, cli_deta, cli_new #, cli_edit
from proyecto1.models import Articulo
urlpatterns = [
# Ejemplos:
# url(r'^$', 'misitio.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
    url(r'^pro1/$', pro1, name='index'),
    url(r'^pro1/(?P<tipo>[^/]+)$', articulo,{'model': Articulo}, name='articulo'),
    url(r'^pro1/(?P<tipo>[^/]+)/$', desc_arti,{'model': Articulo}, name='desc_arti'),
    url(r'^pro1/(?P<pk>[0-9]+)/$', cli_deta, name= 'cli_deta'),
    url(r'^pro1/new/$', cli_new, name= 'cli_new'),
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', cli_edit, name='cli_edit'),


]
