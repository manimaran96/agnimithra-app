from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^megaevents', views.megaevents, name='megaevents'),
    url(r'^funbox', views.funbox, name='funbox'),
    url(r'^techeve', views.techeve, name='techeve'),
    url(r'^register', views.register, name='register'),
]
