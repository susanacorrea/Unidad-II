def costo_de_venta(compras_netas: float, inventario_inicial: float) -> float:
    """Calcula el costo de venta, solicita compras_netas y el inventario_inicial"""
    return compras_netas + inventario_inicial


def costo_de_venta2(total_mercancias: float, inventario_final: float) -> float:
    """Calcula el costo de ventas, solicita el total_mercancias y el inventario_final"""
    return total_mercancias - inventario_final


def compras_netas(compras_totales: float, devoluciones: float, descuentos: float) -> float:
    """Calcula las compras netas, solicita las compras totales, las devoluciones y el descuento"""
    return compras_totales-((devoluciones/compras_totales)+(descuentos/compras_totales))

