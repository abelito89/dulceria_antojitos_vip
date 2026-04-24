from services.cost_service import calcular_costo_receta
from ui.views.costos_view import costos_view
from services.material_service import agregar_materia_prima_service, buscar_materia_prima_service
from services.inventory_service import agregar_lote_service
from services.recipe_service import agregar_nueva_receta, agregar_ingrediente
from state.receta_context import set_receta_activa
import flet as ft


def calcular_click(e,resultado_container,receta_dropdown,page) -> None:
    """Callback para que al presionar el boton calcular en la UI se ejecute el cálculo de costos y se muestre el resultado.

    Args:
        e (_type_): Evento de clic del botón de cálculo
        resultado_container (_type_): Contenedor donde se mostrará el resultado del cálculo de costos
        receta_dropdown (_type_): Dropdown para seleccionar la receta
        page (_type_): Página de Flet para actualizar la UI después de mostrar el resultado

    Raises:
        ValueError: Si no se selecciona una receta antes de hacer clic en calcular.
    """
    try:
        if not receta_dropdown.value:
            raise ValueError("Seleccione una receta")

        receta_id = int(receta_dropdown.value)
        resultado = calcular_costo_receta(receta_id)
        resultado_container.content = costos_view(resultado)
        
    except Exception as ex:
        resultado_container.content = costos_view({
        "nombre_producto": "Error: " + str(ex),
        "costo_total": 0,
        "costo_unitario": 0
    })

    page.update()


def agregar_materia_prima_click(
    e: ft.Event,
    nombre_input: ft.TextField,
    unidad_base_input: ft.TextField,
    unidad_consumo_input: ft.TextField,
    factor_input: ft.TextField,
    resultado: ft.Text,
    page: ft.Page
) -> None:
    """Maneja el evento de agregar una nueva materia prima desde la UI.

    Toma los valores de los campos, ejecuta la inserción en la base de datos
    y muestra el resultado al usuario. Limpia los campos tras una operación exitosa.

    Args:
        e: Evento de clic del botón.
        nombre_input: Campo de texto con el nombre de la materia prima.
        unidad_base_input: Unidad en la que se adquiere la materia prima.
        unidad_consumo_input: Unidad en la que se consume en recetas.
        factor_input: Factor de conversión entre unidades.
        resultado: Control de texto donde se muestra el resultado.
        page: Página de Flet para actualizar la UI.
    """
    try:
        agregar_materia_prima_service(
            nombre_input.value,
            unidad_base_input.value,
            unidad_consumo_input.value,
            float(factor_input.value) if factor_input.value else 1.0
        )

        resultado.value = "Materia prima agregada correctamente"
        resultado.color = "green"

        # Limpiar campos
        nombre_input.value = ""
        unidad_base_input.value = ""
        unidad_consumo_input.value = ""
        factor_input.value = ""


    except Exception as ex:
        print("TIPO ERROR:", type(ex))
        print("ERROR:", ex)
        resultado.value = f"Error: {ex}"
        resultado.color = "red"

    page.update()

def agregar_lote_click(e,materia_prima_nombre_input, cantidad_inicial_input, precio_unitario_input, fecha_compra_input,page) -> None:
    """Construye la vista de compras, que permite al usuario agregar un nuevo lote a la base de datos.

    La función solicita al usuario que ingrese el ID de la materia prima, la cantidad inicial del lote, el precio unitario y la fecha de compra. Luego, llama a la función agregar_lote_service() para agregar el nuevo lote a la base de datos.

    Raises:
        ValueError: Si alguno de los parámetros ingresados por el usuario es inválido.
    """
    boton = e.control
    boton.disabled = True
    page.update()
    try:

        agregar_lote_service(
            materia_prima_nombre_input.value, 
            float(cantidad_inicial_input.value), 
            float(precio_unitario_input.value), 
            fecha_compra_input.value
        )
        print("Lote agregado exitosamente.")
            # 🔥 limpiar formulario
        materia_prima_nombre_input.value = None
        cantidad_inicial_input.value = ""
        precio_unitario_input.value = ""
        fecha_compra_input.value = ""
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        boton.disabled = False
    page.update()


