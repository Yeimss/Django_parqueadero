from django import forms
from django.core import validators
from .models import *
from django.forms import ModelForm


class FormIngreso(ModelForm):
    class Meta:
        model=Vehiculos
        exclude=('valor_total', 'fecha_salida')

        widgets = {
            'placa':forms.TextInput(attrs={
                'placeholder':'Placa',
                'class':'form-control'
            }),
            'fecha_ingreso': forms.DateInput(attrs={
                'class': 'form-control',
                'type':'date'
            }),
            'celda':forms.Select(attrs={
                'class':'form-select'
            }),
        }
        input_formats={'fecha_ingreso':["%Y-%m-%d"]}



class FormSalida(ModelForm):
    class Meta:
        model=Vehiculos
        exclude=('valor_total', 'fecha_ingreso', 'celda')

        widgets = {
            'placa':forms.TextInput(attrs={
                'placeholder':'Placa',
                'class':'form-control'
            }),
            'fecha_salida': forms.DateInput(attrs={
                'class': 'form-control',
                'type':'date'
            }),
        }
        input_formats={'fecha_salida':["%Y-%m-%d"]}
