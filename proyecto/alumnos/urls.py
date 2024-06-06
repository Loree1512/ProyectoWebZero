#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns =[
    path ('', views.index, name='index'),
    path ('catalogo', views.catalogo, name='catalogo'),
    path ('formularioPublicacion', views.formularioPublicacion, name='formularioPublicacion'),
    path ('paginaCompra', views.paginaCompra, name='paginaCompra'),
    path ('PerfilArtista', views.perfilArtista, name='PerfilArtista'),
    path ('producto', views.producto, name='producto'),
    path('listaArtista',views.lista_artista, name='listaArtista'),
    path('agregarArtista',views.agregarArtista, name='agregarArtista'),
]

