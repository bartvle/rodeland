"""rodeland URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.start, name='start'),
    path('wat', views.wat, name='wat'),
    path('wie', views.wie, name='wie'),
    path('acties', views.acties, name='acties'),
    path('pdpo', views.pdpo, name='pdpo'),
    # path('infomoment', views.infomoment, name='infomoment'),
    # path('poelenfeest', views.poelenfeest, name='poelenfeest'),
    path('wandel-fiets', views.wandel_fiets, name='wandel-fiets'),
    path('admin/', admin.site.urls),

    ## redirects
    path('rodelandbrood', views.rodelandbrood),
    path('wetenschap-op-wieltjes', views.wetenschap_op_wieltjes),
]
