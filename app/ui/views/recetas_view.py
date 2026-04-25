import flet as ft
from state.receta_context import get_receta_activa, set_receta_activa, clear_receta_activa
from ui.theme import Colors, Spacing, Sizes, Typography, Alignments
from ui.handlers.recetas_handlers import on_agregar_ingrediente

colores = Colors()
espaciados = Spacing()
sizes = Sizes()
tipografia = Typography()
alignments = Alignments()


def build_ingredientes_section(materia_prima_input, cantidad_input, btn_add, btn_confirmar):
    """
    Construye la sección de UI para agregar ingredientes a una receta.

    Args:
        materia_prima_input: Campo de entrada para seleccionar la materia prima.
        cantidad_input: Campo de entrada para la cantidad del ingrediente.
        btn_add: Botón para añadir el ingrediente.
        btn_confirmar: Botón para confirmar la lista de ingredientes.

    Returns:
        ft.Column: Contenedor con los controles de ingredientes.
    """
    return ft.Container(
        content=ft.Column(
                    [
                        ft.Container(
                            ft.Text("Agregar", style = tipografia.SUBTITLE),
                                    padding=espaciados.MD,
                                    border_radius=sizes.RADIUS,
                                    width=sizes.FORM_WIDTH
                        ),
                        materia_prima_input,
                        cantidad_input,
                        btn_add,
                        btn_confirmar
                    ],
                    visible=True
        ),
        padding=espaciados.MD,
        border_radius=sizes.RADIUS,
        bgcolor="blues",
        width=sizes.FORM_WIDTH
    )

def build_receta_form(nombre_input, rendimiento_input, boton, resultado):
    """
    Construye el formulario de creación de una receta.

    Args:
        nombre_input: Campo de entrada para el nombre de la receta.
        rendimiento_input: Campo de entrada para el rendimiento de la receta.
        boton: Botón de acción para guardar o crear la receta.
        resultado: Control donde se muestra el resultado o feedback de la operación.

    Returns:
        ft.Column: Contenedor con los controles del formulario de receta.
    """
    return ft.Container(
                content=ft.Column(
                            [
                                ft.Container(
                                    ft.Text(
                                        "Agregar nueva receta", 
                                        style=tipografia.SUBTITLE,
                                        color=colores.TEXT,
                                        text_align=tipografia.ALIGN_LEFT,
                                        expand=True
                                    ),
                                    padding=espaciados.MD,
                                    width=sizes.FORM_WIDTH,
                                    bgcolor="blue"
                                ),
                                nombre_input,
                                rendimiento_input,
                                boton,
                                resultado,
                                ft.Divider()
                            ],
                            horizontal_alignment=alignments.COLUMN_CROSS,
                            alignment=alignments.COLUMN_MAIN                         
                ),
                padding=espaciados.MD,
                border_radius=sizes.RADIUS,
                width=1200
                
    )

