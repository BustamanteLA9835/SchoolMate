from django.http import HttpResponse

def hola_mundo(request):
    
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
<<<<<<< HEAD
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>   
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <div class="">
            <div class="">
                <nav class="navbar navbar-expand-lg  bg-dark">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">SchoolMate</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                        </li>
                        <li class="nav-item">
                        <a class="nav-link" href="#">Link</a>
                        </li>
                        <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Dropdown
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#">Action</a></li>
                            <li><a class="dropdown-item" href="#">Another action</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="#">Something else here</a></li>
                        </ul>
                        </li>
                        <li class="nav-item">
                        <a class="nav-link disabled" aria-disabled="true">Disabled</a>
                        </li>
                    </ul>
                    <form class="d-flex" role="Buscar">
                        <input class="form-control me-2" type="search" placeholder="Buscar" aria-label="Buscar"/>
                        <button class="btn btn-danger" type="submit">Ajustes</button>
                    </form>
                    </div>
                </div>
                </nav>
            </div>
        </div>
    <div style='font-family: sans-serif; text-align: center; padding-top: 50px;'>
      <h1>¡Bienvenido a SchoolMate!</h1>
      <p>Plataforma ligera de cursos.</p>
      <p>!Ir a mi panel!</p>
    </div>
        <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Tarea 1</th>
          <th scope="col">Tarea 2</th>
          <th scope="col">Tarea 3</th>
        </tr>
      </thead>
      <tbody class="table-group-divider">
        <tr>
          <th scope="row">1</th>
          <td>Realiza la actividad 1</td>
          <td>Realiza la actividad 2</td>
          <td>Realiza la actividad 3</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Ver actividad 1</td>
          <td>Ver actividad 2</td>
          <td>Ver actividad 3</td>
        </tr>
      </tbody>
    </table>
    <div class="container text-center">
  <div class="row align-items-start">
    <div class="col">
      Español
    </div>
    <div class="col">
      Matematicas
    </div>
    <div class="col">
      Ciencias naturales
    </div>
  </div>
</div> 
<p><a class="link-opacity-100" href="#">https://es.scribd.com/document/419766591/QUE-ES-LA-MATERIA-ESPANOL-docx</a></p> 
<p style="text-align: center;">
  <a class="link-opacity-100" href="#">https://concepto.de/matematicas/</a>
</p>
<p style="text-align: right;">
  <a class="link-opacity-100" href="#">https://concepto.de/ciencias-naturales/</a>
</p>
<div class="container text-center">
  <div class="row align-items-start">
    <div class="col">
      modulo
    </div>
    <div class="col">
      ingles
    </div>
    <div class="col">
      conciencia historica
    </div>
  </div>
</div> 
<p><a class="link-opacity-100" href="#">https://www.netec.com/que-es-programacion</a></p> 
<p style="text-align: center;">
  <a class="link-opacity-100" href="#">https://www.cambridgeenglish.org/latinamerica/learning-english/</a>
</p>
<p style="text-align: right;">
  <a class="link-opacity-100" href="#">https://nem.comenio.ai/mccems/conciencia-historica</a>
</p>
    </body>

    </html>
    """
    return HttpResponse(html_content)
=======
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SchoolMate</title>

        <style>
            body {
                background-color: #cce7ff;
            }
            /* Color en navbar */
            .navbar-custom {
                background-color: #000000;
            }
            .navbar-custom .nav-link,
            .navbar-custom .navbar-brand,
            .navbar-custom .dropdown-item,
            .navbar-custom .nav-link.disabled {
                color: #cce7ff !important;
            }
            .dropdown-menu {
                background-color: #000000;
            }
            .ajustes-btn {
                background-color: #cce7ff !important;
                color: black !important;  /* Puedes cambiar el color del texto */
                border: none !important;
            }
            .table-custom {
            background-color: #000000 !important;
            color: #cce7ff !important;
            }

            .table-custom th,
            .table-custom td {
            background-color: #000000 !important;
            color: #cce7ff !important;
            border-color: #cce7ff !important;
            }
        </style>

    </head>

    <body>
        <nav class="navbar navbar-expand-lg navbar-custom">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">SchoolMate</a>

                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarSupportedContent">

                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" href="#">Home</a>
                        </li>

                        <li class="nav-item">
                            <a class="nav-link" href="#">Link</a>
                        </li>

                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
                                Dropdown
                            </a>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="#">Action</a></li>
                                <li><a class="dropdown-item" href="#">Another action</a></li>
                                <li><hr class="dropdown-divider"></li>
                                <li><a class="dropdown-item" href="#">Something else here</a></li>
                            </ul>
                        </li>

                        <li class="nav-item">
                            <a class="nav-link disabled">Disabled</a>
                        </li>
                    </ul>

                    <form class="d-flex" role="Buscar">
                        <input class="form-control me-2" type="search" placeholder="Buscar">
                        <button class="btn ajustes-btn" type="submit">Ajustes</button>
                    </form>

                </div>
            </div>
        </nav>

        <div style='font-family: sans-serif; text-align: center; padding-top: 50px;'>
          <h1>¡Bienvenido a SchoolMate!</h1>
          <p>Plataforma ligera de cursos.</p>
          <p>¡Voy a mi panel!</p>
        </div>

        <table class="table table-custom">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Tarea 1</th>
                    <th>Tarea 2</th>
                    <th>Tarea 3</th>
                </tr>
            </thead>
            <tbody class="table-group-divider">
                <tr>
                    <th>1</th>
                    <td>Realiza la actividad 1</td>
                    <td>Realiza la actividad 2</td>
                    <td>Realiza la actividad 3</td>
                </tr>
                <tr>
                    <th>2</th>
                    <td>Ver actividad 1</td>
                    <td>Ver actividad 2</td>
                    <td>Ver actividad 3</td>
                </tr>
            </tbody>
        </table>

        <div class="container text-center">
            <div class="row align-items-start">
                <div class="col">Español</div>
                <div class="col">Matemáticas</div>
                <div class="col">Ciencias naturales</div>
            </div>
        </div>

        <p><a href="#" class="link-opacity-100">https://es.scribd.com/document/419766591/QUE-ES-LA-MATERIA-ESPANOL-docx</a></p>
        <p style="text-align: center;">
            <a href="#" class="link-opacity-100">https://concepto.de/matematicas/</a>
        </p>
        <p style="text-align: right;">
            <a href="#" class="link-opacity-100">https://concepto.de/ciencias-naturales/</a>
        </p>

        <div class="container text-center">
            <div class="row align-items-start">
                <div class="col">Módulo</div>
                <div class="col">Inglés</div>
                <div class="col">Conciencia histórica</div>
            </div>
        </div>

        <p><a href="#" class="link-opacity-100">https://www.netec.com/que-es-programacion</a></p>
        <p style="text-align: center;">
            <a href="#" class="link-opacity-100">https://www.cambridgeenglish.org/latinamerica/learning-english/</a>
        </p>
        <p style="text-align: right;">
            <a href="#" class="link-opacity-100">https://nem.comenio.ai/mccems/conciencia-historica</a>
        </p>

    </body>
    </html>
    """
    return HttpResponse(html_content)

>>>>>>> 14ef7c07ac5a02f805a2444b1e585293382f7073
