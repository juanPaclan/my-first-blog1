from django.contrib import admin
from book.models import Author, Publisher, Book

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
