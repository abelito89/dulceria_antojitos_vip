import flet as ft
from ui.callbacks import (
    agregar_materia_prima_click,
    buscar_materia_prima_click,
    seleccionar_materia_prima_click,
)
from ui.theme import Colors, Sizes, Alignments, Typography

colores = Colors()
sizes = Sizes()
alignments = Alignments()
typography = Typography()


def build_materiales_view(page: ft.Page):
    nombre_input = ft.TextField(label="Nombre de la materia prima", bgcolor=colores.BACKGROUND, border=ft.InputBorder.NONE)
    unidad_base_input = ft.TextField(label="Unidad base (ej: kg, l, etc.)", bgcolor=colores.BACKGROUND, border=ft.InputBorder.NONE)
    unidad_consumo_input = ft.TextField(label="Unidad de consumo (ej: g, ml, etc.)", bgcolor=colores.BACKGROUND, border=ft.InputBorder.NONE)
    factor_input = ft.TextField(
        label="Factor de conversión a unidad base (ej: 1000 para g a kg)",
        bgcolor=colores.BACKGROUND,
        border=ft.InputBorder.NONE
    )

    resultado = ft.Text()

    boton_guardar = ft.ElevatedButton(
        "Guardar",bgcolor=colores.PRIMARY, color=colores.TEXT, height=44, width=sizes.FORM_WIDTH,
        on_click=lambda e: agregar_materia_prima_click(
            e,
            nombre_input,
            unidad_base_input,
            unidad_consumo_input,
            factor_input,
            resultado,
            page,
        ),
    )
    texto_agregar_materia_prima = ft.Text("Agregar nueva materia prima", style=typography.SUBTITLE)
    columna_build_materiales_view = ft.Column(
        [
            texto_agregar_materia_prima,
            nombre_input,
            unidad_base_input,
            unidad_consumo_input,
            factor_input,
            boton_guardar,
            resultado,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
    )
    return columna_build_materiales_view


# ui/views/materiales_view.py
def build_consultar_materiales_view(page: ft.Page):
    search_input = ft.TextField(label="Buscar materia prima", bgcolor=colores.BACKGROUND, border=ft.InputBorder.NONE)
    ITEM_HEIGHT = 50  # puedes ajustar luego si tus items son más altos

    lista = ft.ListView(
        spacing=5,
        item_extent=ITEM_HEIGHT
    )

    lista_container = ft.Container(
        content=lista,
        height=ITEM_HEIGHT * 3,  # 👈 máximo 3 visibles
        alignment=ft.Alignment.CENTER,
    )
    resultado = ft.Text()

    # Nuevo: Contenedor donde se mostrarán los datos completos al seleccionar
    columna_detalle_resultado = ft.Column()

    # Función interna para manejar la selección sin ensuciar el callback de búsqueda
    def handle_materia_seleccionada(materia):
        seleccionar_materia_prima_click(materia, columna_detalle_resultado, page)

    # El callback de búsqueda ahora debe pasar la función de selección
    search_input.on_change = lambda e: buscar_materia_prima_click(
        e,
        search_input,
        lista,  # Pasamos el ListView dentro del contenedor
        resultado,
        page,
        on_select_fn=handle_materia_seleccionada,  # Pasamos el manejador
    )
    texto_consultar_materias_primas = ft.Text("Consultar materias primas", style=typography.SUBTITLE)


    columna_texto_consultar_materias_primas = ft.Container(
        content=ft.Column(
            [
                texto_consultar_materias_primas,
                search_input,
                lista_container,
                resultado,
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        expand=True,
        alignment=ft.Alignment.TOP_CENTER,
        width=sizes.FORM_WIDTH
    
    )

    columna_build_consultar_materiales_view = ft.Column(
        [
            columna_texto_consultar_materias_primas,

            ft.Container(content=columna_detalle_resultado, expand=1, padding=20),
        ],
        expand=True,
        alignment=alignments.COLUMN_MAIN,
        horizontal_alignment=alignments.COLUMN_CROSS
    )
    container_build_consultar_materiales_view = ft.Container(
        content=columna_build_consultar_materiales_view,
        expand=True,
        padding=80,
        bgcolor=colores.SURFACE,
        border_radius=10
    )
    return container_build_consultar_materiales_view
