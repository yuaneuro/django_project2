from django.shortcuts import render
import requests
from random import randint


def home(request):
    api = requests.get('https://api.github.com/users?since=' + str(randint(0, 99999)))
    api_json = api.json()
    return render(request, 'home.html', {'api': api_json})


def user(request):
    if request.method == 'POST':
        user = request.POST['user']
        api = requests.get('https://api.github.com/users/'+user)
        api_json = api.json()
        return render(request, 'user.html', {'user': user, 'api': api_json})
    else:
        notfound = 'please input user'
        return render(request, 'user.html', {'notfound': notfound})
