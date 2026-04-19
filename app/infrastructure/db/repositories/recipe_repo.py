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


def agregar_receta(nombre_producto: str, rendimiento: int) -> int | None:
    """Agrega una nueva receta a la tabla receta

    Args:
        nombre_producto (str): El nombre del producto a agregar.
        rendimiento (int): Unidades que produce la receta.

    Returns:
        int | None: El ID de la receta agregada o None si no se pudo agregar.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO receta (nombre_producto, rendimiento) VALUES (?, ?)",
        (nombre_producto, rendimiento)
    )

    conn.commit()
    receta_id = cursor.lastrowid
    conn.close()
    return receta_id

def agregar_ingrediente_a_receta(receta_id: int, materia_prima_id: int, cantidad: float) -> None:
    """Agrega un ingrediente a una receta en la tabla receta_ingrediente

    Args:
        receta_id (int): El ID de la receta a la que se le agregará el ingrediente.
        materia_prima_id (int): El ID de la materia prima que se agregará como ingrediente.
        cantidad (float): La cantidad de la materia prima que se usará en la receta.

    Returns:
        None
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO receta_ingrediente (receta_id, materia_prima_id, cantidad) VALUES (?, ?, ?)",
        (receta_id, materia_prima_id, cantidad)
    )

    conn.commit()
    conn.close()