from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import CreateView
from datetime import datetime, timezone

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
                #Cambiar el estado de la celda en la tabla de celdas
                modelCelda=Celdas.objects.get(pk=celda.id)
                if modelCelda.estado:
                    estado=modelCelda.estado
                    modelCelda.estado=not estado
                    modelCelda.save()
                    #######################################
                    form.save()
                    messages.success(request, 'Gracias por elegirnos como su parqueadero de confianza')
                    return redirect('ingreso')
                else:
                    messages.warning(request, 'Esa celda está ocupada, por favor verifique las celdas que están disponibles')
                    return redirect('ingreso')

            else:
                messages.warning(request, 'Hay algun error en el formulario')
                return redirect('ingreso')


class Salida(ListView):
    model=Vehiculos
    template_name="pages/salida.html"
    def get_context_data(self,  **kwargs):  
        context=super().get_context_data(**kwargs)
        tarifa=Tarifas.objects.order_by('-fecha')[:1]
        fecha_completa=datetime.datetime.now()
        fecha_personalizada=fecha_completa.strftime("%d/%m/%Y %H:%M:%S")
        vehiculos=Vehiculos.objects.select_related("celda").filter(celda__estado=0)
        #for para guardar los nuevos precios de el parqueader/se actualiza al recargar la pagina
        #sirve para poder mostrar dichos precios en el template
        for vehiculo in vehiculos:
            d = vehiculo.fecha_ingreso.strftime("%d/%m/%Y %H:%M:%S")
            tiempo_total=datetime.datetime.strptime(fecha_personalizada,"%d/%m/%Y %H:%M:%S") - datetime.datetime.strptime(d,"%d/%m/%Y %H:%M:%S")
            segundos=tiempo_total.days * 24 * 3600 + tiempo_total.seconds        
            minutos=segundos//60      
            vehiculo.valor_total=minutos*tarifa[0].precio
            vehiculo.save()

        if 'vehiculos' not in context:
            context['vehiculos']=Vehiculos.objects.select_related("celda").filter(celda__estado=0)
        if 'tarifa' not in context:
            context['tarifa']=tarifa[0].precio
        return context
    
def salir(request, id):
    try:
        vehiculo=Vehiculos.objects.get(pk=id)
        vehiculo.celda=None
        vehiculo.fecha_salida=datetime.datetime.now()
        vehiculo.save()
        messages.success(request, 'Puede salir, muchas gracias por preferirnos como su parqueadero de confianza')
        return redirect('salida')
    except:
        messages.warning(request, 'No ha podido salir con exito, lo siento, tendrá que quedarse por siempre')
        return redirect('salida')
