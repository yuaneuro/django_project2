from django.shortcuts import render
import requests
from random import randint


def home(request):
    api = requests.get('https://api.github.com/users?since=' + str(randint(0, 99999)))
    api_json = api.json()
    return render(request, 'home.html', {'api': api_json})
