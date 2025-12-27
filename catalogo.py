from data import productos_disponibles
from ui import mostrar_producto


def ver_productos():
    print("=============  LISTADO DE PRODUCTOS  ====================")
    print("ID |         NOMBRE            |    CATEGORIA    | PRECIO")
    print("=========================================================")
    for product_id, producto in productos_disponibles.items():
        mostrar_producto(product_id, producto)
