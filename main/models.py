from django.db import models
import datetime

# Create your models here.

class Tarifas(models.Model):
    precio=models.FloatField(null=False, verbose_name="Tarifa")
    fecha=models.DateField(null=False, auto_now=True, verbose_name="Fecha")
    class Meta:
        verbose_name="Tarifa"
        verbose_name_plural="Tarifas"

    def __str__(self):
        return str(self.precio)
    

class Celdas(models.Model):
    nombre=models.CharField(max_length=3,unique=True, verbose_name="Celda")
    estado=models.BooleanField(verbose_name="¿Está disponible?")
    class Meta:
        verbose_name="Celda"
        verbose_name_plural="Celdas"
        db_table="Celdas"
    
    def __str__(self):
        return self.nombre
    
class Vehiculos(models.Model):
    placa=models.CharField(max_length=6, null=False, verbose_name="Placa")
    fecha_ingreso=models.DateTimeField(auto_now=False, auto_now_add=False, null=False, verbose_name="Fecha de ingreso")
    fecha_salida=models.DateTimeField(null=False, default=datetime.datetime(2020,1,1), verbose_name="Fecha de salida")
    valor_total=models.FloatField(null=True, blank=True, verbose_name="Precio Total")
    celda=models.ForeignKey(Celdas, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Celda", related_name="%(class)s_Celda")
    class Meta:
        verbose_name="Vehiculo"
        verbose_name_plural="Vehiculos"
        db_table="Vehiculos"
    
    def __str__(self):
        return self.placa
    



