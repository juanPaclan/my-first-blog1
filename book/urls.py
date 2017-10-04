from django.conf.urls import url
from book.views import AboutView
from django.views.generic import ListView
from book.models import Publisher

urlpatterns  =  [
    url (r'^about/$' ,  AboutView.as_view ()),
    url (r'^publishers/$', ListView.as_view(
        model=Publisher,
    )),

]
