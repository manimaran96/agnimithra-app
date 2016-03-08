from django.conf.urls import include, url
from django.contrib import admin
from cse import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'agnimithra2k16.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name="index"),
    url(r'^cse/', include('cse.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
