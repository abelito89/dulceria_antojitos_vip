import flet as ft
from .components.layout import create_app_layout

# ... tus otros imports

def main(page: ft.Page):
    page.title = "Costos Dulcería"
    # Alineación básica
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.add(create_app_layout(page))

ft.app(target=main)


