import flet as ft
from ui.callbacks import agregar_materia_prima_click

def build_materiales_view(page: ft.Page):
    nombre_input = ft.TextField(label="Nombre de la materia prima")
    unidad_base_input = ft.TextField(label="Unidad base (ej: kg, l, etc.)")
    unidad_consumo_input = ft.TextField(label="Unidad de consumo (ej: g, ml, etc.)")
    factor_input = ft.TextField(label="Factor de conversión a unidad base (ej: 1000 para g a kg)")

    resultado = ft.Text()

    boton = ft.ElevatedButton(
        "Guardar",
        on_click=lambda e: agregar_materia_prima_click(e, nombre_input, unidad_base_input, unidad_consumo_input, factor_input, resultado, page)
    )
    return ft.Column(
        [
            ft.Text("Agregar nueva materia prima"),
            nombre_input,
            unidad_base_input,
            unidad_consumo_input,
            factor_input,
            boton,
            resultado
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER
    )
        


    