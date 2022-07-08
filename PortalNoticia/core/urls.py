from django.urls import path, include
from .views import NoticiaViewset, CategoriaViewset, \
    administrador, eliminar_mensaje, eliminar_noticia, \
    escribir_noticia, home, contacto, listar_noticia, mensaje_contacto, plantilla1, plantilla2, plantilla3, plantilla4, plantilla5, plantilla6, plantilla7, plantilla8, plantilla9, registrar, ver_noticia
from rest_framework import routers

router = routers.DefaultRouter()
router.register('noticia', NoticiaViewset)
router.register('categoria', CategoriaViewset)

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('administrador/', administrador, name="administrador"),
    path('listar_noticia/', listar_noticia, name="listar_noticia"),
    path('escribir_noticia/', escribir_noticia, name="escribir_noticia"),
    path('eliminar_noticia/<id>/', eliminar_noticia, name="eliminar_noticia"),
    path('registrar/', registrar, name="registrar"),
    path('mensaje_contacto', mensaje_contacto, name='mensaje_contacto'),
    path('eliminar_mensaje/<id>/', eliminar_mensaje, name='eliminar_mensaje'),
    path('api/', include(router.urls)),
    #PLANTILLAS
    path('plantilla1/', plantilla1, name='plantilla1'),
    path('plantilla2/', plantilla2, name='plantilla2'),
    path('plantilla3/', plantilla3, name='plantilla3'),
    path('plantilla4/', plantilla4, name='plantilla4'),
    path('plantilla5/', plantilla5, name='plantilla5'),
    path('plantilla6/', plantilla6, name='plantilla6'),
    path('plantilla7/', plantilla7, name='plantilla7'),
    path('plantilla8/', plantilla8, name='plantilla8'),
    path('plantilla9/', plantilla9, name='plantilla9'),
    path('ver_noticia/', ver_noticia, name='ver_noticia')
]
