from django.contrib import admin
from .models import Carrito, Genero, Artista, ItemCarrito, ProductoC 

# Register your models here para que aparezcan en el panel de administracion.

admin.site.register(Genero)
admin.site.register(Artista)
admin.site.register(ProductoC)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)