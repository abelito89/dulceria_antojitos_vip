import flet as ft

def costos_view(resultado):

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(f"Producto: {resultado['nombre_producto']}",weight=ft.FontWeight.BOLD, size=18),
                ft.Text(f"Costo total: {resultado['costo_total']:.2f}", weight=ft.FontWeight.BOLD, size=16),
                ft.Text(f"Costo unitario: {resultado['costo_unitario']:.2f}", weight=ft.FontWeight.BOLD, size=14)
            ]
        )
    )
        