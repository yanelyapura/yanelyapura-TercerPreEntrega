from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_datos, name='agregar_datos'),
    path('buscar/', views.buscar_libro, name='buscar_libro'),
]