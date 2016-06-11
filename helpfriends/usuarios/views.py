from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import PCE
from .models import Discapacidad

from ipware.ip import get_real_ip
import googlemaps

import requests
from bs4 import BeautifulSoup


def accion(request, id, accion):
    # if request.method == 'POST':
    d = Discapacidad(tipo="Cordura")
    d.save()
    # ip = getip(request)
    # return HttpResponse(get_direccion(ip))
    return redirect('/')


def get_direccion(ip):
    gmaps = googlemaps.Client(key='AIzaSyBCbMUYaa4h9gNoWAjq-6OKz7i9R3gf8JU')
    direccion = gmaps.reverse_geocode(getlatlng(ip))
    return direccion


def getlatlng(ip):
    soup = BeautifulSoup(get_raw_latlng(ip))
    latitud = soup.find('td', {'id': 'latitud'}).text
    longitud = soup.find('td', {'id': 'longitud'}).text
    return latitud, longitud


def getip(request):
    ip = get_real_ip(request)
    if ip is not None:
        return ip
    return '200.110.89.74'


def get_raw_latlng(ip):
    url = 'http://www.cual-es-mi-ip.net/geolocalizar-ip-mapa'
    data = {'direccion-ip': ip}
    req = requests.get(url, data=data)
    return req.text
