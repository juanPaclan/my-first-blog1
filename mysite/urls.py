from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^router', include(router.urls)),
    url(r'^rest-auth/',include('rest_auth.urls')),
#    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
#    url(r'^api-token-auth/', obtain_jtw_token),
    url(r'', include('prueba.urls')),
    url(r'', include('proyecto1.urls')),
    url(r'', include('biblioteca.urls')),
    #url(r'', include('contactos.urls')),
    #url(r'^admin/', include('django.contrib.admin.urls')),
    url(r'^blog', include('blog.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
