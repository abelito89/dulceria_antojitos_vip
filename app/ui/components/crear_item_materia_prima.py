import flet as ft



def crear_item_materia_prima(materia: dict, on_select) -> ft.Container:
    """Crea un control de Flet que representa una materia prima en la lista de resultados de búsqueda."""
    return ft.Container(
        content=ft.Text(value=materia["nombre"]),
        on_click=lambda e: on_select(materia), # Llamamos a la función que nos pasen
        padding=10
    )

