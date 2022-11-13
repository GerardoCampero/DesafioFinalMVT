from django.shortcuts import render
from FinaApp.forms import *
from FinaApp.models import *

# Create your views here.

# Se define vista inicio
def inicio(request):

    return render(request, 'FinaApp/index.html')

# Se define vistas formularios
def bajistas(request):
    
    if request.method == "POST":
        formulario = BajistasFORM(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            bajista = BajistasDB(nombre=data['nombre'], apellido=data['apellido'], edad=data['edad'], email=data['email'])
            bajista.save()

    formulario = BajistasFORM()

    return render(request, 'FinaApp/bajistas.html', {"formulario": formulario})

def bateristas(request):
    
    if request.method == "POST":
        formulario = BateristasFORM(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            baterista = BateristasDB(nombre=data['nombre'], apellido=data['apellido'], edad=data['edad'], email=data['email'])
            baterista.save()

    formulario = BateristasFORM()

    return render(request, 'FinaApp/bateristas.html', {"formulario": formulario})

def guitarristas(request):
    
    if request.method == "POST":
        formulario = GuitarristasFORM(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            guitarrista = GuitarristasDB(nombre=data['nombre'], apellido=data['apellido'], edad=data['edad'], email=data['email'])
            guitarrista.save()

    formulario = GuitarristasFORM()

    return render(request, 'FinaApp/guitarristas.html', {"formulario": formulario})

# Se definen vistas buscador
def buscar(request):

    return render(request, 'FinaApp/buscar.html')



def buscar_bajista(request):

    if request.GET:
        bajista = BajistasDB.objects.filter(nombre__icontains=request.GET["nombre_bajista"])
        return render(request, 'FinaApp/buscar_bajista.html', {"lista_bajistas": bajista})

    return render(request, 'FinaApp/buscar_bajista.html',{"lista_bajistas": []})

def buscar_baterista(request):

    if request.GET:
        baterista = BateristasDB.objects.filter(nombre__icontains=request.GET["nombre_baterista"])
        return render(request, 'FinaApp/buscar_baterista.html', {"lista_bateristas": baterista})


    return render(request, 'FinaApp/buscar_baterista.html', {"lista_bateristas": []})


def buscar_guitarrista(request):

    if request.GET:
        guitar = GuitarristasDB.objects.filter(nombre__icontains=request.GET["nombre_guitarrista"])
        return render(request, 'FinaApp/buscar_guitarrista.html', {"lista_guitarristas": guitar})
    
    return render(request, 'FinaApp/buscar_guitarrista.html', {"lista_guitarristas":[]} )

