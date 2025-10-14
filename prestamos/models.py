from django.db import models
from django.conf import settings
from libros.models import Libro

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    devuelto = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Si es un nuevo préstamo
        if not self.pk:
            # Verifica stock
            if self.libro.stock < 1:
                raise ValueError("No hay stock disponible para este libro.")
            # Resta 1 al stock
            self.libro.stock -= 1
            self.libro.save()
        else:
            # Si se está editando y se marca como devuelto
            original = Prestamo.objects.get(pk=self.pk)
            if not original.devuelto and self.devuelto:
                self.libro.stock += 1
                self.libro.save()
            # Si se desmarca como devuelto (no deberías permitirlo, pero por si acaso)
            if original.devuelto and not self.devuelto:
                if self.libro.stock < 1:
                    raise ValueError("No hay stock disponible para volver a prestar el libro.")
                self.libro.stock -= 1
                self.libro.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.libro} prestado a {self.usuario}"