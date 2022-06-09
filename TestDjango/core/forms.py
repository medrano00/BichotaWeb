from django import forms
from django.forms import ModelForm
from .models import Periodista

class PeriodistaForm(ModelForm):
    class Meta:
        model = Periodista
        fields = ['id','nombre','apellidos','email','noticia']
        