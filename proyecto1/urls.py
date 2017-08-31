from django.conf.urls import url
from proyecto1.views import pro1, articulo, desc_arti
from proyecto1.models import Articulo
urlpatterns = [
# Ejemplos:
# url(r'^$', 'misitio.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
    url(r'^pro1/$', pro1, name='index'),
    url(r'^pro1/(?P<tipo>[^/]+)$', articulo,{'model': Articulo}, name='articulo'),
    url(r'^pro1/(?P<tipo>[^/]+)/$', desc_arti,{'model': Articulo}, name='desc_arti'),
    #url(r'^pro1/(?P<pk>[0-9]+)/$', desc_arti,{'model': Articulo}, name='desc_arti'),

]
