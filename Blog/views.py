from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def index(request):
    now = datetime.datetime.now();
    return render(request, 'Blog/inicio.html', {'current_date': now})
def esta_pagina(request):
    return render(request, 'Blog/esta-pagina.html', {})
