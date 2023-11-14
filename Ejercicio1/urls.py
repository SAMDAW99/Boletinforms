from django.urls import path
from Ejercicio1 import views

urlpatterns= [
    path('', views.pagina_bienvenida, name='pagina_bienvenida'),
    path('', views.pagina_formulario, name='pagina_formulario'),
]