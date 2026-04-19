import flet as ft
from services.material_service import listar_materiales_service
from ui.callbacks import agregar_receta_click, agregar_ingrediente_click



def build_recetas_view(page: ft.Page):
    receta_actual = {"id": -1}
    nombre_input = ft.TextField(label="Nombre del producto")
    rendimiento_input = ft.TextField(label="Rendimiento (unidades que produce la receta)")

    resultado = ft.Text()
    ingredientes_container = ft.Column(visible=True)
    lista_materiales = listar_materiales_service()
    dropdown = ft.Dropdown(
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
    materia_prima_input = dropdown
    cantidad_input = ft.TextField(label="Cantidad")
    
    def on_agregar_ingrediente(e):
        receta_id = receta_actual["id"]
        print(f"TIPO RECETA: {type(receta_id)}")
        agregar_ingrediente_click(
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
        receta_id = agregar_receta_click(
            e,
            nombre_input,
            rendimiento_input,
            resultado,
            page
        )
        print(f"RECETA ID: {receta_id}")
        # Si se guardó correctamente
        if receta_id:
            receta_actual["id"] = receta_id
            # 1. Cambiamos el estado
            ingredientes_container.visible = True
        

    ingredientes_container.controls = [
    ft.Text("Agregar ingredientes a la receta"),

    materia_prima_input,
    cantidad_input,

    ft.ElevatedButton(
        "Agregar ingrediente",
        on_click=on_agregar_ingrediente
    )
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
            ingredientes_container  # 👈 aparece después de guardar
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER
    )