def build_recetas_view(page: ft.Page, lista_materiales, agregar_receta_cb, agregar_ingrediente_cb):
    """
    Construye la vista principal de gestión de recetas.

    Permite crear una receta, agregar ingredientes asociados a ella y
    gestionar su estado de edición dentro de la UI.

    Args:
        page (ft.Page): Página principal de Flet para actualización de UI.
        lista_materiales (list): Lista de materias primas disponibles para selección.
        agregar_receta_cb (callable): Callback para persistir una nueva receta.
        agregar_ingrediente_cb (callable): Callback para añadir ingredientes a una receta existente.

    Returns:
        ft.Column: Vista completa de creación y edición de recetas.
    """
    nombre_input = ft.TextField(label="Nombre del producto")
    rendimiento_input = ft.TextField(label="Rendimiento (unidades que produce la receta)")

    resultado = ft.Text()
    ingredientes_container = ft.Column(visible=True)
    materia_prima_input = ft.Container(
                content=ft.Dropdown(
                    label="Ingrediente",
                    width=250,
                    options=[
                        ft.dropdown.Option(
                            key=str(m["id"]),
                            text=m["nombre"]
                        )
                        for m in lista_materiales
                    ],
                    
                   
                ),
                width=sizes.FORM_WIDTH,
                
    )
    cantidad_input = ft.TextField(label="Cantidad")

        
    def on_guardar(e, nombre_input, rendimiento_input, resultado, page, ingredientes_container, btn_add, agregar_receta_cb):
        """Maneja el evento de guardar la receta. Valida los campos, llama al callback para agregar 
        la receta y actualiza el estado para permitir agregar ingredientes.
        """
        try:
            if not nombre_input.value or not nombre_input.value.strip():
                resultado.value = "El nombre es obligatorio"
                page.update()
                return

            if not rendimiento_input.value or not rendimiento_input.value.isdigit():
                resultado.value = "El rendimiento debe ser un número"
                page.update()
                return

            receta_id = agregar_receta_cb(e, nombre_input, rendimiento_input, resultado, page)

            if receta_id:
                set_receta_activa(page, receta_id)
                ingredientes_container.visible = True
                btn_add.disabled = False
                boton_confirmar_receta.disabled = False
                boton_guardar.disabled = True  # 🔴 bloquea nuevas recetas

        except Exception as ex:
            resultado.value = f"Error al guardar: {str(ex)}"

        page.update()

    def on_confirmar(e, nombre_input, rendimiento_input, materia_prima_input, cantidad_input, resultado, btn_add, btn_confirmar, boton, page):
        """
        Confirma la receta actual y resetea el estado de creación.

        Limpia los campos del formulario, deshabilita los controles de
        ingredientes y restablece el estado interno de la receta.
        """
        # Reset estado
        clear_receta_activa(page)

        # Limpiar inputs
        nombre_input.value = ""
        rendimiento_input.value = ""
        materia_prima_input.content.value = None
        materia_prima_input.content.update()
        cantidad_input.value = ""

        # Reset UI
        btn_add.disabled = True
        btn_confirmar.disabled = True
        boton.disabled = False

        resultado.value = "Receta confirmada correctamente"
        resultado.update()
        page.update()
        
    boton_agregar_ingrediente = ft.ElevatedButton(
        "Agregar",bgcolor=colores.PRIMARY, color=colores.TEXT, height=44, 
        on_click=lambda e: on_agregar_ingrediente(
            e,
            materia_prima_input,
            cantidad_input,
            resultado,
            page,
            agregar_ingrediente_cb
        ),
        disabled=True
    )

    boton_confirmar_receta = ft.ElevatedButton(
        "Confirmar",bgcolor=colores.PRIMARY, color=colores.TEXT, height=44,
        disabled=True
    )


    boton_confirmar_receta.on_click = lambda e: on_confirmar(e, nombre_input, rendimiento_input, materia_prima_input, cantidad_input, resultado, boton_agregar_ingrediente, boton_confirmar_receta, boton_guardar, page)

    ingredientes_container = build_ingredientes_section(
        materia_prima_input,
        cantidad_input,
        boton_agregar_ingrediente,
        boton_confirmar_receta
    )
    boton_guardar = ft.ElevatedButton(
        "Guardar",bgcolor=colores.PRIMARY, color=colores.TEXT, height=44, width=sizes.FORM_WIDTH,
        on_click=lambda e: on_guardar(e, nombre_input, rendimiento_input, resultado, page, ingredientes_container, boton_agregar_ingrediente, agregar_receta_cb)
    )
    receta_id = get_receta_activa(page)

    if receta_id:
        boton_agregar_ingrediente.disabled = False
        boton_confirmar_receta.disabled = False
        boton_guardar.disabled = True

    return ft.Container(
        content=ft.Column(
            [
                build_receta_form(
                    nombre_input,
                    rendimiento_input,
                    boton_guardar,
                    resultado
                ),
                ingredientes_container
            ],
            horizontal_alignment=alignments.COLUMN_CROSS,
            alignment=alignments.COLUMN_MAIN,
        ),
        padding=espaciados.MD,
        border_radius=sizes.RADIUS,
        bgcolor=colores.SURFACE
    )