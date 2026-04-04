import flet as ft
from .views.costos_view import build_calculadora_view
from .views.materiales_view import build_materiales_view
from .callbacks import calcular_click

def get_view_by_index(index, page):
    # Mapeo simple: Índice -> Función constructora
    views = {
        0: lambda: build_calculadora_view(page, calcular_click),
        1: lambda: build_materiales_view(page),
    }
    return views.get(index, lambda: ft.Text("Vista no encontrada"))()