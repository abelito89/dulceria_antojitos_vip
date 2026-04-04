from ..services.cost_service import calcular_costo_receta
from .views.costos_view import costos_view


def calcular_click(e,resultado_container,receta_dropdown,page):
        try:
            if not receta_dropdown.value:
                raise ValueError("Seleccione una receta")

            receta_id = int(receta_dropdown.value)
            resultado = calcular_costo_receta(receta_id)
            resultado_container.content = costos_view(resultado)
            
        except Exception as ex:
            resultado_container.content = costos_view({
            "nombre_producto": "Error: " + str(ex),
            "costo_total": 0,
            "costo_unitario": 0
        })

        page.update()