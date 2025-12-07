from django.urls import path
from . import views

urlpatterns = [
    path('mi-pagina/', views.hola_mundo, name='mi_pagina'),
    path('', views.hola_mundo, name='hola'),
    path('registro_tarea/', views.registrar_tarea, name='registro_tarea'),
    path('tareas/<int:pk>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tareas/<int:pk>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
]
