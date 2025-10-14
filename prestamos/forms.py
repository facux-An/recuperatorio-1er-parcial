from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro', 'usuario', 'fecha_devolucion', 'devuelto']

    def clean(self):
        cleaned_data = super().clean()
        libro = cleaned_data.get('libro')
        devuelto = cleaned_data.get('devuelto', False)

        
        if self.instance.pk is None and libro and libro.stock < 1:
            raise forms.ValidationError("¡No hay stock disponible para este libro!")
        return cleaned_data