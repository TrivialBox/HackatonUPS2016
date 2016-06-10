from django.contrib import admin

from .models import Discapacidad
from .models import PCE
from .models import TrabajadorPublico
from .models import Ciudadano

admin.site.register(Discapacidad)
admin.site.register(PCE)
admin.site.register(TrabajadorPublico)
admin.site.register(Ciudadano)
