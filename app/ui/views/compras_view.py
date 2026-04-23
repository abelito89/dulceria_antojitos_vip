import flet as ft
from ui.callbacks import agregar_lote_click
from services.material_service import listar_materiales_service

def build_lot_view(page:ft.Page):

    lista_materiales = listar_materiales_service()
    dropdown = ft.Dropdown(
        label="Selecciona una materia prima",
        width=250,
        options=[
            ft.dropdown.Option(
                key=str(m["id"]),
                text=m["nombre"]
            )
            for m in lista_materiales
        ]
    )
    text_unidad = ft.Text("Unidad: (se determina por la materia prima seleccionada)", color="yellow")

    materia_prima_nombre_input=dropdown
    
    cantidad_inicial_input=ft.TextField(label="Cantidad inicial (en unidad base del producto)", width=200)
    precio_unitario_input=ft.TextField(label="Precio unitario (por unidad base)", width=200)
    fecha_compra_input=ft.TextField(label="Fecha de compra", width=200)

    boton = ft.ElevatedButton(
        "Guardar",
        on_click=lambda e: agregar_lote_click(e,materia_prima_nombre_input, cantidad_inicial_input, precio_unitario_input, fecha_compra_input,page) 
    )
    return ft.Column(
        [
            ft.Text("Agregar nuevo lote"),
            materia_prima_nombre_input,
            text_unidad,
            cantidad_inicial_input,
            precio_unitario_input,
            fecha_compra_input,
            boton
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER
    )