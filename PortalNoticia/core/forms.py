from django import forms
from .models import Contacto, Noticia
from django.contrib.auth.forms import UserCreationForm

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre','correo','tipo_consulta','asunto','mensaje','avisos']

class form_noticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['fecha_publicacion','titulo', 'categoria', 'cuerpo', 'imagen', 'nuevo']

class CustomUserCreationForm(UserCreationForm):
    pass