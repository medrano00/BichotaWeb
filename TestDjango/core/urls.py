from django.urls import path
from .views import home, form_periodista, form_mod_periodista, form_del_periodista

urlpatterns = [
    path('', home, name="home"),
    path('form-vehiculo', form_periodista, name="form_vehiculo"),
    path('form-mod-vehiculo/<id>', form_mod_periodista, name="form_mod_vehiculo"),
    path('form-del-vehiculo/<id>', form_del_periodista, name="form_del_vehiculo"),
]
