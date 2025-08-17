from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'mensaje']

class FormularioMensaje(forms.Form):
    nombre = forms.CharField(max_length=100)
    correo_electronico = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)