from ..db import get_connection


def get_unidades_by_materia_prima(materia_prima_id: int):
    """
    Devuelve las unidades y el factor de conversión de un insumo.
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


def insertar_materia_prima(nombre: str, unidad_base: str, unidad_consumo: str, factor_conversion: float):
    """
    Inserta una nueva materia prima en la base de datos.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO materia_prima (nombre, unidad_base, unidad_consumo, factor_conversion)
        VALUES (?, ?, ?, ?)
        """,
        (nombre, unidad_base, unidad_consumo, factor_conversion)
    )

    conn.commit()
    conn.close()