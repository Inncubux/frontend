import os
import sys
import django
import pandas as pd

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from frontend.models import Alumno, Mentor, Asignatura, Mentoria

def importar_desde_excel(ruta_archivo):
    datos = pd.read_excel(ruta_archivo, engine='openpyxl')
    print("Columnas en el DataFrame:", datos.columns)

    # Crear asignaturas
    asignaturas = {}
    for _, fila in datos.iterrows():
        asignatura_nombre = str(fila[' ASIGNATURA']).strip()
        if asignatura_nombre not in asignaturas:
            asignatura = Asignatura.objects.create(
                nombre=asignatura_nombre,
                horas=int(fila[' HORAS']),
                seccion=str(fila[' SECCION']).strip()
            )
            asignaturas[asignatura_nombre] = asignatura

    # Crear mentores
    mentores = {}
    for _, fila in datos.iterrows():
        mentor_nombre = str(fila['NOMBRE']).strip() if not pd.isna(fila['NOMBRE']) else None
        if mentor_nombre and mentor_nombre not in mentores:
            mentor = Mentor.objects.create(
                nombre=mentor_nombre.strip(),
                email_institucional=str(fila[' E-MAIL nadian']).strip() if not pd.isna(fila[' E-MAIL nadian']) else '',
                email_personal=str(fila[' E-MAIL PERSONAL']).strip() if not pd.isna(fila[' E-MAIL PERSONAL']) else ''
            )
            mentores[mentor_nombre] = mentor

    # Crear alumnos
    alumnos = {}
    for _, fila in datos.iterrows():
        alumno_nombre = str(fila[' NOMBRE2']).strip() if not pd.isna(fila[' NOMBRE2']) else None
        if alumno_nombre and alumno_nombre not in alumnos:
            alumno = Alumno.objects.create(
                nombre=alumno_nombre,
                email_institucional=str(fila[' E-MAIL nadian']).strip() if not pd.isna(fila[' E-MAIL nadian']) else '',
                email_personal=str(fila[' E-MAIL PERSONAL']).strip() if not pd.isna(fila[' E-MAIL PERSONAL']) else ''
            )
            alumnos[alumno_nombre] = alumno

    # Crear mentorías
    for _, fila in datos.iterrows():
        mentor_nombre = str(fila['NOMBRE']).strip() if not pd.isna(fila['NOMBRE']) else None
        alumno_nombre = str(fila[' NOMBRE2']).strip() if not pd.isna(fila[' NOMBRE2']) else None
        asignatura_nombre = str(fila[' ASIGNATURA']).strip()
        
        mentor = mentores.get(mentor_nombre)
        alumno = alumnos.get(alumno_nombre)
        asignatura = asignaturas.get(asignatura_nombre)
        
        if mentor and alumno and asignatura:
            Mentoria.objects.create(
                mentor=mentor,
                alumno=alumno,
                asignatura=asignatura
            )

if __name__ == "__main__":
    ruta_archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Cleaned_Proyecto_Integrador.xlsx')
    importar_desde_excel(ruta_archivo)
    print("Datos importados con éxito!")
