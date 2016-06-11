from django.shortcuts import render, redirect
from push_notifications.models import GCMDevice

from usuarios.models import Ciudadano


def registro(request, id, nombre, apellido, direccion, telefono, mail, id_dispositivo):
    dispositivo = GCMDevice(name='device', user=None, device_id=1, registration_id=id_dispositivo)
    dispositivo.save()
    p = Ciudadano(id=id, nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono, mail=mail, dispositivo=dispositivo)
    p.save()
    return redirect('/')
