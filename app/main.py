from infrastructure.db.db import init_db
import flet as ft
from ui.ui import main as ui_main
def main(page: ft.Page):
    try:
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