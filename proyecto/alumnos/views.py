from django.shortcuts import render, get_object_or_404, redirect
from .models import Artista,Genero,ProductoC, Carrito, ItemCarrito
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'webzero/index.html')

def catalogo(request):
    return render(request,"webzero/catalogo.html")

def formularioPublicacion(request):
    return render(request,"webzero/formularioPublicacion.html")

def paginaCompra(request):
    return render(request,"webzero/paginaCompra.html")

def perfilArtista(request):
    return render(request,"webzero/PerfilArtista.html")

def producto(request):
    return render(request,"webzero/producto.html")

def lista_artista(request):
    artistas= Artista.objects.all()
    context={"artistas":artistas}
    return render(request,'webzero/listaArtista.html', context)

def agregarArtista(request):
    if request.method is not "POST":
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'webzero/agregarArtista.html',context)
    else:
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero=genero)
        obj=Artista.objects.create ( rut=rut,
                                    nombre=nombre,
                                    apellido_paterno= aPaterno,
                                    apellido_materno = aMaterno,
                                    fecha_nacimiento= fechaNac,
                                    id_genero=objGenero,
                                    telefono=telefono,
                                    email=email,
                                    direccion=direccion,
                                    activo=1)
        obj.save()
        context={'mensaje':"ok, datos guardados..."}
        return render(request,'webzero/agregarArtista.html', context)

def artistas_del(request,pk):
    context={}
    try:
        artista=Artista.objects.get(rut=pk)

        artista.delete()
        mensaje="Bien,datos eliminados..."
        artistas=Artista.objects.all()
        context={'artistas':artistas, 'mensaje': mensaje}
        return render(request,'webzero/listaArtista.html', context)
    except: 
        mensaje= "Error, rut no existe "
        artistas = Artista.objects.all()
        context={'artistas':artistas, 'mensaje': mensaje}
        return render(request,'webzero/listaArtista.html', context)
        
def artistas_findEdit (request,pk):
    if pk != "":
        artista=Artista.objects.get(rut=pk)
        generos=Genero.objects.all()

        print(type(artista.id_genero.genero))

        context= {'artista': artista, 'generos': generos}
        if artista:
            return render(request, 'webzero/artistas_edit.html', context)
        else: 
            context={'mensaje': "Error, rut no existe..."}
            return render(request, 'webzero/listaArtista.html',context)
        
def artistasUpdate (request):
    if request.method == "POST":
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero=genero)

        artista= Artista()
        artista.rut= rut
        artista.nombre= nombre
        artista.apellido_paterno= aPaterno
        artista.apellido_materno= aMaterno
        artista.fecha_nacimiento= fechaNac
        artista.id_genero= objGenero
        artista.email= email
        artista.direccion= direccion
        artista.activo= 1
        artista.save()

        generos=Genero.objects.all()
        context={'mensaje': "Ok, datos actualizados...", "generos": generos, "artista": artista}
        return render(request, 'webzero/artistas_edit.html', context)
    else:
        artistas = Artista.objects.all()
        context={'artistas': artistas}
        return render(request, 'webzero/listaArtista.html',context)
    
@login_required
def menu(request):
    request.session["usuario"]=request.user.username
    usuario=request.session["usuario"]
    context= {'usuario':usuario}
    return render(request, 'webzero/index.html', context)

# las vistas para agregar un producto al carrito.

def agregar_al_carrito(request, productoC_id):
    
    productoC = get_object_or_404(ProductoC, id=productoC_id) #obtiene el producto o retorna 404 si no existe
    carrito_id= request.session.get('carrito_id') #obtiene id del carro de la sesion.

    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id) #obtiene carrito existente
    else:
        carrito = Carrito.objects.create() #crea carrito nuevo si no existe
        request.session['carrito_id'] = carrito.id #guarda la id del nuevo carrito en la sesion
    
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, productoC=productoC)
    if not created:
        item.cantidad += 1 #incrementa la cantidad si el item ya existia
        item.save() #guarda el item actualizado

    return redirect('ver_carrito') #Redirige a la vista del carrito

#Vista para mostrar el contenido del carrito

def ver_carrito(request):
    carrito_id = request.session.get('carrito_id') # obtiene el id del carrito de la sesion
    if carrito_id: 
        carrito = Carrito.objects.get(id=carrito_id) 
        items = carrito.items.all() 
        total = 0 
        for item in items: 
            item.total_por_linea = item.cantidad * item.producto.precio 
            total += item.total_por_linea
    else:
        carrito = None #no hay carrito si el id no esta en la sesion
        items = []
        total = 0

    return render(request, 'webzero/ver_carrito.html', {'carrito': carrito, 'items': items, 'total': total}) #renderiza la plantilla con el carrito


