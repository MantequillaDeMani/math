from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
  
    path('pagina/', views.pagina_css, name='pagina_css'),
    path('numeros/', views.numeros, name='numeros'),
    path('intro/', views.intro, name='intro'), 
     path('ejercicios/', views.ejercicios, name='ejercicios'),
    path('numeros/ejercicios/', views.ejercicios, name='numeros_ejercicios'),    
    path('ejercicios2_u1/', views.ejercicios2_u1, name='ejercicios2_u1'),   
    path('numeros2/', views.numeros2, name='numeros2'),   
    path("pdfs/", views.lista_pdfs, name="lista_pdfs"),           
           
            ]
