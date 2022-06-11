from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('ingreso/',views.Ingreso.as_view(), name="ingreso"),
    path('salida/',views.Salida.as_view(), name="salida"),


]
