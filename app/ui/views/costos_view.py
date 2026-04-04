import flet as ft
from ...services.recipe_service import listar_recetas



def build_calculadora_view(page: ft.Page, calcular_click):
    
    recetas = listar_recetas()
    dropdown = ft.Dropdown(
        label="Selecciona una receta",
        width=250,
        options=[
            ft.dropdown.Option(
                key=str(r["id"]),
                text=r["nombre"]
            )
            for r in recetas
        ]
    )
    resultado_container = ft.Container()
    receta_dropdown = dropdown
    # Botón
    boton = ft.ElevatedButton("Calcular", on_click=lambda e: calcular_click(e, resultado_container, receta_dropdown, page))
    return ft.Column([
        ft.Text("Ingrese el ID de la receta para calcular su costo"),
        receta_dropdown,
        boton,
        resultado_container
    ], 
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    alignment=ft.MainAxisAlignment.CENTER,
    spacing=15
    )


def costos_view(resultado):

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(f"Producto: {resultado['nombre_producto']}",weight=ft.FontWeight.BOLD, size=18),
                ft.Text(f"Costo total: {resultado['costo_total']:.2f}", weight=ft.FontWeight.BOLD, size=16),
                ft.Text(f"Costo unitario: {resultado['costo_unitario']:.2f}", weight=ft.FontWeight.BOLD, size=14)
            ]
        )
    )
        