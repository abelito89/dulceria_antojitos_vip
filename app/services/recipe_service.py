from infrastructure.db.repositories.recipe_repo import obtener_recetas, agregar_receta, agregar_ingrediente_a_receta

def listar_recetas() -> list:
    """Ejecuta la funcion obtener_recetas() y devuelve la lista retornada

    Returns:
        list: Lista total de recetas
    """

    listado_recetas = obtener_recetas()
    return listado_recetas

def agregar_nueva_receta(nombre_producto: str, rendimiento: int) -> int | None:
    """Ejecuta la funcion agregar_receta() para agregar una nueva receta

    Args:
        nombre_producto (str): El nombre del producto a agregar.
        rendimiento (int): Unidades que produce la receta.

    Returns:
        int | None: El ID de la receta agregada o None si no se pudo agregar.
    """
    id =agregar_receta(nombre_producto, rendimiento)
    return id

def agregar_ingrediente(receta_id: int, materia_prima_id: int, cantidad: float) -> None:
    """Ejecuta la funcion agregar_ingrediente_a_receta() para agregar un ingrediente a una receta

    Args:
        receta_id (int): El id de la receta a la que se le agregará el ingrediente.
        materia_prima_id (int): El id de la materia prima que se agregará como ingrediente.
        cantidad (float): La cantidad de materia prima que se agregará como ingrediente.

    Returns:
        None
    """
    agregar_ingrediente_a_receta(receta_id, materia_prima_id, cantidad)