from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Prestamo
from .forms import PrestamoForm

class PrestamoListView(ListView):
    model = Prestamo
    template_name = 'prestamos/prestamo_list.html'
    context_object_name = 'prestamos'
    paginate_by = 5

class PrestamoCreateView(CreateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'prestamos/prestamo_form.html'
    success_url = reverse_lazy('prestamos:lista')

class PrestamoUpdateView(UpdateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'prestamos/prestamo_form.html'
    success_url = reverse_lazy('prestamos:lista')

class PrestamoDeleteView(DeleteView):
    model = Prestamo
    template_name = 'prestamos/prestamo_confirm_delete.html'
    success_url = reverse_lazy('prestamos:lista')
    
    
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

def marcar_como_devolver(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if not prestamo.devuelto:
        prestamo.devuelto = True
        prestamo.save()  # Esto ya actualiza el stock por la lógica del modelo
        messages.success(request, "¡Préstamo marcado como devuelto!")
    else:
        messages.info(request, "El préstamo ya estaba marcado como devuelto.")
    return redirect('prestamos:lista')    