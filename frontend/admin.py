from django.contrib import admin
from .models import Asignatura, Alumno, Mentor, Mentoria

admin.site.register(Asignatura)
admin.site.register(Alumno)
admin.site.register(Mentor)
admin.site.register(Mentoria)
# Register your models here.
