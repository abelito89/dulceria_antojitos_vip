from .infrastructure.db.db import init_db
import flet as ft
from .ui.ui import main as ui_main

def main(page: ft.Page):
    init_db()
    print("Base de datos inicializada")
    ui_main(page)  # reutilizas tu lógica actual

if __name__ == "__main__":
    ft.run(main)