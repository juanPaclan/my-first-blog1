from django.db import models

# Create your models here.
PRODUCTO_CHOICES = (('COMPUTADORA','Computadora'),('CELULAR','Celular'),('TABLET','Tablet'))
class Articulo(models.Model):
    producto = models.CharField(max_length=11, choices=PRODUCTO_CHOICES)
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=10)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='articulos')

    class Meta:
        ordering = ['marca']

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.producto, self.marca, self.modelo,self.precio, self.descripcion, self.imagen)

class Cliente(models.Model):
    usuario = models.CharField(max_length=10)
    password= models.CharField(max_length=10)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    direccion = models.CharField(max_length= 30)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(verbose_name='e-mail')

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return '%s %s %s %s %s' % (self.usuario,self.password, self.nombre, self.apellidos, self.email)

class Venta(models.Model):
    fecha = models.DateField(auto_now_add = True)
    cliente = models.ForeignKey(Cliente)
    articulos = models.ManyToManyField(Articulo)

    class Meta:
        ordering = ['cliente']

    def __str__(self):
        return '%s %s' % (self.cliente, self.articulos)
