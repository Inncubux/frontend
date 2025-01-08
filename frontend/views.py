from django.shortcuts import render, get_object_or_404
import requests

from frontend.models import Alumno

def login(request):
    """
    Manejar solicitudes de inicio de sesión de usuarios.
    Esta función de vista procesa solicitudes POST para autenticar usuarios 
    basándose en el nombre de usuario y la contraseña proporcionados. Si el 
    método de solicitud es POST, recupera el 'username' y 'password' de los 
    datos POST de la solicitud.
    Args:
        request (HttpRequest): El objeto de solicitud HTTP que contiene 
                            metadatos sobre la solicitud.
    Returns:
        HttpResponse: La plantilla 'login.html' renderizada.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        request.session['username'] = username
        request.session['role'] = 'admin'
        
    return render(request, 'login.html')

def home(request):
    return render(request, 'eliminar_alumno.html')

def inscripcionAlumno(request):
    
    return render(request, 'inscripcionAlumno.html')

def administrarAlumno(request):
    return render(request, 'adm_alumnos.html')

def eliminarAlumno(request):
    """
    Manejar la eliminación de un alumno de la base de datos.
    Si el método de solicitud es POST, recupera el ID del alumno de los datos POST,
    elimina el registro correspondiente del alumno de la base de datos y redirige a una página de éxito.
    Si el método de solicitud no es POST, recupera todos los registros de alumnos y renderiza la
    plantilla 'eliminar_alumno.html' con la lista de alumnos.
    Args:
        request (HttpRequest): El objeto de solicitud HTTP.
    Returns:
        HttpResponse: Una redirección a la página de éxito si se elimina un alumno,
                      o una página HTML renderizada con la lista de alumnos.
    """
    if request.method == 'POST':
        alumno_id = request.POST['alumno']
        Alumno.objects.filter(id=alumno_id).delete()
        return redirect('success') 

    alumnos = Alumno.objects.all()
    return render(request, 'eliminar_alumno.html', {'alumnos': alumnos})



def modificarAlumno(request):
    alumno_id = request.POST.get('alumno')
    alumno = get_object_or_404(Alumno, id=alumno_id)
    if request.method == 'POST':
        alumno.nombre = request.POST.get('nombre')
        alumno.email_institucional = request.POST.get('email_institucional')
        alumno.email_personal = request.POST.get('email_personal')
        alumno.save()
        return redirect('alumno_list')  # Cambia esto al nombre de tu vista de lista de alumnos
    else:
        alumno_id = request.GET.get('alumno_id')  # Obtener el ID del alumno desde los parámetros de la URL
        alumno = get_object_or_404(Alumno, id=alumno_id)
        return render(request, 'modificar_alumno.html', {'alumno': alumno})

def administrarMentor(request):
    return render(request, 'adm_mentores.html')



def success(request):
    """
    Maneja la vista de éxito.

    Esta vista renderiza la plantilla 'success.html' cuando se realiza una solicitud.

    Args:
        request (HttpRequest): El objeto de solicitud HTTP.

    Returns:
        HttpResponse: La plantilla 'success.html' renderizada.
    """
    return render(request, 'success.html')

