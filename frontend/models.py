from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(max_length=30)
    horas = models.IntegerField()
    seccion = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length= 30)
    email_institucional = models.CharField(max_length= 30)
    email_personal = models.CharField(max_length= 30)

    def __str__(self):
        return self.nombre
    
class AlumnoContraseña(models.Model):
    email_institucional = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30, blank=True)  # blank=True para permitir que se genere automáticamente
    rol = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        # Generar contraseña a partir del email institucional si no está ya definida
        if not self.contraseña:
            self.contraseña = self.email_institucional.split('@')[0]
        super().save(*args, **kwargs)  # Llamar al método save del padre

    def __str__(self):
        return f"{self.email_institucional} - {self.rol}"

class Mentor(models.Model):
    nombre = models.CharField(max_length=30)
    email_institucional = models.CharField(max_length= 30)
    email_personal = models.CharField(max_length= 30)

    def __str__(self):
        return self.nombre

class Mentoria(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.asignatura.nombre} - {self.alumno.nombre}"

