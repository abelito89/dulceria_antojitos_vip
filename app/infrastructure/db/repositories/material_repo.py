from infrastructure.db.db import get_connection
from typing import Dict
import sqlite3

def get_unidades_by_materia_prima(materia_prima_id: int) -> Dict:
    """Realiza consulta SQL para obtener la unidad base, unidad de consumo y factor de conversión
    
    Args:
        materia_prima_id (int): El ID de la materia prima para la cual se desean obtener las unidades y el factor de conversión.
    
    Returns:
        Dict: Un diccionario con las claves 'unidad_base', 'unidad_consumo' y 'factor_conversion' con los valores correspondientes de la materia prima especificada.
    Raises:
        ValueError: Si no existe una materia prima con el ID proporcionado.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT 
            unidad_base, 
            unidad_consumo, 
            factor_conversion
        FROM materia_prima
        WHERE id = ?
        """,
        (materia_prima_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise ValueError(f"No existe materia_prima_id={materia_prima_id}")

    return row


def insertar_materia_prima(nombre: str, unidad_base: str, unidad_consumo: str, factor_conversion: float) -> None:
    """Realiza una inserción SQL para agregar una nueva materia prima a la base de datos con los datos proporcionados.

    Args:
        nombre (str): El nombre de la materia prima a insertar.
        unidad_base (str): La unidad base de la materia prima.
        unidad_consumo (str): La unidad de consumo de la materia prima.
        factor_conversion (float): El factor de conversión de la materia prima.
    Returns:
        None
    """

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO materia_prima (nombre_insumo, unidad_base, unidad_consumo, factor_conversion)
            VALUES (?, ?, ?, ?)
            """,
            (nombre, unidad_base, unidad_consumo, factor_conversion)
        )
        conn.commit()
    except sqlite3.IntegrityError as ex:
        raise ValueError("Ya existe una materia prima con ese nombre") from ex

    finally:
        conn.close()


def listar_materiales() -> list[Dict]:
    """Realiza una consulta SQL para obtener el id y nombre de todas las materias primas disponibles en la tabla materia_prima

    Returns:
        list: Una lista de diccionarios con las claves 'id' y 'nombre' para cada materia prima.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, nombre_insumo
        FROM materia_prima
        """
    )

    rows = cursor.fetchall()
    
    conn.close()

    return [{"id": row["id"], "nombre": row["nombre_insumo"]} for row in rows]