from django.shortcuts import render
from .models import Artista,Genero

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

