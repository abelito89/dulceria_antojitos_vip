from state.receta_context import get_receta_activa

def on_agregar_ingrediente(e, materia_prima_input, cantidad_input, resultado_ingredientes, page, agregar_ingrediente_cb):
        """Maneja el evento de agregar ingrediente a la receta. Valida los campos y llama al callback para agregar el ingrediente.
         Requiere que la receta ya haya sido guardada para tener un ID válido.
        """
        receta_id = get_receta_activa(page)
        try:
            if not receta_id:
                resultado_ingredientes.value = "Primero debes guardar la receta"
                page.update()
                return

            if not materia_prima_input.content.value:
                resultado_ingredientes.value = "Selecciona una materia prima"
                page.update()
                return

            if not cantidad_input.value or not cantidad_input.value.replace(".", "", 1).isdigit():
                resultado_ingredientes.value = "Cantidad inválida"
                page.update()
                return
        

            agregar_ingrediente_cb(e, receta_id, materia_prima_input.content.value, cantidad_input.value, resultado_ingredientes, page)

            materia_prima_input.content.value = None
            cantidad_input.value = ""
            page.update()
        except Exception as ex:
            resultado_ingredientes.value = f"Error al agregar ingrediente: {str(ex)}"
            page.update()