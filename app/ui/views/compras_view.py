import flet as ft
from ..callbacks import agregar_lote_click

def build_lot_view(page:ft.Page):
    materia_prima_id_input=ft.TextField(label="ID de la materia prima", width=200)
    cantidad_inicial_input=ft.TextField(label="Cantidad inicial", width=200)
    precio_unitario_input=ft.TextField(label="Precio unitario", width=200)
    fecha_compra_input=ft.TextField(label="Fecha de compra", width=200)

    boton = ft.ElevatedButton(
        "Guardar",
        on_click=lambda e: agregar_lote_click(e,materia_prima_id_input, cantidad_inicial_input, precio_unitario_input, fecha_compra_input,page) 
    )
    return ft.Column(
        [
            ft.Text("Agregar nuevo lote"),
            materia_prima_id_input,
            cantidad_inicial_input,
            precio_unitario_input,
            fecha_compra_input,
            boton
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER
    )