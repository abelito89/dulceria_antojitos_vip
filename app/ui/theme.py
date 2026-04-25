# theme.py
import flet as ft

class Colors:
    PRIMARY = "#F8230B"
    PRIMARY_LIGHT = "#A7681C"
    BACKGROUND = "#370606"
    SURFACE = "#0B0101"
    TEXT = "#FBF9F9"
    ERROR = "#F81515"


class Spacing:
    XS = 4
    SM = 8
    MD = 16
    LG = 24
    XL = 32


class Sizes:
    RADIUS = 8
    FORM_WIDTH = 300
    MAX_WIDTH = 900


class Typography:
    TITLE = ft.TextStyle(size=22, weight=ft.FontWeight.BOLD)
    SUBTITLE = ft.TextStyle(size=18, weight=ft.FontWeight.W_500)
    BODY = ft.TextStyle(size=14)

    # Alineaciones estándar
    ALIGN_LEFT = ft.TextAlign.LEFT
    ALIGN_CENTER = ft.TextAlign.CENTER
    ALIGN_RIGHT = ft.TextAlign.RIGHT


class Alignments:
    COLUMN_MAIN = ft.MainAxisAlignment.START
    COLUMN_CROSS = ft.CrossAxisAlignment.CENTER


