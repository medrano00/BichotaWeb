from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to="images", null=True)
    fecha_publicacion = models.DateField()
    nuevo = models.BooleanField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo


opciones_consultas = [
    [0, 'Consultas'],
    [1, 'Reclamos'],
    [2, 'Sugerencias']
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.correo
