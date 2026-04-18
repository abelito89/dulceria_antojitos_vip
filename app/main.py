from infrastructure.db.db import init_db
import flet as ft
from ui.ui import main as ui_main
from infrastructure.db.db import set_db_path
from pathlib import Path
import sys
import os


def get_base_path() -> Path:
    if "ANDROID_ARGUMENT" in os.environ:
        base = Path("/data/user/0/com.flet.app/files")
    elif sys.platform == "win32":
        base = Path(os.getenv("LOCALAPPDATA", Path.home()))
    else:
        base = Path.home() / ".local" / "share"

    return base

def main(page: ft.Page):
    try:
        # 👇 ruta nativa de Flet
        # 1. Instanciamos el servicio StoragePaths como indica tu terminal
        # Esto evita el DeprecationWarning y asegura compatibilidad con Flet 1.0
        sp = ft.StoragePaths()

        # 2. Agregamos el servicio a la página para que sea persistente en la sesión [6]
        page.services.append(sp)
    
        base_path = get_base_path()
        
        data_dir = base_path / "dulceria"
        data_dir.mkdir(parents=True, exist_ok=True)

        # 👇 configurar DB dinámicamente
        set_db_path(data_dir)

        init_db()

        page.add(ft.Text("DB OK"))

    except Exception as e:
        page.add(ft.Text(f"ERROR INIT_DB: {e}"))
        return

    try:
        ui_main(page)
    except Exception as e:
        page.add(ft.Text(f"ERROR UI: {e}"))


if __name__ == "__main__":
    ft.run(main)