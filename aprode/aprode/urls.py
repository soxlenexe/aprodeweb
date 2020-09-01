"""aprode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include

# importamos las vistas
from proyectos.views import frontpage, proyectos, proyecto, ong
from tienda.views import tienda
import djrichtextfield

urlpatterns = [
    path('', frontpage, name ='frontpage'),
    path('proyectos/', proyectos, name ='proyectos'),
    path('proyecto/<slug:slug>/', proyecto, name ='proyecto'),
    path('ong/<slug:slug>/', ong, name='ong'),
    path('tienda/', tienda, name="tienda"),
    path('admin/', admin.site.urls),
    path('djrichtextfield/', include('djrichtextfield.urls')),
]
