from infrastructure.db.repositories.material_repo import insertar_materia_prima, listar_materiales

def agregar_materia_prima_service(nombre: str, unidad_base: str, unidad_consumo: str, factor_conversion: float):
    """Ejecuta la funcion insertar_materia_prima() para agregar una nueva materia prima a la base de datos

    Args:
        nombre (str): Nombre de la materia prima
        unidad_base (str): Unidad base de la materia prima
        unidad_consumo (str): Unidad de consumo de la materia prima
        factor_conversion (float): Factor de conversión entre unidad_consumo y unidad_base
    Raises:
        ValueError: Si alguno de los parámetros es inválido
    """    
    if not nombre:
        raise ValueError("El nombre de la materia prima no puede estar vacío")
    if not unidad_base:
        raise ValueError("La unidad base no puede estar vacía")
    if not unidad_consumo:
        raise ValueError("La unidad de consumo no puede estar vacía")
    if factor_conversion <= 0:
        raise ValueError("El factor de conversión debe ser mayor que 0")
    
    insertar_materia_prima(nombre, unidad_base, unidad_consumo, factor_conversion)


def listar_materiales_service() -> list:
    """Ejecuta la función listar_materiales() para obtener una lista de todas las materias primas almacenadas en la base de datos.

    Returns:
        list: Una lista de nombres de materias primas.
    """

    return listar_materiales()