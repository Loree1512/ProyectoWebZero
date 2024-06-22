function generarNavbar() {
    let navbar = `
        <div class="container-fluid">
            <div class="row">
                <div class="col-11">
                    <nav class="navbar navbar-expand-md" style="background-color: #e4e2dd;">
                        <div class="container-fluid">
                            <div class="container" style="width:100px;">
                                <a class="navbar-brand" href="#">                            
                                    <img src="/static/img/zero.png" alt="Grupo Zero" width="80" height="50"> 
                                </a>
                            </div>
                            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                                aria-expanded="false" aria-label="Toggle navigation">
                                <span class="navbar-toggler-icon"></span>
                            </button>
                            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                                    <li class="nav-item">
                                        <a class="nav-link active" aria-current="page" href="file:///C:/Users/gatit/OneDrive/Desktop/Proyecto%20Pagina%20Web%20Casi%20Final/index.html">Inicio</a>
                                    </li>
                                    <li class="nav-item dropdown">
                                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                                            aria-expanded="false">
                                            Categorías
                                        </a>
                                        <ul class="dropdown-menu">
                                            <li><a class="dropdown-item" href="#">Esculturas</a></li>
                                            <li><a class="dropdown-item" href="#">Pinturas</a></li>
                                            <li><hr class="dropdown-divider"></li>
                                            <li><a class="dropdown-item" href="file:///C:/Users/gatit/OneDrive/Desktop/Proyecto%20Pagina%20Web%20Casi%20Final/catalogo.html#">Ver todo</a></li>
                                        </ul>
                                    </li>
                                    <li class="nav-item dropdown">
                                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                                            aria-expanded="false">
                                            Artistas
                                        </a>
                                        <ul class="dropdown-menu">
                                            <li><a class="dropdown-item" href="file:///C:/Users/gatit/OneDrive/Desktop/Proyecto%20Pagina%20Web%20Casi%20Final/PerfilArtista.html">Maria Pinto Saavedra</a></li>
                                            <li><a class="dropdown-item" href="#">Jose Pablo Errazuriz</a></li>
                                        <li><a class="dropdown-item" href="#">Cristina Montenegro</a></li>
                                        <li>
                                            <hr class="dropdown-divider">
                                        </li>
                                        <li><a class="dropdown-item" href="#">Ver todo</a></li>
                                    </ul>
                                </li>
                                </ul>
                                
                                <!-- Formulario de inicio de sesion -->
                                <!--BOTON MODAL  -->
                                <div class="boton-modal">
                                    <label for="btn-modal">
                                       Ingresar
                                    </label>
                                  </div>
                                          <!-- fin boton -->
                                      
                                          <!-- ventana modal -->
                                      <input type="checkbox" id="btn-modal">
                                      <div class="container-modal">
                                          
                                          <div class="content-modal">
                                                      <div class="formulario_ini">
                                                          
                                                          
                                                         
                                                          <!-- Form con metodo post para enviar información -->
                                                        <form method="post" class="formulario" id="formulario">
                                                            <!-- Agregamos titulo -->
                                                                <h1>Inicio de sesion</h1>
                                                            
                                                            <!-- INICIO SESION: USUARIO -->
                                                                
                                                                <div class="formulario__usu-con " id="gp_username">
                                                                    <label for="usuario" class="formulario__label">Nombre de usuario</label>
                                                                    <div class="formulario_gp-input">
                                                                        <input type="text" class="formulario_input" name="usuario" id="usuario" placeholder="Usuario">   
                                                                        <i class="formulario__validacion-estado bi bi-x-octagon"></i>
                                                                        
                                                                    </div>
                                                                    <p class="formulario__input-error">Debe ser de 4 a 16 digitos y solamente letras, puntos y guion bajo.</p>
                                                                </div>
                                                            
                                                            <!-- INICIO SESION: CONTRASEÑA -->
                                                                <div class="formulario__usu-con " id="gp_contrasena">
                                                                    <label for="contrasena" class="formulario__label">Contraseña</label>
                                                                    <div class="formulario_gp-input">
                                                                        <input type="password" class="formulario_input" name="contrasena" id="contrasena" >
                                                                        <i class="formulario__validacion-estado bi bi-x-octagon"></i>
                                                                    </div>
                                                                    <p class="formulario__input-error">Debe ser de 4 a 12 digitos.</p>
                                                                </div>
                                                              
                                                                <div class="formulario__mensaje" id="formulario__mensaje">
                                                                
                                                                    <p><i class="bi bi-exclamation-triangle-fill"></i><b>Algo salio mal:</b>Por favor vuelva a intentarlo.</p>
                                                                
                                                                </div>
                                                              
                                                                <div class="recordar" style="padding-left: 25px; padding-top: 15px;">
                                                                    ¿Olvido su contraseña?
                                                                </div>
                                                              
                                                              <div class="formulario__iniciar formulario__btn-iniciar" style="padding: 10px;">
                                                                <button type="submit" class="formulario__btn">Iniciar</button>
                                                                <!-- <input type="submit" value="Iniciar"> -->
                                                                
                                                              </div>
                                                              
                              
                                                              <div class="registrarse" style="padding-left: 30%; padding-top: 15px;">
                                                                  <a href="">Registrarse</a>
                                                              </div>
                                                        </form>
                                                      
                                                              <div class="btn-cerrar">
                                                                  <label for="btn-modal"><i class="bi bi-x"></i></label>
                                          
                                                              </div>
                                                      
                                                        <label for="btn-modal" class="cerrar-modal"></label>      
                                                      </div>
                                                       
                                          </div>                
                                      </div> 
                                <!-- Fin formulario inicio sesion -->
                                <script src="formulario.js"></script>             
                            
                            <form class="d-flex" role="search">
                                <input class="form-control me-2" type="search" placeholder="Buscar" aria-label="Search">
                                <button class="btn btn-outline-success" type="submit">Buscar</button>
                            </form>
                        </div>
                    </div>
                </nav>
            </div>
            <!--Carrito-->
            <div class="col-1">
                <div class="popover" style="padding-top: 20%; background-color: #e4e2dd;">
                    <button class="popover-button"><i class="bi bi-cart" style="font-size: 25px;"></i></button>
                    <div class="popover-content">
                    Ningun producto seleccionado...
                    </div>
                </div>
              </div>
        </div>
        
    </div>
    `;
    
    document.getElementById("miNavbar").innerHTML = navbar;
}


document.addEventListener("DOMContentLoaded", function(){
    generarNavbar();
});

const listaComentarios = async() => {
    const respuesta = await fetch('https://jsonplaceholder.typicode.com/comments');
    const comentarios = await respuesta.json();
    let datosJson = [];
   // comentarios.forEach((comentario) => {
       // datosJson.push(comentario);
   // });
    Object.entries(comentarios).forEach(([postid, comentario]) => {
        let { name, body } = comentario;
        datosJson.push({
            nombre: name,
            mensaje: body
        });
    });
    
    document.getElementById("Nombre1").innerHTML= datosJson[1].nombre;
    
    document.getElementById("Comentario1").innerText= datosJson[1].mensaje;
    document.getElementById("Nombre2").innerText= datosJson[2].nombre;
    
    document.getElementById("Comentario2").innerText= datosJson[2].mensaje;
};

window.addEventListener("DOMContentLoaded",function(){
    listaComentarios();
});

function subir() {
    window.scrollTo({
        top: 0,
        behavior: "smooth" 
    });
}
