from django.contrib import admin

from core.models import Categoria, Contacto, Noticia

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Contacto)
