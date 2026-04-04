import flet as ft
from .callbacks import calcular_click


def main(page: ft.Page):
    page.title = "Costos Dulcería"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.add(ft.Text("Ingrese el ID de la receta para calcular su costo"))
    # Input para ID de receta
    receta_input = ft.TextField(label="ID Receta", width=200)

    # Resultado
    resultado_container = ft.Container()

    # Botón
    boton = ft.ElevatedButton("Calcular", on_click=lambda e: calcular_click(e, resultado_container, receta_input, page))

    page.add(
        ft.Column([
            receta_input,
            boton,
            resultado_container
        ])
    )