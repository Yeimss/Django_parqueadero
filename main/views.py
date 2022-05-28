from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    celdas=Celdas.objects.all()
    return render(request, 'pages/index.html',{
        'title':'Inicio',
        'celdas':celdas,
    })

def ingreso(request):
    form=FormIngreso(request.POST)
    form2=FormSalida(request.POST)
    return render(request, 'pages/ingreso.html', {
        'title':'Ingreso/Salida',
        'form':form,
        'form2':form2,

    }) 