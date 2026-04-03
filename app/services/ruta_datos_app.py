from pathlib import Path
def get_app_data_path() -> Path:
    """Devuelve una ruta escribible para la app.
    En escritorio: carpeta local 'data'.
    En futuro móvil: se puede adaptar sin romper nada.

    Returns:
        Path: La ruta escribible para la app.
    """
    base_path = Path.cwd() / "data"
    base_path.mkdir(parents=True, exist_ok=True)
    return base_path