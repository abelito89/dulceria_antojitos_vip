"""
theme_helpers.py - Componentes factory para UI estandarizada

Adaptado para funcionar EXCLUSIVAMENTE con las definiciones del theme.py original.
No requiere ningún atributo adicional en theme.py.
"""

import flet as ft
from ui.theme import Colors, Spacing, Sizes, Typography

# ============================================================================
# VALORES LOCALES FALLBACK (para lo que no está en theme.py)
# ============================================================================
_BORDER_COLOR = "#3D1A1A"       # más oscuro que SURFACE para bordes
_TEXTSEC_COLOR = "#C0C0C0"      # gris claro para texto secundario
_SURFACE_VARIANT = "#1A0808"    # variante más oscura de SURFACE
_INFO_COLOR = "#2196F3"         # azul estándar
_WARNING_COLOR = "#FF9800"       # naranja
_RADIUS_SMALL = 4                # tamaño pequeño para badges
_ICON_SIZE = 20                  # tamaño por defecto para iconos

# Estilos de texto adicionales basados en los existentes
_H1_STYLE = ft.TextStyle(size=28, weight=ft.FontWeight.BOLD)
_H2_STYLE = ft.TextStyle(size=22, weight=ft.FontWeight.BOLD)
_H3_STYLE = ft.TextStyle(size=18, weight=ft.FontWeight.W_600)
_BODY_SMALL = ft.TextStyle(size=12, weight=ft.FontWeight.NORMAL)
_BODY_LARGE = ft.TextStyle(size=16, weight=ft.FontWeight.NORMAL)
_LABEL_STYLE = ft.TextStyle(size=12, weight=ft.FontWeight.W_500)
_HELPER_STYLE = ft.TextStyle(size=11, weight=ft.FontWeight.NORMAL)
_ERROR_STYLE = ft.TextStyle(size=11, weight=ft.FontWeight.NORMAL, color=Colors.ERROR)

# ============================================================================
# CONTENEDORES
# ============================================================================

def card(content, padding=None, width=None):
    """Tarjeta estándar con borde visible."""
    return ft.Container(
        content=content,
        padding=padding or Spacing.LG,
        bgcolor=Colors.SURFACE,
        border_radius=Sizes.RADIUS,
        border=ft.border.all(1, _BORDER_COLOR),
        width=width
    )

def section(content, title=None, padding=None):
    """Sección con título opcional."""
    items = []
    if title:
        items.append(heading2(title))
        items.append(ft.Container(height=Spacing.MD))
    items.append(content)
    return ft.Container(
        content=ft.Column(items, spacing=0),
        padding=padding or Spacing.XL,
    )

def form_group(controls, spacing=None):
    """Agrupa campos de formulario."""
    return ft.Column(controls, spacing=spacing or Spacing.MD)

# ============================================================================
# TEXTOS
# ============================================================================

def heading1(text, color=None):
    """Título H1 (más grande)."""
    return ft.Text(value=text, style=_H1_STYLE, color=color or Colors.TEXT)

def heading2(text, color=None):
    """Título H2."""
    return ft.Text(value=text, style=_H2_STYLE, color=color or Colors.TEXT)

def heading3(text, color=None):
    """Título H3."""
    return ft.Text(value=text, style=_H3_STYLE, color=color or Colors.TEXT)

def body_text(text, color=None, size=None):
    """Texto de cuerpo. size: 'small' o 'large'."""
    if size == "small":
        style = _BODY_SMALL
    elif size == "large":
        style = _BODY_LARGE
    else:
        style = Typography.BODY
    return ft.Text(value=text, style=style, color=color or Colors.TEXT)

def label_text(text):
    """Etiqueta de formulario."""
    return ft.Text(value=text, style=_LABEL_STYLE, color=_TEXTSEC_COLOR)

def helper_text(text, error=False):
    """Texto de ayuda o error (pequeño)."""
    if error:
        return ft.Text(value=text, style=_ERROR_STYLE)
    return ft.Text(value=text, style=_HELPER_STYLE, color=_TEXTSEC_COLOR)

def success_text(text):
    """Texto de éxito (verde). Usar para mensajes breves positivos."""
    return ft.Text(
        value=text,
        color=Colors.SUCCESS,
        size=14,
        weight=ft.FontWeight.W_500
    )

def error_text(text):
    """Texto de error (rojo). Usar para mensajes breves de error."""
    return ft.Text(
        value=text,
        color=Colors.ERROR,
        size=14,
        weight=ft.FontWeight.W_500
    )

# ============================================================================
# BOTONES
# ============================================================================

def _base_button(text, on_click, width, disabled, bgcolor):
    """Botón base para no repetir código."""
    return ft.FilledButton(
        content=ft.Text(text, color=Colors.TEXT, style=Typography.SUBTITLE),
        on_click=on_click,
        width=width,
        disabled=disabled,
        style=ft.ButtonStyle(
            bgcolor=bgcolor,
            shape=ft.RoundedRectangleBorder(radius=Sizes.RADIUS),
        ),
        height=44
    )

def confirm_button(text, on_click=None, width=None, disabled=False):
    """Confirmación final - Azul."""
    return _base_button(text, on_click, width, disabled, Colors.CONFIRM)

