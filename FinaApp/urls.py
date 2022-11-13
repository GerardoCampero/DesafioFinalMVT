from django.urls import path
from FinaApp.views import *

# Se definen urls de la app
urlpatterns = [
    path('inicio/', inicio, name='inicio'), 
    path('bajistas/', bajistas, name='bajistas'), 
    path('bateristas/', bateristas, name='bateristas'),
    path('guitarristas/', guitarristas, name='guitarristas'),
    path('buscar/', buscar, name='buscar'),
    path('buscar-bajista/', buscar_bajista, name='buscar-bajista'),
    path('buscar-baterista/', buscar_baterista, name='buscar-baterista'),
    path('buscar-guitarrista/', buscar_guitarrista, name='buscar-guitarrista'),
]