from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea

def registrar_tarea(request):
    tarea = None       
    message = None
    errors = {}

    data = {
        'titulo': '',
        'materia': '',
        'grado': '',
        'fecha_entrega': '',
        'estado': '',
        'descripcion': '',
    }
#El guadado de datos materia,titulo,fecha de entrega etc
#Hecho por Elvis
    if request.method == 'POST':
        data['titulo'] = request.POST.get('titulo', '').strip()
        data['materia'] = request.POST.get('materia', '').strip()
        data['grado'] = request.POST.get('grado', '').strip()
        data['fecha_entrega'] = request.POST.get('fecha_entrega', '').strip()
        data['estado'] = request.POST.get('estado', '').strip()
        data['descripcion'] = request.POST.get('descripcion', '').strip()
        archivo = request.FILES.get('archivo')

        if not data['titulo']:
            errors['titulo'] = 'El título es obligatorio.'
        if not data['materia']:
            errors['materia'] = 'La materia es obligatoria.'
        if not data['grado']:
            errors['grado'] = 'El grado es obligatorio.'
        if not data['fecha_entrega']:
            errors['fecha_entrega'] = 'La fecha de entrega es obligatoria.'
        if not data['estado']:
            errors['estado'] = 'El estado es obligatorio.'
        if not data['descripcion']:
            errors['descripcion'] = 'La descripción es obligatoria.'

        if not errors:
            tarea_nueva = Tarea(
                titulo=data['titulo'],
                materia=data['materia'],
                grado=data['grado'],
                fecha_entrega=data['fecha_entrega'],  
                estado=data['estado'],
                descripcion=data['descripcion'],
            )
            if archivo:
                tarea_nueva.archivo = archivo

            tarea_nueva.save()
            message = "La tarea se guardó correctamente."

            data = {
                'titulo': '',
                'materia': '',
                'grado': '',
                'fecha_entrega': '',
                'estado': '',
                'descripcion': '',
            }

    return render(request, 'nucleo/registro_tarea.html', {
        'tarea': tarea,      
        'message': message,  
        'errors': errors,    
        'data': data,        
    })
#Edicion de datos hecho por Saul

def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    message = None

    if request.method == 'POST':
        tarea.titulo = request.POST.get('titulo')
        tarea.materia = request.POST.get('materia')
        tarea.grado = request.POST.get('grado')
        tarea.fecha_entrega = request.POST.get('fecha_entrega')
        tarea.estado = request.POST.get('estado')
        tarea.descripcion = request.POST.get('descripcion')
        archivo = request.FILES.get('archivo')

        if archivo:
            tarea.archivo = archivo

        tarea.save()
        message = "La tarea se actualizó correctamente."

    return render(request, 'nucleo/registro_tarea.html', {
        'tarea': tarea,
        'message': message,
    })
#Eliminar regristro hecho por romina

def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)

    if request.method == 'POST':
        tarea.delete()
        return redirect('hola')

    return render(request, 'nucleo/confirmar_eliminar.html', {
        'tarea': tarea,
    })

#Realizado Por Jose Eduardo

def hola_mundo(request):
   
    q = request.GET.get('q', '').strip()

    if q:
        tareas = Tarea.objects.filter(
            Q(titulo__icontains=q) | Q(materia__icontains=q)
        ).order_by('fecha_entrega')
    else:
        tareas = Tarea.objects.all().order_by('fecha_entrega')

    
    rows_html = ""
    if tareas.exists():
        for i, t in enumerate(tareas, start=1):
            rows_html += f"""
                <tr>
                    <th>{i}</th>
                    <td>{t.titulo}</td>
                    <td>{t.materia}</td>
                    <td>{t.fecha_entrega}</td>
                    <td>{t.archivo}</td>
                    <td>
                        <a href="/tareas/{t.id}/editar/" class="btn btn-sm btn-warning me-1">
                            Editar
                        </a>
                        <a href="/tareas/{t.id}/eliminar/" class="btn btn-sm btn-danger">
                            Eliminar
                        </a>
                    </td>
                </tr>
            """
    else:
        rows_html = """
            <tr>
                <td colspan="5" class="text-center">No se encontraron tareas.</td>
            </tr>
        """

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>

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
                color: black !important;
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

                    <!-- Botón para ir al formulario de registro -->
                    <form class="d-flex" role="Buscar" action="/registro_tarea/" method="get">
                        <button class="btn ajustes-btn" type="submit">Registro Tareas</button>
                    </form>

                </div>
            </div>
        </nav>

        <div style='font-family: sans-serif; text-align: center; padding-top: 30px;'>
          <h1>¡Bienvenido a SchoolMate!</h1>
          <p>Plataforma ligera de cursos.</p>
        </div>

        <!-- BUSCADOR ENCIMA DE LA TABLA -->
        <div class="container my-3">
            <form method="get" class="d-flex justify-content-center mb-3" style="max-width: 500px; margin: 0 auto;">
                <div class="input-group">
                    <input class="form-control" type="search" name="q"
                           placeholder="Buscar tarea por título o materia..."
                           value="%%BUSQUEDA%%">
                    <button class="btn btn-dark" type="submit">Buscar</button>
                </div>
            </form>
        </div>

        <!-- TABLA DE TAREAS (DINÁMICA) -->
        <div class="container">
            <table class="table table-custom">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Título</th>
                    <th>Materia</th>
                    <th>Fecha de entrega</th>
                    <th> archivo </th>
                    <th>Acciones</th>
                </tr>
            </thead>

                <tbody class="table-group-divider">
                    %%ROWS%%
                </tbody>
            </table>
        </div>

        <!-- Lo demás de tu página lo dejo intacto -->
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
            <a href="#" class="link-opacity-100">https://nem.comenio.ai/mccems/conciencia-historica</a></p>

    </body>
    </html>
    """

    html_content = html_content.replace("%%ROWS%%", rows_html)
    html_content = html_content.replace("%%BUSQUEDA%%", q)

    return HttpResponse(html_content)
