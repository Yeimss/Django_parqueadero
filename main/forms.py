from random import choices
from django import forms
from django.core import validators
from .models import *
from django.forms import ModelForm




class FormIngreso(ModelForm):

    class Meta:
        celdas=Celdas.objects.filter(estado=1)
        c=[]
        for celda in celdas:
            tupla=(celda.pk, celda.nombre)
            c.append(tupla)

        #-----------------------
        model=Vehiculos
        exclude=('valor_total', 'fecha_salida','fecha_ingreso')
        widgets = {
            'placa':forms.TextInput(
            attrs={
                'placeholder':'Placa',
                'class':'form-control'
            }),
            'fecha_ingreso': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type':'datetime-local'
            }),
            'celda':forms.Select(
            attrs={
                'class':'form-select',
            }),
        }
        choices={
            'celda':c
        }

        input_formats={'fecha_ingreso':["%Y-%m-%d %H:%M:%S"]}


