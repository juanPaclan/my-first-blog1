from django.contrib import admin
from proyecto1.models import Articulo, Cliente, Venta
# Register your models here.
class ArticuloAdmin(admin.ModelAdmin):
    search_fields = ('marca', 'producto')
    filer_horizontal= ('producto')
    list_display = ('producto','marca', 'modelo', 'precio', 'descripcion')
class ClienteAdmin(admin.ModelAdmin):
    list_display= ('usuario','nombre','apellidos','email','telefono')
class VentaAdmin(admin.ModelAdmin):
    list_display= ('fecha' ,'usuario' ,'cliente_datos')
    filter_horizontal = ('articulos',)
    #list_display_links = ('cliente_datos')
    def cliente_datos(self, obj):
        datos= obj.cliente.nombre +' ' +obj.cliente.apellidos
        return datos
    def usuario(self, obj):
        datos= obj.cliente.usuario
        return datos
    cliente_datos.admin_order_field = 'cliente_datos'
class VentasNAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "modelo":
            kwargs["queryset"]= Articulo.objects.filter(owner=request.user)
        return super(VentasNAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venta,  VentaAdmin)
