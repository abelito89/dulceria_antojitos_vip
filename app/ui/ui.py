import flet as ft
from .components.layout import create_app_layout

# ... tus otros imports

def main(page: ft.Page) -> None:
    """Función principal que configura la página de Flet y muestra el layout de la aplicación.

    Args:
        page (ft.Page): Página de Flet que se pasará automáticamente al ejecutar la aplicación.
    """
    page.title = "Costos Dulcería"
    # Alineación básica
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.add(create_app_layout(page))

ft.app(target=main)


