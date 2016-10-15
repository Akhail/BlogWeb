from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$|inicio', views.index),
    url(r'^$|esta-pagina', views.esta_pagina),
]
