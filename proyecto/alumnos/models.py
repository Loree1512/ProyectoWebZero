from django.db import models

# Create your models here.

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

def __str__(self):
    return str(self.genero)

class Artista(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.IntegerField()

def __str__(self):
    return str(self.nombre)+" "+str(self.apellido_paterno)

# Modelo para los productos disponibles de la tienda
class ProductoC(models.Model):
    nombre = models.CharField(max_length=255) # Nombre del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2) # Precio del producto
    descripcion = models.TextField() #Descripcion producto

    def __str__(self):
        return self.nombre #Representacion en cadena del producto 
    
#Modelo para carrito de compras

class Carrito(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True) #Fecha de la creacion del carro

# Modelo para los productos dentro del carro
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE) #RElacion con el carro
    productoC = models.ForeignKey(ProductoC, on_delete=models.CASCADE) #relacion con el producto
    cantidad = models.PositiveIntegerField(default=1) # cantidad de este producto en el carro

    def __str__(self):
        return f'{self.cantidad} x {self.productoC.nombre}' #representacion en cadena del objeto del carrito

