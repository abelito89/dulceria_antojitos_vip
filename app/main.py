from .infrastructure.db.db import init_db
import flet as ft
from .ui.ui import main as ui_main

def main():
    """Función principal que inicializa la base de datos y muestra un mensaje de confirmación.
    """
    init_db()
    print("Base de datos inicializada")
    ft.run(ui_main, view=ft.AppView.WEB_BROWSER)

if __name__ == "__main__":
    main()