from django.shortcuts import render, redirect
from .models import Noticia, Periodista
from .forms import PeriodistaForm
# Create your views here.

def home(request):
    lista = Periodista.objects.all()
    contexto = {
        'periodista': lista,
    }
    return render(request, 'core/index.html', contexto)

def form_periodista(request):
    contexto = { 
        'form': PeriodistaForm(),
        }
    if request.method=='POST':
        formulario=PeriodistaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje']='Datos guardados correctamente'
    return render(request, 'core/form-vehiculo.html', contexto)

def form_mod_periodista(request, id):
    periodista = Periodista.objects.get(id=id)
    contexto = { 
        'form': PeriodistaForm(instance=periodista),
        }
    if request.method=='POST':
        formulario=PeriodistaForm(data=request.POST, instance=periodista)
        if formulario.is_valid():
            formulario.save()
            contexto['mensaje']='Datos modificados correctamente'
    return render(request, 'core/form-mod-vehiculo.html', contexto)

def form_del_periodista(request, id):
    periodista = Periodista.objects.get(id=id)
    Periodista.delete()
    return redirect(to="home")

