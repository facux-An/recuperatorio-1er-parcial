from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('', views.LibroListView.as_view(), name='lista'),
    path('crear/', views.LibroCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', views.LibroUpdateView.as_view(), name='editar'),
    path('borrar/<int:pk>/', views.LibroDeleteView.as_view(), name='borrar'),
]