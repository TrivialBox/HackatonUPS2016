from django.shortcuts import render, redirect
from django.http import HttpResponse

import json

from .models import PCE


def accion(request, id, accion):
    if request.method == 'POST':
        pass  # Notificar
    return redirect('/')
