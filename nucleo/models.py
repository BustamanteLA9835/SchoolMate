from django.db import models


from django.db import models

class Tarea(models.Model):

    titulo = models.CharField(max_length=200)


    materia = models.CharField(max_length=100)


    grado = models.CharField(max_length=2)

    fecha_entrega = models.DateField()

    estado = models.CharField(max_length=20)

    descripcion = models.TextField(blank=True)

    archivo = models.FileField(upload_to='tareas/', blank=True, null=True)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} - {self.materia}"
