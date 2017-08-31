from django.contrib import admin
from proyecto1.models import Articulo, Cliente, Venta
# Register your models here.
class ArticuloAdmin(admin.ModelAdmin):
    search_fields = ('marca', 'producto')
    filer_horizontal= ('producto')
    list_display = ('producto','marca', 'modelo', 'precio', 'descripcion')

admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Cliente)
admin.site.register(Venta)
