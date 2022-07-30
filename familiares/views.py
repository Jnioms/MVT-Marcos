from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from familiares.models import Familiar
import datetime

# Create your views here.

def add_familiares(request):
    date1 = datetime.date(1950, 11, 19)
    familiar1 = Familiar(nombre = "Papa", hijos = 4, fecha_nac = date1)
    date2 = datetime.date(1951, 3, 4)
    familiar2 = Familiar(nombre = "Mama", hijos = 4, fecha_nac = date2)
    date3 = datetime.date(1997, 6, 30)
    familiar3 = Familiar(nombre = "Hermana", hijos = 1, fecha_nac = date3)

    familiar1.save()
    familiar2.save()
    familiar3.save()

    return HttpResponse("Objetos de modelos para testear ingresados")

def familiares(request):

    familiares = Familiar.objects.all()

    lista_familiares = []

    if len(familiares) == 0:
    
        return HttpResponse("<p>No hay elementos en la BBDD. Te conviene ir a <a href='./add/'>familiares/add</a> primero.")

    else:
        for familiar in familiares:
            lista_familiares.append(f"<p>{familiar.nombre} tiene {familiar.hijos} hijos y nacio en {familiar.fecha_nac}</p>")
    
        return HttpResponse(lista_familiares)