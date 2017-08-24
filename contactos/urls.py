from django.conf.urls import url
from contactos.views import contactos
urlpatterns = [
# Ejemplos:
# url(r'^$', 'misitio.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
    url(r'^contactos/$', contactos),

]
