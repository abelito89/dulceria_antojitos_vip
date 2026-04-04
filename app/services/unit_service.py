# app/services/unit_service.py

def consumo_a_base(cantidad_consumo: float, factor_conversion: float) -> float:
    """
    Convierte cantidad desde unidad_consumo a unidad_base
    """
    return cantidad_consumo / factor_conversion