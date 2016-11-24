from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$|inicio', views.index),
    url(r'^$|esta-pagina', views.details),
    url(r'^$|entrada/([\w,-]+)', views.details),
    url(r'^$|nuevo-comentario/', views.details, name='comment')
]
