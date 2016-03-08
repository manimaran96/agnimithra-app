from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def megaevents(request):
    return render(request, 'megaevents.html')

def techeve(request):
    return render(request, 'techeve.html')

def funbox(request):
    return render(request, 'funbox.html')
