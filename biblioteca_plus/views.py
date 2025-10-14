from django.shortcuts import render
from libros.models import Libro, Categoria
from django.core.paginator import Paginator
from django.db.models import Count

def home(request):
    libros_list = Libro.objects.all().select_related('categoria')
    paginator = Paginator(libros_list, 5)
    page_number = request.GET.get('page')
    libros = paginator.get_page(page_number)

    categorias = Categoria.objects.annotate(num_libros=Count('libro'))

    return render(request, 'home.html', {
        'libros': libros,
        'categorias': categorias,
    })