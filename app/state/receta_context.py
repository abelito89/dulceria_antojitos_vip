_receta_id_activa = None


def set_receta_activa(page, receta_id: int | None):
    """Establece la receta activa en el contexto global. 
    Esto permite que otras partes de la aplicación sepan cuál es la receta actualmente en edición o visualización.
    """
    global _receta_id_activa
    _receta_id_activa = receta_id


def get_receta_activa(page):
    """Devuelve el ID de la receta actualmente activa. Si no hay ninguna receta activa, devuelve None.
     Esto es útil para mantener el estado de la receta que se está editando o visualizando en la aplicación.
    """
    return _receta_id_activa


def clear_receta_activa(page):
    """Limpia la receta activa del contexto global. Esto se puede usar cuando se finaliza la edición de una receta o se cancela la operación, para asegurarse de que no quede un estado residual.
    """
    global _receta_id_activa
    _receta_id_activa = None