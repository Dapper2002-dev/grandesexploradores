from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail

def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def servicios(request):
    return render(request, 'servicios.html')

def programas(request):
    return render(request, 'programas.html')

def eventos(request):
    return render(request, 'eventos.html')

def contactanos(request):
    return render(request, 'contactanos.html')  