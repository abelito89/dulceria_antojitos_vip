import flet as ft
from services.recipe_service import listar_recetas
from typing import Callable, Dict, Any
from ui.theme import Colors, Sizes, Typography, Alignments
from ui.theme_helpers import confirm_button,body_text,heading3, success_text

colores = Colors()
sizes = Sizes()
typography = Typography()
alignments = Alignments()



def build_calculadora_view(page: ft.Page, calcular_click: Callable) -> ft.Control:
    """Construye la vista de la calculadora de costos, que incluye un dropdown para seleccionar una receta y un botón para calcular su costo.

    Args:
        page (ft.Page): Página
        calcular_click (Callable): La función a llamar cuando se haga clic en el botón de cálculo

    Returns:
        ft.Control: La vista de la calculadora de costos
    """
    
    recetas = listar_recetas()
    dropdown = ft.Dropdown(
        label="Selecciona una receta",
        width=250,
        options=[
            ft.dropdown.Option(
                key=str(r["id"]),
                text=r["nombre"]
            )
            for r in recetas
        ],
        bgcolor=colores.BACKGROUND
    )
    resultado_container = ft.Container()
    receta_dropdown = dropdown

    boton =confirm_button("Calcular", on_click=lambda e: calcular_click(e, resultado_container, receta_dropdown, page) )
    return ft.Column([
        body_text("Ingrese el nombre de la receta para calcular su costo"),
        receta_dropdown,
        boton,
        resultado_container
    ], 
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    alignment=ft.MainAxisAlignment.CENTER,
    spacing=15
    )


def costos_view(resultado: Dict[str, Any]) -> ft.Control:
    """Construye la vista que muestra el resultado del cálculo de costos, incluyendo el nombre del producto, costo total y costo unitario.

    Args:
        resultado (Dict[str, Any]): El diccionario con los resultados del cálculo de costos.

    Returns:
        ft.Control: La vista que muestra el resultado del cálculo de costos.
    """
    return ft.Container(
        content=ft.Column(
            [
                heading3(f"Producto: {resultado['nombre_producto']}"),
                success_text(f"Costo total: ${resultado['costo_total']:.2f}"),
                body_text(f"Costo unitario: ${resultado['costo_unitario']:.2f}")
            ]
        )
    )

        