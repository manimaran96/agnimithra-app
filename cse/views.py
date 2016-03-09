import os

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError
from django.template import Context
from django.template.loader import get_template

from easy_pdf.rendering import render_to_pdf_response
from xhtml2pdf import pisa

from .models import Person
from .utils import link_callback

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

def admitcard(request):
    try:
        if request.method == "POST":
            email = request.POST.get('email','')
            person = Person.objects.get(mailid=unicode(email))
            data = {'person': person}
            template = get_template('admitcard.html')
            html = template.render(Context(data))
            f = open(os.path.join(settings.MEDIA_ROOT, 'admitcard.pdf'), "w+b")
            pisaStatus = pisa.CreatePDF(html, dest=f, link_callback=link_callback)
            file.seek(0)
            pdf = file.read()
            file.close()            
            return HttpResponse(pdf, mimetype='application/pdf')
    except Person.DoesNotExist:
        message = "Sorry! The email you have entered is not Registered. Please Register!"
        return render(request, "register.html", {"message": message})
    return render(request, "register.html")

