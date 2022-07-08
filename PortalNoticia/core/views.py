from django.shortcuts import redirect, render
from core.models import Categoria, Contacto, Noticia
from .forms import ContactoForm, form_noticia, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import CategoriaSerializer, NoticiaSerializer


# Create your views here.

class NoticiaViewset(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer


class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


def home(request):
    noticia = Noticia.objects.all()
    data = {
        'noticia': noticia
    }
    return render(request, 'core/home.html', data)


def administrador(request):
    return render(request, 'core/administracion/administrador.html')


def contacto(request):
    if request.method == 'GET':
        form = ContactoForm()
        contexto = {
            'form': form
        }
    else:
        form = ContactoForm(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid:
            form.save()
    return render(request, 'core/contacto.html', contexto)


def mensaje_contacto(request):
    data = Contacto.objects.all()
    contexto = {
        'data': data
    }
    return render(request, 'core/administracion/mensaje_contacto.html', contexto)


def eliminar_noticia(request, id):
    noticia = Noticia.objects.get(id=id)
    noticia.delete()
    return redirect(to='listar_noticia')


@permission_required('core.add_noticia')
def escribir_noticia(request):
    if request.method == 'GET':
        form = form_noticia()
        contexto = {
            'form': form
        }
    else:
        form = form_noticia(request.POST, files=request.FILES)
        contexto = {
            'form': form
        }
        if form.is_valid:
            form.save()
    return render(request, 'core/escribir_noticia.html', contexto)

# LISTAS


def listar_noticia(request):
    data = Noticia.objects.all()
    contexto = {
        'data': data
    }
    return render(request, 'core/administracion/listar_noticia.html', contexto)

def ver_noticia(request):
    data = Noticia.objects.all()
    contexto = {
        'data': data
    }
    return render(request, 'core/administracion/ver_noticia.html', contexto)

# REGISTRO


def registrar(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        contexto = CustomUserCreationForm(data=request.POST)
        if contexto.is_valid():
            contexto.save()
            user = authenticate(
                username=contexto.cleaned_data['username'], password=contexto.cleaned_data['password1'])
            login(request, user)
            return redirect(to='home')
        data['form'] = contexto
    return render(request, 'registration/register.html', data)


def eliminar_mensaje(request, id):
    mensaje = Contacto.objects.get(id=id)
    mensaje.delete()
    return redirect(to='mensaje_contacto')

# PLANTILLAS


def plantilla1(request):
    return render(request, 'core/plantilla1.html')


def plantilla2(request):
    return render(request, 'core/plantilla2.html')


def plantilla3(request):
    return render(request, 'core/plantilla3.html')


def plantilla4(request):
    return render(request, 'core/plantilla4.html')


def plantilla5(request):
    return render(request, 'core/plantilla5.html')


def plantilla6(request):
    return render(request, 'core/plantilla6.html')


def plantilla7(request):
    return render(request, 'core/plantilla7.html')


def plantilla8(request):
    return render(request, 'core/plantilla8.html')


def plantilla9(request):
    return render(request, 'core/plantilla9.html')
