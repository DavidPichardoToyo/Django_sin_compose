from django.urls import path, include
from .views import hola, listar_productos

urlpatterns = [
    path("", hola, name="hola"),
    path("productos/", listar_productos, name="listar_productos")
]