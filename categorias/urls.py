from django.urls import path
from . import views

app_name = 'categorias'

urlpatterns = [
    path('', views.CategoriaListView.as_view(), name='lista'),
    path('crear/', views.CategoriaCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', views.CategoriaUpdateView.as_view(), name='editar'),
    path('borrar/<int:pk>/', views.CategoriaDeleteView.as_view(), name='borrar'),
]