from django.conf.urls import url
from proyecto1.views import pro1, articulo
from proyecto1.models import Articulo
urlpatterns = [
# Ejemplos:
# url(r'^$', 'misitio.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
    url(r'^pro1/$', pro1),
    url(r'^cel/$', articulo,{'model': Articulo}),

]
