from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d{10})/'
        r'(?P<nombre>[a-zA-Z]{,50})/'
        r'(?P<apellido>[a-zA-Z]{,50})/'
        r'(?P<direccion>\w{4,50})/'
        r'(?P<telefono>\w{10})/'
        r'(?P<mail>.+)/'
        r'(?P<id_dispositivo>.+)/$',
        views.registro, name='registro'),
]
