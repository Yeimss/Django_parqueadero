from django.db import models

""" class ChildVehiculo(models.Manager):
    def get_queryset(self):
        return super(ChildVehiculo, self).get_queryset().select_related('celda').filter(celda__estado=True) """