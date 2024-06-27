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
    path('artista_del/<str:pk>',views.artistas_del,name='artistas_del'),
    path('artistas_findEdit/<str:pk>', views.artistas_findEdit, name='artistas_findEdit'),
    path('artistasUpdate', views.artistasUpdate, name='artistasUpdate'),
    path ('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'), #URL pa agregar unprod al carrito
    path ('ver_carrito', views.ver_carrito, name ='ver_carrito'), #URL pa ver el contenido del carro

]

