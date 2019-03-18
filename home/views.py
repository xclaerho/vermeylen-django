from django.shortcuts import render, redirect
from django.contrib.auth import logout as out
from .models import PraesidiumMember, Sponsor
from random import shuffle

# Create your views here.
def index(request):
    sponsors = Sponsor.objects.all()
    shuffle(sponsors)
    return render(request, 'home/index.html',{'sponsors':sponsors})

def info(request):
    return render(request, 'home/info.html')

def clublied(request):
    return render(request, 'home/clublied.html')

def archief(request):
    return render(request, 'home/archief.html')

def praesidium(request):
    praesidiummembers = PraesidiumMember.objects.all()
    return render(request, 'home/praesidium.html',{'praesidiummembers':praesidiummembers})