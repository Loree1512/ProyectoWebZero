from django.shortcuts import render
from .models import Artista,Genero
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
    request.session["usuario"]="@Lore_1512"
    usuario=request.session["usuario"]
    context= {'usuario':usuario}
    return render(request, 'webzero/index.html', context)