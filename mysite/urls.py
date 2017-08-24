from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('prueba.urls')),
    url(r'', include('proyecto1.urls')),
    url(r'', include('biblioteca.urls')),
    url(r'', include('contactos.urls')),
    #url(r'^admin/', include('django.contrib.admin.urls')),
    #url(r'', include('blog.urls')),
]
