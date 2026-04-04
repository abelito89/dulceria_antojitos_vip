from ..services.cost_service import calcular_costo_receta
from .views.costos_view import costos_view
from ..services.material_service import agregar_materia_prima_service


def calcular_click(e,resultado_container,receta_dropdown,page) -> None:
    """Callback para que al presionar el boton calcular en la UI se ejecute el cálculo de costos y se muestre el resultado.

    Args:
        e (_type_): Evento de clic del botón de cálculo
        resultado_container (_type_): Contenedor donde se mostrará el resultado del cálculo de costos
        receta_dropdown (_type_): Dropdown para seleccionar la receta
        page (_type_): Página de Flet para actualizar la UI después de mostrar el resultado

    Raises:
        ValueError: _description_
    """
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


def agregar_materia_prima_click(e, nombre_input, unidad_base_input, unidad_consumo_input, factor_input, resultado,page) -> None:
    """Callback para que al presionar el boton guardar en la UI se ejecute el insert en db

    Args:
        e (_type_): _description_
        nombre_input (_type_): _description_
        unidad_base_input (_type_): _description_
        unidad_consumo_input (_type_): _description_
        factor_input (_type_): _description_
        resultado (_type_): _description_
        page (_type_): _description_
    """
    try:
        agregar_materia_prima_service(
            nombre_input.value,
            unidad_base_input.value,
            unidad_consumo_input.value,
            float(factor_input.value) if factor_input.value else 1
        )
        resultado.value = "Materia prima agregada correctamente"
        
    
    except Exception as ex:
        resultado.value = "Error: " + str(ex)
    page.update()