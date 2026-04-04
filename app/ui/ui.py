import flet as ft
from .callbacks import calcular_click


def main(page: ft.Page):
    page.title = "Costos Dulcería"
   
    page.add(
        ft.Text("Ingrese el ID de la receta para calcular su costo"),
        )
    # Input para ID de receta
    receta_input = ft.TextField(label="ID Receta", width=200)

    # Resultado
    resultado_text = ft.Text()

    # Botón
    calcular_click(None, resultado_text, receta_input, page)

    boton = ft.ElevatedButton("Calcular", on_click=lambda e: calcular_click(e, resultado_text, receta_input, page))

    page.add(
        ft.Column([
            receta_input,
            boton,
            resultado_text
        ])
    )