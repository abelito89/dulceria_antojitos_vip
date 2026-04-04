from ..services.cost_service import calcular_costo_receta


def calcular_click(e,resultado_text,receta_input,page):
        try:
            receta_id = int(receta_input.value)
            resultado = calcular_costo_receta(receta_id)

            resultado_text.value = f"""Producto: {resultado['nombre_producto']}
                            Costo total: {resultado['costo_total']}
                            Costo unitario: {resultado['costo_unitario']}
                            """
        except Exception as ex:
            resultado_text.value = f"Error: {str(ex)}"

        page.update()