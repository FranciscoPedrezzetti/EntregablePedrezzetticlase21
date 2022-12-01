
from django.urls import path
from Limpieza.views import *

urlpatterns = [
    path("quimicos/", quimicos, name="quimicos"),
    path("cepillos/", cepillos, name="cepillos"),
    path("descartables/", descartables, name="descartables"),
    path("", inicio, name="inicio"),
    path("formularioquimicos/", formularioquimicos, name="formularioquimicos"),
    path("formulariocepillos/", formulariocepillos, name="formulariocepillos"),
    path("formulariodescartables/", formulariodescartables, name="formulariodescartables"),
    path("busqueda/", busqueda, name="busqueda"),
    path("buscar/", buscar, name="buscar" ),
]