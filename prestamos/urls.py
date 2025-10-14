from django.urls import path
from . import views

app_name = 'prestamos'

urlpatterns = [
    path('', views.PrestamoListView.as_view(), name='lista'),
    path('crear/', views.PrestamoCreateView.as_view(), name='crear'),
    path('editar/<int:pk>/', views.PrestamoUpdateView.as_view(), name='editar'),
    path('borrar/<int:pk>/', views.PrestamoDeleteView.as_view(), name='borrar'),
    path('devolver/<int:pk>/', views.marcar_como_devolver, name='devolver'),
]