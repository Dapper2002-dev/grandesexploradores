from django.urls import path 
from . import views

urlpatterns = [
    path('', views.inicio),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('programas/', views.programas, name='programas'),
    path('eventos/', views.eventos, name='eventos'),
    path('contactanos/', views.contactanos, name='contactanos'),
]