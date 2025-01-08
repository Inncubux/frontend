from django.contrib import admin
from django.urls import path
from frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('', views.login, name='login'),
    path('home/administrar_alumno/', views.administrarAlumno, name='administrar alumno'),
    path('home/administrar_alumno/inscripcion_alumno/', views.inscripcionAlumno, name='inscripcion alumno'),
    path('home/administrar_alumno/eliminar_alumno/', views.eliminarAlumno, name = 'eliminar alumno'),
    path('home/administrar_alumno/modificar_alumno/',views.modificarAlumno, name = 'modificar alumno'),
    path('home/administrar_mentor/eliminar_alumno', views.administrarMentor, name='eliminar mentor'),
    path('home/administrar_alumno/solicitar_alumno_id/', views.solicitarAlumnoID, name='solicitarAlumnoID'),
    path('success/', views.success, name='success'),
    path('home/administrar_asignaturas/visualizar_asignaturas/', views.visualizarAsignaturas, name='visualizar asignaturas'),
    path('home/administrar_asignaturas/crear_asignatura/', views.crearAsignatura, name='crear asignatura'),
    path('home/administrar_asignaturas/eliminar_asignatura/', views.eliminarAsignatura, name='eliminar asignatura'),
    path('home/administrar_asignaturas/', views.administrarAsignaturas, name='administrar asignaturas'),
    path('alumno', views.home, name='alumno'),
    path('asignatura', views.verAsignaturas, name='ver asignaturas'),
]
