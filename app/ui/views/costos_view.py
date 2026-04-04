import flet as ft

def costos_view(resultado):

    return ft.Column(
        [
            ft.Text(f"Producto: {resultado['nombre_producto']}",weight=ft.FontWeight.BOLD),
            ft.Text(f"Costo total: {resultado['costo_total']:.2f}"),
            ft.Text(f"Costo unitario: {resultado['costo_unitario']:.2f}")
        ]
    )