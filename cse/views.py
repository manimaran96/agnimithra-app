from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def megaevents(request):
    return render(request, 'mega_events.html')

def techeve(request):
    return render(request, 'tech_eve.html')

def funbox(request):
    return render(request, 'fun_box.html')
