
from django.http import HttpResponse
from django.shortcuts import render 
from Limpieza.forms import quimForm, cepiForm, descaForm
from .models import Quimico, Cepillo, Descartable
# Create your views here.
from django.shortcuts import render

def inicio(request):
    return render (request, "inicio.html")

def quimicos(request):
    return render (request, "quimicos.html")

def cepillos(request):
    return render (request, "cepillos.html")

def descartables(request):
    return render (request, "descartables.html")

def formularioquimicos(request):

    if request.method=="POST":
        form=quimForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            proveedor=informacion["proveedor"]
            prodxbulto=informacion["prodxbulto"]
            quimi=Quimico(nombre=nombre, proveedor=proveedor, prodxbulto=prodxbulto)
            quimi.save()
            return render (request, "inicio.html", {"mensaje": "PRODUCTO QUIMICO CREADO CORRECTAMENTE!!"})
    else:
        formulario=quimForm()


    return render (request, "formularioquimico.html", {"form":formulario})

def formulariocepillos(request):

    if request.method=="POST":
        form=cepiForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            proveedor=informacion["proveedor"]
            prodxbulto=informacion["prodxbulto"]
            cepi= Cepillo(nombre=nombre, proveedor=proveedor, prodxbulto=prodxbulto)
            cepi.save()
            return render (request, "inicio.html", {"mensaje": "CEPILLO CREADO CORRECTAMENTE!!"})
    else:
        formulario=cepiForm()


    return render (request, "formulariocepillo.html", {"form":formulario})

def formulariodescartables(request):

    if request.method=="POST":
        form=descaForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            proveedor=informacion["proveedor"]
            prodxbulto=informacion["prodxbulto"]
            desca= Descartable(nombre=nombre, proveedor=proveedor, prodxbulto=prodxbulto)
            desca.save()
            return render (request, "inicio.html", {"mensaje": "PRODUCTO DESCARTABLE CREADO CORRECTAMENTE!!"})
    else:
        formulario=descaForm()


    return render (request, "formulariodescartable.html", {"form":formulario})

def busqueda(request):
    return render(request, "busqueda.html")


def buscar(request):

    if request.GET["nombre"]:

        nombre=request.GET["nombre"]
        quimicos=Quimico.objects.filter(nombre__icontains=nombre)
        return render(request,"resultadosBusqueda.html", {"quimicos":quimicos} )
    else:
        return render(request, "busqueda.html", {"mensaje":"CHE! Ingresa nomrbre de un producto quimico"})








