# libros/models.py
from django.db import models
from categorias.models import Categoria

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=1)  # Nuevo campo

    # Extra: campo de imagen de portada (opcional)
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)

    def __str__(self):
        return self.titulo