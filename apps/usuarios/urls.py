from django.urls import path
from . import views
from apps.usuarios.views import *

urlpatterns = [
    path('registro/', views.RegisterView.as_view(), name='register'),
    path('', views.Login, name='login'),
    path('logout/', logout_view, name='logout'),
    
]    