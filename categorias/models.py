from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre