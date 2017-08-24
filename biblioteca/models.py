from django.db import models

# Create your models here.
class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ['nombre']
        verbose_name_plural='Editores'
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    class Meta:
        verbose_name_plural='Autores'
        ordering = ['nombre']

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor)
    fecha_publicacion = models.DateField(blank=True, null=True)
    portada = models.ImageField(upload_to='portadas')

    def __str__(self):
        return '%s %s %s' % (self.titulo, self.autores, self.portada)
