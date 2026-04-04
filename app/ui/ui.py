import flet as ft
from .views.costos_view import build_calculadora_view
from .views.materiales_view import build_materiales_view
from .callbacks import calcular_click

# ... tus otros imports

def main(page: ft.Page):
    page.title = "Costos Dulcería"
    # Alineación básica
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    # 1. Definimos el contenedor de contenido con expand=True 
    # para que ocupe el resto del ancho en el Row
    content = ft.Container(expand=True)
    
    def cambiar_vista(index):
        if index == 0:
            content.content = build_calculadora_view(page, calcular_click)
        elif index == 1:
            content.content = build_materiales_view(page)
        page.update() # Importante actualizar para ver el cambio de vista

    # 2. Definimos el NavigationRail
    nav = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        extended=False,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.CALCULATE,
                label="Calculadora"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.INVENTORY,
                label="Materias primas"
            ),
        ],
        on_change=lambda e: cambiar_vista(e.control.selected_index)
    )

    # Carga inicial de la primera vista
    cambiar_vista(0)

    # 3. La clave: Metemos todo en un Row con expand=True
    page.add(
        ft.Row(
            [
                nav,
                ft.VerticalDivider(width=1), # Opcional: una línea divisoria
                content,
            ],
            expand=True, # Esto soluciona el error de "unbounded height"
        )
    )

ft.app(target=main)


