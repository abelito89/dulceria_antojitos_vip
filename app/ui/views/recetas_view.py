import flet as ft

class RecetaState:
    def __init__(self):
        self.receta_id: int = -1

def build_recetas_view(page: ft.Page, lista_materiales, agregar_receta_cb, agregar_ingrediente_cb):
    state = RecetaState()
    nombre_input = ft.TextField(label="Nombre del producto")
    rendimiento_input = ft.TextField(label="Rendimiento (unidades que produce la receta)")

    resultado = ft.Text()
    ingredientes_container = ft.Column(visible=True)
    materia_prima_input = ft.Dropdown(
        label="Selecciona un ingrediente (materia prima)",
        width=250,
        options=[
            ft.dropdown.Option(
                key=str(m["id"]),
                text=m["nombre"]
            )
            for m in lista_materiales
        ]
    )
    cantidad_input = ft.TextField(label="Cantidad")
    
    def on_agregar_ingrediente(e, state, materia_prima_input, cantidad_input, resultado, page, agregar_ingrediente_cb):
        """Maneja el evento de agregar ingrediente a la receta. Valida los campos y llama al callback para agregar el ingrediente.
         Requiere que la receta ya haya sido guardada para tener un ID válido.
        """
        try:
            if state.receta_id == -1:
                resultado.value = "Primero debes guardar la receta"
                page.update()
                return

            if not materia_prima_input.value:
                resultado.value = "Selecciona una materia prima"
                page.update()
                return

            if not cantidad_input.value or not cantidad_input.value.replace(".", "", 1).isdigit():
                resultado.value = "Cantidad inválida"
                page.update()
                return
            receta_id = state.receta_id

            agregar_ingrediente_cb(e, receta_id, materia_prima_input.value, cantidad_input.value, resultado, page)

            materia_prima_input.value = None
            cantidad_input.value = ""
            page.update()
        except Exception as ex:
            resultado.value = f"Error al agregar ingrediente: {str(ex)}"
            page.update()
        
    def on_guardar(e, state, nombre_input, rendimiento_input, resultado, page, ingredientes_container, btn_add, agregar_receta_cb):
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
                state.receta_id = receta_id
                ingredientes_container.visible = True
                btn_add.disabled = False
                btn_confirmar.disabled = False
                boton.disabled = True  # 🔴 bloquea nuevas recetas

        except Exception as ex:
            resultado.value = f"Error al guardar: {str(ex)}"

        page.update()

    def on_confirmar(e, state, nombre_input, rendimiento_input, materia_prima_input, cantidad_input, resultado, btn_add, btn_confirmar, boton, page):
        # Reset estado
        state.receta_id = -1

        # Limpiar inputs
        nombre_input.value = ""
        rendimiento_input.value = ""
        materia_prima_input.value = None
        cantidad_input.value = ""

        # Reset UI
        btn_add.disabled = True
        btn_confirmar.disabled = True
        boton.disabled = False

        resultado.value = "Receta confirmada correctamente"

        page.update()
        
    btn_add = ft.ElevatedButton(
        "Agregar ingrediente",
        on_click=lambda e: on_agregar_ingrediente(e, state, materia_prima_input, cantidad_input, resultado, page, agregar_ingrediente_cb),
        disabled=True
    )

    btn_confirmar = ft.ElevatedButton(
        "Confirmar receta",
        disabled=True
    )
    btn_confirmar.on_click = lambda e: on_confirmar(e, state, nombre_input, rendimiento_input, materia_prima_input, cantidad_input, resultado, btn_add, btn_confirmar, boton, page)

    ingredientes_container.controls = [
        ft.Text("Agregar ingredientes a la receta"),
        materia_prima_input,
        cantidad_input,
        btn_add,
        btn_confirmar
    ]

    boton = ft.ElevatedButton(
        "Guardar",
        on_click=lambda e: on_guardar(e, state, nombre_input, rendimiento_input, resultado, page, ingredientes_container, btn_add, agregar_receta_cb)
    )

    return ft.Column(
        [
            ft.Text("Agregar nueva receta"),
            nombre_input,
            rendimiento_input,
            boton,
            resultado,
            ft.Divider(),  # línea visual
            ingredientes_container 
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER
    )