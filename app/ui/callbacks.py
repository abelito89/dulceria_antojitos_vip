from ..services.cost_service import calcular_costo_receta
from .views.costos_view import costos_view
import flet as ft


def calcular_click(e,costos,receta_input,page):
        try:
            receta_id = int(receta_input.value)
            resultado = calcular_costo_receta(receta_id)
            costos.content = costos_view(resultado)
            
        except Exception as ex:
            costos.content = ft.Text(f"Error: {str(ex)}")

        page.update()