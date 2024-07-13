from django.urls import path
from . import views
from apps.asesores.views import *

urlpatterns = [
    # Funcionario prestamos
    path('home/', views.homeView.as_view(), name='index'),
]