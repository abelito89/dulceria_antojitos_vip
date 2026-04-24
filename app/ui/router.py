import flet as ft
from ui.views.costos_view import build_calculadora_view
from ui.views.materiales_view import build_materiales_view, build_consultar_materiales_view
from ui.views.compras_view import build_lot_view
from ui.views.recetas_view import build_recetas_view
from ui.callbacks import calcular_click, agregar_receta_click, agregar_ingrediente_click
from services.material_service import listar_materiales_service

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
        2: lambda: build_consultar_materiales_view(page),
        3: lambda: build_lot_view(page),
        4: lambda: build_recetas_view(page, listar_materiales_service(), agregar_receta_click, agregar_ingrediente_click)
    }
    return views.get(index, lambda: ft.Text("Vista no encontrada"))()