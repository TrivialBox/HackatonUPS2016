from django.shortcuts import render, redirect
from django.http import HttpResponse

import json

from .models import PCE


def accion(request, id, accion):
    if request.method == 'POST':
        ip = getip(request)
        return HttpResponse("<h1>" + ip + "</h1>")
    # return redirect('/')


def getip(request):
    ip = request.META['HTTP_X_FORWARDED_FOR']
    return str(ip)
