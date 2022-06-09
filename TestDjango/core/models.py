import email
from django.db import models
from django.forms import EmailField

# Create your models here.


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreCategoria


class Noticia(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    titulo = models.TextField()
    cuerpo = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Periodista(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    nombre = models.TextField()
    apellidos = models.TextField()
    email = models.EmailField(max_length=250)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
