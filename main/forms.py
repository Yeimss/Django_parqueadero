from random import choices
from django import forms
from django.core import validators
from .models import *
from django.forms import ModelForm




class FormIngreso(ModelForm):
    class Meta:
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
            choices=[(1,"adfads")],
            attrs={
                'class':'form-select',
            }),
        }

        input_formats={'fecha_ingreso':["%Y-%m-%d %H:%M:%S"]}


