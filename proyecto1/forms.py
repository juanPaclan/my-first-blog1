from django import forms
from .models import Cliente

class CliForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('usuario','password', 'nombre', 'apellidos', 'direccion', 'telefono', 'email',)
        widgets = {'password': forms.PasswordInput()}
class LoginForm(forms.Form):
    name_user = forms.CharField(max_length=20,label="",
        widget = (forms.TextInput(attrs={"placeholder":"Nombre de usuario","class":"input-login"})))
    password_user = forms.CharField(max_length=20, label="",
        widget = (forms.PasswordInput(attrs={"placeholder":"Password", "class":"input-login"})))
