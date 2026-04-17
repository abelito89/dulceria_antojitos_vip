from infrastructure.db.db import get_connection

def get_receta(receta_id: int) -> dict | None:
    """
    Obtiene una receta por su ID.

    Args:
        receta_id (int): El ID de la receta a obtener.

    Returns:
        dict | None: La receta encontrada o None si no se encuentra.

    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM receta WHERE id = ?",
        (receta_id,)
    )

    row = cursor.fetchone()
    conn.close()

    return row


def get_ingredientes_by_receta(receta_id: int) -> list:
    """
    Obtiene los ingredientes de una receta por su ID.

    Args:
        receta_id (int): El ID de la receta para la cual se desean obtener los ingredientes.

    Returns:
        list: Una lista de diccionarios con los ingredientes de la receta.

    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT materia_prima_id, cantidad
        FROM receta_ingrediente
        WHERE receta_id = ?
        """,
        (receta_id,)
    )

    rows = cursor.fetchall()
    conn.close()

    return rows

def obtener_recetas() -> list:
    """Obtiene una lista con el id y el nombre de todas las recetas disponibles en la tabla receta

    Returns:
        list: Lista de diccionarios con claves id y nombre.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre_producto FROM receta")

    rows = cursor.fetchall()
    conn.close()

    return [{"id": row["id"], "nombre": row["nombre_producto"]} for row in rows]