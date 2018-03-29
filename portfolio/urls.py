"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from suveen import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^experience/$', views.experience, name="experience"),
    url(r'^education/$', views.education, name="experience"),
    url(r'^skills/$', views.skills, name="experience"),
    url(r'^training/$', views.training, name="experience"),
    url(r'^internships/$', views.internships, name="experience"),
    url(r'^voluntary/$', views.voluntary, name="experience"),
    url(r'^academic/$', views.academic, name="experience"),
    url(r'^publications/$', views.publications, name="experience"),
    url(r'^contact/(?P<pk>\d+)/read', views.mark_contact_read, name="mark_contact_read"),
    url(r'^$', views.index, name="index"),
]
