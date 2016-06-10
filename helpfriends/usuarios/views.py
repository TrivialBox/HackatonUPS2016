from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import PCE
from ipware.ip import get_real_ip


def accion(request, id, accion):
    # if request.method == 'POST':
    ip = getip(request)
    return HttpResponse("<h1>" + str(ip) + "</h1>")
    # return redirect('/')


def getip(request):
    ip = get_real_ip(request)
    if ip is not None:
        return 0
    return ip

