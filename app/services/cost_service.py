from ..infrastructure.db.repositories.recipe_repo import (
    get_receta,
    get_ingredientes_by_receta,
)

from ..infrastructure.db.repositories.lot_repo import (
    get_max_price_available,
)
from ..services.unit_service import consumo_a_base
from ..infrastructure.db.repositories.material_repo import (
    get_unidades_by_materia_prima,
)


def calcular_costo_receta(receta_id: int):
    receta = get_receta(receta_id)

    if receta is None:
        raise ValueError("La receta no existe")

    ingredientes = get_ingredientes_by_receta(receta_id)

    if not ingredientes:
        raise ValueError("La receta no tiene ingredientes")

    costo_total = 0
    detalle = []

    for ingrediente in ingredientes:
        materia_prima_id = ingrediente["materia_prima_id"]
        cantidad = ingrediente["cantidad"]



        precio = get_max_price_available(materia_prima_id)

        if precio is None:
            raise ValueError(
                f"No hay stock disponible para materia_prima_id={materia_prima_id}"
            )

        # Obtener unidades del insumo
        unidades = get_unidades_by_materia_prima(materia_prima_id)

        factor = unidades["factor_conversion"]

        # Convertir cantidad a unidad_base
        cantidad_en_base = consumo_a_base(cantidad, factor)

        # Calcular costo correctamente
        costo = cantidad_en_base * precio


        costo_total += costo

        detalle.append({
            "materia_prima_id": materia_prima_id,
            "cantidad_consumo": cantidad,
            "unidad_consumo": unidades["unidad_consumo"],
            "cantidad_base": cantidad_en_base,
            "unidad_base": unidades["unidad_base"],
            "precio_unitario": precio,
            "costo": costo,
        })

    rendimiento = receta["rendimiento"]

    if rendimiento <= 0:
        raise ValueError("El rendimiento debe ser mayor que 0")

    costo_unitario = costo_total / rendimiento

    return {
        "receta_id": receta_id,
        "nombre_producto": receta["nombre_producto"],
        "costo_total": costo_total,
        "costo_unitario": costo_unitario,
        "detalle": detalle,
    }