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


def crear_lote(materia_prima_nombre_input: str, cantidad_inicial: float, precio_unitario: float, fecha_compra: str) -> None:
    """Realiza una inserción SQL para agregar un nuevo lote a la base de datos con los datos proporcionados.

    Args:
        - materia_prima_nombre_input (str): El nombre de la materia prima para la cual se desea crear un nuevo lote.
        - cantidad_inicial (int): La cantidad inicial del lote.
        - cantidad_disponible (int): La cantidad disponible del lote.
        - precio_unitario (float): El precio unitario del lote.
        - fecha_compra (str): La fecha de compra del lote.

    Returns:
        - None: No devuelve ningún valor.
    """

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO lotes (
            materia_prima_id,
            cantidad_inicial,
            cantidad_disponible,
            precio_unitario,
            fecha_compra
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            materia_prima_nombre_input,
            cantidad_inicial,
            cantidad_inicial,  # cantidad_disponible se inicializa con el mismo valor que cantidad_inicial
            precio_unitario,
            fecha_compra
        )
    )
    conn.commit()

    conn.close()
