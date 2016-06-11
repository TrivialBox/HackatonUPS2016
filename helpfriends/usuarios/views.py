from django.shortcuts import render, redirect
from django.http import HttpResponse
from push_notifications.models import GCMDevice

from .models import PCE

from ipware.ip import get_real_ip
import googlemaps

import requests
from bs4 import BeautifulSoup
import json


def accion(request, id, accion):
    ip = getip(request)
    datos = dict()
    direccion = get_direccion(ip)
    datos = add_streets(direccion, datos)
    datos = add_latlng(*getlatlng(ip), datos)
    try:
        p = PCE.objects.get(id=id)
        datos['nombre'] = p.nombre
        datos['accion'] = accion
        noticar(datos)
    except:
        pass
    return redirect('/')


def get_direccion(ip):
    gmaps = googlemaps.Client(key='AIzaSyBCbMUYaa4h9gNoWAjq-6OKz7i9R3gf8JU')
    latlng = getlatlng(ip)
    direccion = gmaps.reverse_geocode(latlng)
    return str(direccion)


def getlatlng(ip):
    soup = BeautifulSoup(get_raw_latlng(ip), "html.parser")
    latitud = soup.find('td', {'id': 'latitud'}).text
    longitud = soup.find('td', {'id': 'longitud'}).text
    return latitud, longitud


def getip(request):
    ip = get_real_ip(request)
    if ip is not None:
        return ip
    return '200.110.89.74'  # TODO


def get_raw_latlng(ip):
    url = 'http://www.cual-es-mi-ip.net/geolocalizar-ip-mapa'
    data = {'direccion-ip': ip}
    req = requests.get(url, data=data)
    return req.text


def add_latlng(lat, lng, new_json):
    new_json['latitud'] = lat
    new_json['longitud'] = lng
    return new_json


def add_streets(json_text, new_json):
    json_text = json_text.replace("'", '"')
    parsed_json = json.loads(json_text)[0]
    new_json['direccion'] = parsed_json['formatted_address']
    return new_json


def noticar(msj):
    devices = GCMDevice.objects.all()
    for device in devices:
        try:
            device.send_message(str(msj))
        except:
            continue
