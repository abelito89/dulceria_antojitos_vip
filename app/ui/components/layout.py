import flet as ft
from ui.router import get_view_by_index
from ui.theme import Colors

colors = Colors()

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

    rail_visible = True

    def toggle_rail(e):
        nonlocal rail_visible

        rail_visible = not rail_visible
        rail_section.width = 120 if rail_visible else 0

        page.update()

    nav_rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.CALCULATE, label=ft.Text("Calculadora de costos", color=colors.TEXT)),
            ft.NavigationRailDestination(icon=ft.Icons.INVENTORY, label=ft.Text("Agregar materias primas", color=colors.TEXT)),
            ft.NavigationRailDestination(icon=ft.Icons.INVENTORY, label=ft.Text("Consultar materias primas", color=colors.TEXT)),
            ft.NavigationRailDestination(icon=ft.Icons.SHOPPING_CART, label=ft.Text("Compras", color=colors.TEXT)),
            ft.NavigationRailDestination(icon=ft.Icons.MENU_BOOK, label=ft.Text("Crear recetas", color=colors.TEXT))

        ],
        on_change=handle_route_change,
        bgcolor=colors.BACKGROUND
    )

    # Carga inicial manual
    content_area.content = get_view_by_index(0, page)

    icon_button =  ft.IconButton(
        icon=ft.Icons.MENU,
        on_click=toggle_rail
    )

    columna = ft.Column(
        controls=[
            icon_button
        ],
        expand=True
    )

    rail_section = ft.Container(
        content=ft.Row(
            [
                nav_rail,
                ft.VerticalDivider(width=1)
            ],
            spacing=0
        ),
        width=200  # aquí controlas el ancho del rail
    )

    fila = ft.Row(
        controls=[
            rail_section,
            columna,
            content_area
        ],
        expand=True
    )

    return fila