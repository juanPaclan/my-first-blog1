from django import forms

class FormularioContactos(forms.Form):
    asunto = forms.CharField(max_length=100, min_length=10)
    email = forms.EmailField(required = False, label='Tu correo electronico')#required hace el campo opcional
    mensaje = forms.CharField(widget=forms.Textarea)#crea una caja de texto
#Piensa en las clases Field como las encargadas de la lógica de validación , mientras
#que los widgets se encargan de la lógica de presentación .
#validacion con clean_mesaje
def clean_mesaje(self):
    mensaje = self.cleaned_data['mensaje']
    num_palabras = len(mensaje.split())
    if num_palabras < 4:
        raise form.validationError("Se requieren minimo 4 palabras")
    return mensaje
