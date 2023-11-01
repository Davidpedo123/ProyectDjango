from django.shortcuts import render
import requests

def clima():
    API_KEY = 'af5767adfd6471c26a5c9971990a87ef'
    OP = 'temperatura'
    Z = '10'
    X = '-7074932.886'
    Y = '3908195.838'

    url = f'http://maps.openweathermap.org/maps/2.0/weather/{OP}/{Z}/{X}/{Y}?appid={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        mapa_del_clima = response.content
    else:
        mapa_del_clima = None

    return mapa_del_clima
