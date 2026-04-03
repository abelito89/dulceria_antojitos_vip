from infrastructure.db.repositories.recipe_repo import (
    get_receta,
    get_ingredientes_by_receta,
)

from infrastructure.db.repositories.lot_repo import (
    get_max_price_available,
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

        costo = cantidad * precio
        costo_total += costo

        detalle.append({
            "materia_prima_id": materia_prima_id,
            "cantidad": cantidad,
            "precio_usado": precio,
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