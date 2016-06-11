from django.db import models
from push_notifications.models import GCMDevice


class Persona(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10)
    mail = models.EmailField()

    def __str__(self):
        return self.id + " " + self.apellido + " " + self.nombre


class Voluntario(Persona):
    dispositivo = models.ForeignKey(GCMDevice)


class Ciudadano(Voluntario):
    conocimiento_priemerosaux = models.BooleanField(default=False)


class TrabajadorPublico(Voluntario):
    institucion = models.CharField(max_length=250)
    especialidad = models.CharField(max_length=250)


class Discapacidad(models.Model):
    tipo = models.CharField(max_length=250)

    def __str__(self):
        return self.tipo


class PCE(Persona):
    discapacidad = models.ForeignKey(Discapacidad)
    porcentaje = models.FloatField()

    def __str__(self):
        return Persona.__str__(self) + " - " + str(self.discapacidad) + " %" + str(self.porcentaje)
