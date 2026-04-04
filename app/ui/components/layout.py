import flet as ft
from ..router import get_view_by_index

def create_app_layout(page: ft.Page) -> ft.Row:
    """Crea el layout principal de la aplicación con una barra de navegación lateral y un área de contenido.

    Args:
        page (ft.Page): La página de Flet donde se agregará el layout.

    Returns:
        ft.Row: El layout principal de la aplicación.
    """
    # El contenedor donde cambiaremos el contenido
    content_area = ft.Container(expand=True)

    def handle_route_change(e) -> None:
        """Maneja el cambio de ruta en la barra de navegación lateral.

        Args:
            e (_type_): El evento de cambio de selección en la barra de navegación.
        """
        # Usamos el índice del control que disparó el evento
        content_area.content = get_view_by_index(e.control.selected_index, page)
        page.update()

    nav_rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.CALCULATE, label="Calculadora"),
            ft.NavigationRailDestination(icon=ft.Icons.INVENTORY, label="Materias primas"),
        ],
        on_change=handle_route_change
    )

    # Carga inicial manual
    content_area.content = get_view_by_index(0, page)

    # Retornamos el Row directamente, que es lo que pide page.add()
    return ft.Row(
        controls=[
            nav_rail,
            ft.VerticalDivider(width=1),
            content_area
        ],
        expand=True
    )