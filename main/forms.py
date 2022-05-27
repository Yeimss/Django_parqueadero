from django import forms
from django.core import validators
from .models import *
from django.forms import ModelForm


class FormIngreso(ModelForm):
    class Meta:
        model=Vehiculos
        fields="__all__"

        widgets = {
            'placa':forms.TextInput(attrs={
                'placeholder':'Placa',
                'class':'form-input'
            }),
            'fecha_salida': forms.DateInput(attrs={
                'class': 'form-input',
                'type':'date'
            }),
        }
        input_formats={'fecha_salida':["%Y-%m-%d"]}
