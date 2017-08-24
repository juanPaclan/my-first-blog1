from django.conf.urls import url
from biblioteca import views
from biblioteca.models import Libro, Editor, Autor
urlpatterns = [
# Ejemplos:
# url(r'^$', 'misitio.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
    url(r'^formulario_buscar/$', views.formulario_buscar),
    url(r'^buscar/$', views.buscar),
    url(r'^lista_libros/$', views.lista_objetos,{'model': Libro}),
    url(r'^lista_editores/$', views.lista_objetos,{'model': Editor}),

]
