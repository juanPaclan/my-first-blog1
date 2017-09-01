from django import forms
from .models import Cliente

class CliForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('usuario','password', 'nombre', 'apellidos', 'direccion', 'telefono', 'email',)
