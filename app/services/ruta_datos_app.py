import appdirs
from pathlib import Path

def get_app_data_path() -> Path:
    """
    Retorna la ruta de datos de la aplicación, compatible con desktop y Android.
    
    Usa `appdirs` que automáticamente retorna:
    - Windows: C:\\Users\\<user>\\AppData\\Local\\Dulceria
    - Linux:   ~/.local/share/dulceria
    - macOS:   ~/Library/Application Support/Dulceria
    - Android: Maneja automáticamente el directorio seguro de Flet
    
    Returns:
        Path: Ruta absoluta para almacenar datos (creada si no existe).
    """
    app_data = appdirs.user_data_dir("Dulceria")
    data_dir = Path(app_data)
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir