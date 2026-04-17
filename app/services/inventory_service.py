from infrastructure.db.repositories.lot_repo import crear_lote

def agregar_lote_service(materia_prima_nombre_input: str, cantidad_inicial: float, precio_unitario: float, fecha_compra: str) -> None:
    """Ejecuta la función crear_lote() para agregar un nuevo lote a la base de datos con los datos proporcionados.

    Args:
        materia_prima_id (int): El ID de la materia prima para la cual se desea crear un nuevo lote.
        cantidad_inicial (float): La cantidad inicial del lote.
        cantidad_disponible (int): La cantidad disponible del lote.
        precio_unitario (float): El precio unitario del lote.
        fecha_compra (str): La fecha de compra del lote.

    Raises:
        ValueError: Si alguno de los parámetros es inválido.
    """

    if materia_prima_nombre_input is None:
        raise ValueError("El ID de la materia prima debe ser mayor que 0")
    if cantidad_inicial <= 0:
        raise ValueError("La cantidad inicial debe ser mayor que 0")
    if precio_unitario <= 0:
        raise ValueError("El precio unitario debe ser mayor que 0")
    if not fecha_compra:
        raise ValueError("La fecha de compra no puede estar vacía")


    crear_lote(materia_prima_nombre_input, cantidad_inicial, precio_unitario, fecha_compra)