def agregar_receta_click(
    e: ft.ControlEvent,
    nombre_producto_input: ft.TextField,
    rendimiento_input: ft.TextField,
    resultado: ft.Text,
    page: ft.Page
) -> int | None:
    """Maneja el evento de agregar una nueva receta desde la UI.

    Obtiene los valores de los controles de entrada, intenta crear la receta
    en la base de datos y muestra el resultado al usuario.

    Args:
        e: Evento de clic del botón.
        nombre_producto_input: Campo de texto con el nombre del producto.
        rendimiento_input: Campo de texto con el rendimiento de la receta.
        resultado: Control de texto donde se mostrará el mensaje al usuario.
        page: Página de Flet utilizada para refrescar la interfaz.

    Returns:
        int | None: ID de la receta creada si la operación fue exitosa,
        en caso contrario `None`.

    Raises:
        ValueError: Si el rendimiento no puede convertirse a entero.
        Exception: Cualquier error producido durante la inserción en la base de datos.
    """
    try:
        receta_id = agregar_nueva_receta(
            nombre_producto_input.value,
            int(rendimiento_input.value)
        )
        set_receta_activa(page, receta_id)
        nombre_producto_input.value = ""
        rendimiento_input.value = ""

        resultado.value = f"Receta agregada correctamente con ID: {receta_id}"
        resultado.color = "green"
        return receta_id

    except Exception as ex:
        resultado.value = f"Error: {ex}"
        resultado.color = "red"
        return None

    finally:
        page.update()


def agregar_ingrediente_click(
    e: ft.ControlEvent,
    receta_id: int,
    materia_prima_id: int | str | None,
    cantidad: float | str | None,
    resultado: ft.Text,
    page: ft.Page
) -> None:
    """Maneja el evento de agregar un ingrediente a una receta.

    Convierte y valida los valores provenientes de la UI, ejecuta la inserción
    en base de datos y actualiza el mensaje en pantalla.

    Args:
        e: Evento de clic del botón.
        receta_id: ID de la receta a la que se agregará el ingrediente.
        materia_prima_id: ID de la materia prima seleccionada (puede venir como
            string desde el Dropdown).
        cantidad: Cantidad ingresada por el usuario (puede venir como string).
        resultado: Control de texto donde se mostrará el mensaje al usuario.
        page: Página de Flet para refrescar la UI.

    Raises:
        ValueError: Si los valores no son convertibles a los tipos esperados.

    Returns:
        None
    """
    try:
        # Validaciones básicas
        if not materia_prima_id:
            raise ValueError("Debes seleccionar un ingrediente.")

        if not cantidad:
            raise ValueError("Debes introducir una cantidad.")

        # Conversión de tipos
        receta_id_int = int(receta_id)
        materia_prima_id_int = int(materia_prima_id)
        cantidad_float = float(cantidad)

        # Llamada al backend
        agregar_ingrediente(
            receta_id_int,
            materia_prima_id_int,
            cantidad_float
        )

        resultado.value = "Ingrediente agregado correctamente"
        resultado.color = "green"

    except Exception as ex:
        resultado.value = f"Error: {ex}"

    page.update()


def buscar_materia_prima_click(
    e: ft.Event,
    search_input: ft.TextField,
    lista: ft.Column,
    resultado: ft.Text,
    page: ft.Page
):
    """Callback para manejar la búsqueda de materias primas desde la UI.

    Esta función se ejecuta cuando el usuario ingresa texto en el campo de búsqueda
    y actualiza la lista de materias primas mostrada en la interfaz según el término
    ingresado.

    Args:
        e: Evento de cambio en el campo de búsqueda.
        search_input: Campo de texto donde el usuario ingresa el término de búsqueda.
        lista: Control de lista que muestra las materias primas filtradas.
        resultado: Control de texto donde se mostrará el mensaje al usuario.
        page: Página de Flet para actualizar la UI después de filtrar los resultados.

    Returns:
        None
    """
    lista_encontrada = buscar_materia_prima_service(search_input.value)
    if lista_encontrada:
        lista.controls = [ft.Text(m["nombre"]) for m in lista_encontrada]
        resultado.value = f"{len(lista_encontrada)} materia(s) prima(s) encontrada(s)"
        resultado.color = "green"
    else:
        lista.controls = []
        resultado.value = "No se encontraron materias primas que coincidan con la búsqueda."
        resultado.color = "red"