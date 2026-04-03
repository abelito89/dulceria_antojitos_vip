from infrastructure.db.db import get_connection


def get_max_price_available(materia_prima_id: int) -> float | None:
    """Realiza consulta SQL para obtener el precio máximo entre los lotes disponibles
    (cantidad_disponible > 0) para un insumo específico (materia_prima_id).

    Args:
        - materia_prima_id (int): El ID de la materia prima para la cual se desea obtener el precio máximo disponible.

    Returns:
        - float | None: El precio máximo disponible para la materia prima especificada, o None si no hay lotes disponibles.

    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT MAX(precio_unitario) as max_price
        FROM lotes
        WHERE materia_prima_id = ?
        AND cantidad_disponible > 0
        """,
        (materia_prima_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if row["max_price"] is None:
        return None

    return float(row["max_price"])