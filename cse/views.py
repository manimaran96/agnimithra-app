from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError

from .models import Person

# Create your views here.

def index(request):
    return render(request, 'index.html')

def megaevents(request):
    return render(request, 'megaevents.html')

def techeve(request):
    return render(request, 'techeve.html')

def funbox(request):
    return render(request, 'funbox.html')

def register(request):
    try:
        if request.method == "POST":
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            college = request.POST.get('college','')
            person = Person.objects.create(candidate=name, mailid=email, college=college)
            person.save()
            return render(request, "registersuccess.html")
    except IntegrityError:
        message = "Sorry! The email you have entered is already Registered"
        return render(request, "register.html", {"message": message}) 
    return render(request, "register.html")
