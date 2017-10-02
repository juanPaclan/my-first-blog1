from django import forms
from .models import Cliente

class CliForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('usuario','password', 'nombre', 'apellidos', 'direccion', 'telefono', 'email',)
        widgets = {
            'usuario': forms.TextInput(attrs={"placeholder":"Nombre de usuario","pattern":"^[A-Za-z0-9]{5,10}$","title":"Solo se puede utilazar numeros y letras, minimo 5 y maximo 10"}),
            'password': forms.PasswordInput(attrs={"placeholder":"Password","pattern":"[A-Za-z0-9]{4,10}","title":"Solo se puede utilazar numeros y letras, minimo 4 y maximo 10"}),
            'nombre': forms.TextInput(attrs={"placeholder":"Nombres","pattern":"^([A-Za-z]{4,10}|[A-Za-z]{4,10}\s?[A-Za-z]{4,10})$","title":"Solo se puede poner dos nombres"}),
            'apellidos': forms.TextInput(attrs={"placeholder":"Ingrese sus dos apellidos","pattern":"^[A-Za-z]{4,10}\s?[A-Za-z]{4,10}?$","title":"Tiene que poner dos sus dos apellidos"}),
            'direccion': forms.TextInput(attrs={"pattern":"^(\w|\s){4,30}$"}),
            'telefono': forms.TextInput(attrs={"placeholder":"99-99-99","pattern":"^(\d|-){4,15}$"}),
            'email': forms.TextInput(attrs={"placeholder":"exen@exen.com","pattern":"^.*@.*\.com$"})}
class LoginForm(forms.Form):
    name_user = forms.CharField(max_length=20,label="",
        widget = (forms.TextInput(attrs={"placeholder":"Nombre de usuario","class":"input-login","pattern":"^[A-Za-z0-9]{5,10}$","title":"Solo se puede utilazar numeros y letras, minimo 5 y maximo 10"})))
    password_user = forms.CharField(max_length=20, label="",
        widget = (forms.PasswordInput(attrs={"placeholder":"Password", "class":"input-login", "pattern":"[A-Za-z0-9]{4,10}","title":"Solo se puede utilazar numeros y letras, minimo 4 y maximo 10"})))
