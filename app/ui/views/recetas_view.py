import flet as ft



def build_recetas_view(
    page: ft.Page,
    lista_materiales,
    agregar_receta_cb,
    agregar_ingrediente_cb
    ):
    def create_state():
        return {
            "receta_id": -1
        }
    state = create_state()
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
    
    def on_agregar_ingrediente(e):
        receta_id = state["receta_id"]
        print(f"TIPO RECETA: {type(receta_id)}")
        agregar_ingrediente_cb(
            e,
            receta_id,
            materia_prima_input.value,
            cantidad_input.value,
            resultado,
            page        
        )
        materia_prima_input.value = None
        cantidad_input.value = ""
        page.update()
        

    def on_guardar(e):
        receta_id = agregar_receta_cb(
            e,
            nombre_input,
            rendimiento_input,
            resultado,
            page
        )
        if receta_id:
            state["receta_id"] = receta_id
            # 1. Cambiamos el estado
            ingredientes_container.visible = True
            btn_add.disabled = False
        page.update()
        
    btn_add=ft.ElevatedButton(
    "Agregar ingrediente",
    on_click=on_agregar_ingrediente,
    disabled=True
    )    

    ingredientes_container.controls = [
    ft.Text("Agregar ingredientes a la receta"),

    materia_prima_input,
    cantidad_input,
    btn_add

    ]

    boton = ft.ElevatedButton("Guardar", on_click=on_guardar)

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