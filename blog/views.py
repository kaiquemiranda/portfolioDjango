from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def blog(request):
    return HttpResponse('pagina do blog')

def exemplo(request):
    print('exemplo')
    return HttpResponse('pagina do exemplo')