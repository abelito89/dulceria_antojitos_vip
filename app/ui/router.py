import flet as ft
from ui.views.costos_view import build_calculadora_view
from ui.views.materiales_view import build_materiales_view
from ui.views.compras_view import build_lot_view
from ui.callbacks import calcular_click

def get_view_by_index(index: int, page: ft.Page) -> ft.Control:
    """Devuelve la vista correspondiente al índice seleccionado en la barra de navegación lateral.

    Args:
        index (int): Índice del destino seleccionado en la barra de navegación lateral.
        page (ft.Page): La página de Flet donde se mostrará la vista

    Returns:
        ft.Control: El control que representa la vista correspondiente
    """
    # Mapeo simple: Índice -> Función constructora
    views = {
        0: lambda: build_calculadora_view(page, calcular_click),
        1: lambda: build_materiales_view(page),
        2: lambda: build_lot_view(page)

    }
    return views.get(index, lambda: ft.Text("Vista no encontrada"))()