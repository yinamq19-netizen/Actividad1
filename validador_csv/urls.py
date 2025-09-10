from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargar_csv, name='cargar_csv'),
]
