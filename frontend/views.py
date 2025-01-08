from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
import requests

from frontend.models import Alumno, Asignatura  # Import Asignatura model

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
        try:
            if username == 'admin' and password == 'admin':
                request.session['username'] = username
                request.session['role'] = 'admin'
                return redirect('home')
            else:
                request.session['role'] = 'alumno'
                return redirect('alumno')
            
        except Exception as e:
            messages.error(request, 'Error: No se pudo iniciar sesión. Inténtalo de nuevo.')
            return render(request, 'login.html')
        
    return render(request, 'login.html')

def home(request):
    if request.session.get('username') is None:
        return redirect('login')
    
    try:
        role = request.session['role']
        if role == 'admin':
            return render(request, 'home_adm.html')
        if role == 'alumno':
            return render(request, 'home.html')
    except Exception as e:
        return render(request, 'home.html')
    
    
def inscripcionAlumno(request):
    
    return render(request, 'inscripcionAlumno.html')

def administrarAlumno(request):
    alumnos = Alumno.objects.all()
    return render(request, 'adm_alumnos.html', {'alumnos': alumnos})

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
        alumno = get_object_or_404(Alumno, id=alumno_id)
        alumno.delete()
        messages.success(request, 'Alumno eliminado exitosamente.')
        return redirect('success') 

    alumnos = Alumno.objects.all()
    return render(request, 'eliminar_alumno.html', {'alumnos': alumnos})

def modificarAlumno(request):
    """
    Manejar la modificación de los datos de un alumno específico.
    Si el método de solicitud es POST, actualiza los datos del alumno con los valores proporcionados.
    Si el método de solicitud no es POST, recupera los datos del alumno y renderiza la plantilla 'modificar_alumno.html'.
    Args:
        request (HttpRequest): El objeto de solicitud HTTP.
    Returns:
        HttpResponse: Una redirección a la lista de alumnos si se modifica un alumno,
                      o una página HTML renderizada con los datos del alumno.
    """
    alumno_id = request.GET.get('alumno_id')
    if not alumno_id:
        return redirect('administrarAlumno')  # Redirigir si falta el ID del alumno

    alumno = get_object_or_404(Alumno, id=alumno_id)
    if request.method == 'POST':
        alumno.nombre = request.POST.get('nombre')
        alumno.email_institucional = request.POST.get('email_institucional')
        alumno.email_personal = request.POST.get('email_personal')
        alumno.save()
        return redirect('administrar alumno') # Redirigir a la vista de lista de alumnos
    else:
        return render(request, 'modificar_alumno.html', {'alumno': alumno})

def solicitarAlumnoID(request):
    """
    Solicitar el ID del alumno para modificar sus datos.
    Renderiza una plantilla que solicita al usuario ingresar el ID del alumno.
    Args:
        request (HttpRequest): El objeto de solicitud HTTP.
    Returns:
        HttpResponse: La plantilla 'solicitar_alumno_id.html' renderizada.
    """
    if request.method == 'POST':
        alumno_id = request.POST.get('alumno_id')
        return redirect(f'/home/administrar_alumno/modificar_alumno/?alumno_id={alumno_id}')
    return render(request, 'solicitar_alumno_id.html', {'show_modal': True, 'alumno_id': request.POST.get('alumno_id', '')})

def administrarMentor(request):
    return render(request, 'adm_mentores.html')

def visualizarAsignaturas(request):
    """
    Manejar la visualización de todas las asignaturas.
    Recupera todos los registros de asignaturas y renderiza la plantilla 'visualizar_asignaturas.html'.
    Args:
        request (HttpRequest): El objeto de solicitud HTTP.
    Returns:
        HttpResponse: La plantilla 'visualizar_asignaturas.html' renderizada con la lista de asignaturas.
    """
    asignaturas = Asignatura.objects.all()
    return render(request, 'visualizar_asignaturas.html', {'asignaturas': asignaturas})

def crearAsignatura(request):
    """
    Manejar la creación de una nueva asignatura.
    Si el método de solicitud es POST, crea una nueva asignatura con los datos proporcionados.
    Si el método de solicitud no es POST, renderiza la plantilla 'crear_asignatura.html'.
    Args:
        request (HttpRequest): El objeto de solicitud HTTP.
    Returns:
        HttpResponse: Una redirección a la lista de asignaturas si se crea una asignatura,
                      o una página HTML renderizada con el formulario de creación de asignatura.
    """
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        horas = request.POST.get('horas')
        seccion = request.POST.get('seccion')
        Asignatura.objects.create(nombre=nombre, horas=horas, seccion=seccion)
        return redirect('visualizar asignaturas')  # Redirigir a la vista de lista de asignaturas
    return render(request, 'crear_asignatura.html')

def eliminarAsignatura(request):
    """
    Manejar la eliminación de una asignatura de la base de datos.
    Si el método de solicitud es POST, recupera el nombre y la sección de la asignatura de los datos POST,
    elimina el registro correspondiente de la asignatura de la base de datos y redirige a la página de administración de asignaturas.
    Si el método de solicitud no es POST, renderiza la plantilla 'eliminar_asignatura.html'.
    Args:
        request (HttpRequest): El objeto de solicitud HTTP.
    Returns:
        HttpResponse: Una redirección a la página de administración de asignaturas si se elimina una asignatura,
                      o una página HTML renderizada con el formulario de eliminación de asignatura.
    """
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        seccion = request.POST.get('seccion')
        try:
            asignatura = Asignatura.objects.get(nombre=nombre, seccion=seccion)
            asignatura.delete()
            messages.success(request, 'Asignatura eliminada exitosamente.')
            return redirect('administrar asignaturas')  # Redirigir a la vista de administración de asignaturas
        except Asignatura.DoesNotExist:
            messages.error(request, 'Error: No se encontró la asignatura con el nombre y sección proporcionados.')

    return render(request, 'eliminar_asignatura.html')

def administrarAsignaturas(request):
    """
    Renderizar la página de administración de asignaturas.
    Args:
        request (HttpRequest): El objeto de solicitud HTTP.
    Returns:
        HttpResponse: La plantilla 'adm_asignaturas.html' renderizada.
    """
    return render(request, 'adm_asignaturas.html')

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

def verAsignaturas(request):
    """
    Manejar la visualización de todas las asignaturas.
    Recupera todos los registros de asignaturas y renderiza la plantilla 'ver_asignaturas.html'.
    Args:
        request (HttpRequest): El objeto de solicitud HTTP.
    Returns:
        HttpResponse: La plantilla 'ver_asignaturas.html' renderizada con la lista de asignaturas.
    """
    asignaturas = Asignatura.objects.all()
    return render(request, 'asignaturas.html', {'asignaturas': asignaturas})