def primary_button(text, on_click=None, width=None, disabled=False):
    """Acción destructiva - Rojo."""
    return _base_button(text, on_click, width, disabled, Colors.PRIMARY)

def draft_button(text, on_click=None, width=None, disabled=False):
    """Guardado parcial / borrador - Morado."""
    return _base_button(text, on_click, width, disabled, Colors.SECONDARY)

def warning_button(text, on_click=None, width=None, disabled=False):
    """Advertencia - Naranja."""
    return _base_button(text, on_click, width, disabled, Colors.WARNING)

def secondary_button(text, on_click=None, width=None, disabled=False):
    """Acción neutral - borde sin relleno."""
    return ft.OutlinedButton(
        content=ft.Text(text, color=Colors.TEXT, style=Typography.SUBTITLE),
        on_click=on_click,
        width=width,
        disabled=disabled,
        height=44,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=Sizes.RADIUS),
            side=ft.BorderSide(1, Colors.TEXT)
        )
    )

def text_button(text, on_click=None, color=None):
    """Enlace o acción muy secundaria - solo texto."""
    return ft.TextButton(
        content=ft.Text(
            text,
            color=color or _TEXTSEC_COLOR,
            size=14,
            weight=ft.FontWeight.W_500
        ),
        on_click=on_click,
        style=ft.ButtonStyle(overlay_color=ft.Colors.TRANSPARENT)
    )

def icon_button(icon, on_click=None, size=None, tooltip=None, color=None):
    """Botón solo icono."""
    return ft.IconButton(
        icon=icon,
        on_click=on_click,
        icon_size=size or _ICON_SIZE,
        tooltip=tooltip,
        icon_color=color or Colors.PRIMARY
    )

# ============================================================================
# CAMPOS DE ENTRADA
# ============================================================================

def text_field(label, on_change=None, width=None, multiline=False,
               suffix_icon=None, error_text=None):
    """TextField consistente."""
    field = ft.TextField(
        label=label,
        on_change=on_change,
        bgcolor=_SURFACE_VARIANT,
        border=ft.InputBorder.OUTLINE,
        border_radius=Sizes.RADIUS,
        width=width or Sizes.FORM_WIDTH,
        multiline=multiline,
        label_style=ft.TextStyle(size=12, color=_TEXTSEC_COLOR),
        suffix=suffix_icon
    )
    if error_text:
        return ft.Column([field, helper_text(error_text, error=True)])
    return field

def dropdown_field(label, options, on_change=None, width=None):
    """Dropdown consistente."""
    return ft.Dropdown(
        label=label,
        options=options,
        on_change=on_change,
        width=width or Sizes.FORM_WIDTH,
        bgcolor=_SURFACE_VARIANT,
        border_radius=Sizes.RADIUS,
        label_style=ft.TextStyle(size=12, color=_TEXTSEC_COLOR)
    )

# ============================================================================
# FEEDBACK VISUAL
# ============================================================================

def info_box(content, type="info"):
    """Caja de información (info, success, error, warning)."""
    colors_map = {
        "info": (_INFO_COLOR, "#E3F2FD"),
        "success": (Colors.SUCCESS, "#E8F5E9"),
        "error": (Colors.ERROR, "#FFEBEE"),
        "warning": (_WARNING_COLOR, "#FFF3E0"),
    }
    color, bg = colors_map.get(type, colors_map["info"])
    if isinstance(content, ft.Control):
        text_content = content
    else:
        text_content = ft.Text(value=str(content), color=color)
    return ft.Container(
        content=text_content,
        padding=Spacing.MD,
        bgcolor=bg,
        border=ft.border.all(1, color),
        border_radius=Sizes.RADIUS
    )

def badge(text, color=None, bgcolor=None):
    """Pequeña etiqueta."""
    color = color or Colors.PRIMARY
    bgcolor = bgcolor or "#FFE4E1"
    return ft.Container(
        content=ft.Text(value=text, size=11, weight=ft.FontWeight.W_600, color=color),
        padding=ft.padding.symmetric(4, 8),
        bgcolor=bgcolor,
        border_radius=_RADIUS_SMALL
    )

# ============================================================================
# UTILIDADES Y SEPARADORES
# ============================================================================

def spacer(height=None):
    """Separador vertical."""
    return ft.Container(height=height or Spacing.MD)

def divider(vertical=False):
    """Línea divisoria."""
    if vertical:
        return ft.VerticalDivider(width=1, color=_BORDER_COLOR)
    return ft.Divider(height=1, color=_BORDER_COLOR)

def loading_indicator(message="Cargando..."):
    """Indicador de carga."""
    return ft.Column(
        [
            ft.ProgressRing(width=40, height=40, color=Colors.PRIMARY),
            ft.Container(height=Spacing.MD),
            body_text(message, color=_TEXTSEC_COLOR)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=Spacing.MD
    )

def empty_state(icon, title, description=""):
    """Estado vacío (sin datos)."""
    items = [
        ft.Icon(icon, size=64, color=_TEXTSEC_COLOR),
        ft.Container(height=Spacing.MD),
        heading2(title, color=_TEXTSEC_COLOR),
    ]
    if description:
        items.extend([
            ft.Container(height=Spacing.SM),
            body_text(description, color=_TEXTSEC_COLOR)
        ])
    return ft.Column(
        items,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0
    )