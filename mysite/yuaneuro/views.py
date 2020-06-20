from django.shortcuts import render
import requests
import random

# Create your views here.

def home(request):
    api = requests.get('https://api.github.com/users?since='+str(random.randint(0, 99999)))
    api_json = api.json()
    return render(request, 'home.html', {'api': api_json})
