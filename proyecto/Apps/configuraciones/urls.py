from django.contrib import admin
from django.urls import path
from proyecto.Apps.configuraciones.views import *


urlpatterns = [
        path('',login,name='login'),
        path('inicio/',index,name='inicio'),
        path('salir/',salir,name='salir'),
        path('usuario/',usuario,name='usuario'),
        path('agregar_usuario/',agregar_usuario,name='agregar_usuario'),
]
