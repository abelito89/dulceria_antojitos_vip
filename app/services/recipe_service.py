from ..infrastructure.db.repositories.recipe_repo import obtener_recetas

def listar_recetas() -> list:
    """Ejecuta la funcion obtener_recetas() y devuelve la lista retornada

    Returns:
        list: Lista total de recetas
    """

    listado_recetas = obtener_recetas()
    return listado_recetas