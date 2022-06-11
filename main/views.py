from ast import Return
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import CreateView

from .models import *
from .forms import *

def index(request):
    celdas=Celdas.objects.all().order_by("nombre")
    return render(request, 'pages/index.html',{
        'title':'Inicio',
        'celdas':celdas,
    })
class Ingreso(CreateView):
    model=Vehiculos
    template_name="pages/ingreso.html"
    form_class=FormIngreso

    def get_context_data(self,  **kwargs):
        context=super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        self.object=self.get_object
        if request.method=='POST':
            form= FormIngreso(request.POST)
            if form.is_valid():
                data=form.cleaned_data
                celda=data['celda']
                modelCelda=Celdas.objects.get(pk=celda.id)
                estado=modelCelda.estado
                print(estado)
                modelCelda.estado=not estado
                estado=modelCelda.estado
                print(estado)
                modelCelda.save()
                form.save()
                messages.success(request, 'Gracias por elegirnos como su parqueadero de confianza')
                return redirect('ingreso')
            else:
                messages.warning(request, 'Hay algun error en el formulario')
                return redirect('ingreso')



def ingreso(request):
    form=FormIngreso(request.POST)

    return render(request, 'pages/ingreso.html', {
        'title':'Ingreso/Salida',
        'form':form,
    }) 

class Salida(ListView):
    model=Vehiculos
    template_name="pages/salida.html"
    def get_context_data(self,  **kwargs):
        context=super().get_context_data(**kwargs)
        if 'vehiculos' not in context:
            context['vehiculos']=Vehiculos.objects.select_related("celda").filter(celda__estado=0)
        return context
    """ def get_queryset(self):
        if self.request.GET.get('acronym') is not None:
            return 
        return super().get_queryset() """
    