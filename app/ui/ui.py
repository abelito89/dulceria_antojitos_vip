import flet as ft
from .views.costos_view import build_calculadora_view
from .callbacks import calcular_click


def main(page: ft.Page):
    page.title = "Costos Dulcería"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.add(build_calculadora_view(page, calcular_click))
    # Input para ID de receta


