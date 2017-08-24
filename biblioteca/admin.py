from django.contrib import admin
from biblioteca.models import Editor, Autor, Libro

# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email')
    search_fields=('nombre','apellidos')

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo','editor' ,'fecha_publicacion')#cambia los nombre de los campos en el admin
    list_filter= ('fecha_publicacion',)#crea una lista para filtar por fecha o segun el parametro
    date_hierarchy= 'fecha_publicacion'#otra forma de filtrar per mas sencilla
    ordering = ('-fecha_publicacion',)#ordena los datos segun el parametro que se le pasa
    filter_horizontal = ('autores',)#modifica la caja de relacion cuando es de uno a muchosy
    raw_id_fields = ('editor',)# esta etiqueta solo se utiliza para ForeignKey por el tipo de relacion 
    #fields = ('editor', 'titulo', 'autores', 'fecha_publicacion') #determina el orden del formualario, los campos que no se toman encuemta son ocultados para los usuario
    #filter_vertical=este tipo de etiquetas solo funciona con ManyToManyField por la relacion una a muchas
admin.site.register(Editor)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
