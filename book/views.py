from django.views.generic import DetailView
from book.models import Publisher, Book
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "book/about.html"
    
class PublisherDetailView(DetailView):

    context_object_name = "publisher"
    model = Publisher

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(PublisherDetailView, self).get_context_data(**kwargs)
        # Agregamos un QuerySet de todos los books
        context['book_list'] = Book.objects.all()
        return context
