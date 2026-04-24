import flet as ft
from ui.callbacks import agregar_materia_prima_click, buscar_materia_prima_click,seleccionar_materia_prima_click

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




# ui/views/materiales_view.py
def build_consultar_materiales_view(page: ft.Page):
    search_input = ft.TextField(label="Buscar materia prima")
    lista = ft.Column()
    resultado = ft.Text()
    
    # Nuevo: Contenedor donde se mostrarán los datos completos al seleccionar
    detalle_resultado = ft.Column()

    # Función interna para manejar la selección sin ensuciar el callback de búsqueda
    def handle_materia_seleccionada(materia):
        seleccionar_materia_prima_click(materia, detalle_resultado, page)

    # El callback de búsqueda ahora debe pasar la función de selección
    search_input.on_change = lambda e: buscar_materia_prima_click(
        e, search_input, lista, resultado, page, 
        on_select_fn=handle_materia_seleccionada # Pasamos el manejador
    )

    return ft.Row( # Usamos Row para ver lista a la izquierda y detalles a la derecha
        [
            ft.Column([
                ft.Text("Consultar materias primas"),
                search_input,
                lista,
                resultado
            ], expand=1),
            ft.VerticalDivider(),
            ft.Container(detalle_resultado, expand=1, padding=20)
        ],
        expand=True
    )
    