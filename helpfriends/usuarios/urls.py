from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d{10})/'
        r'(?P<accion>\d+)/$',
        views.accion, name='accion'
        ),
]
