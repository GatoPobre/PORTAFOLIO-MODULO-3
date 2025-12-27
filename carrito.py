from data import carrito

def ver_carrito_total():
    if not carrito:
        print("Carrito vacío.")
        return
    print("========================  CARRITO DE COMPRAS  ================================================")
    print("ID |         NOMBRE            |    CATEGORIA    | CANTIDAD |    PRECIO   |   SUBTOTAL")
    print("==============================================================================================")
    total = 0
    for id,nombre,categoria, precio, cantidad in carrito:
        subtotal = precio * cantidad
        total += subtotal
        subtotal = f"{subtotal:10,}".replace(",", ".")
        precio = f"{precio:10,}".replace(",", ".")
        print(
            f"{id:2} | "
            f"{nombre:25} | "
            f"{categoria:15} |"
            f" {cantidad:8} |"
            f" ${precio} |"
            f" ${subtotal}"
            )
    print("_"*93)
    print(f"{'':64}TOTAL A PAGAR: ${total:,}".replace(",", "."))


def vaciar_carrito():
    carrito.clear()
    print("Carrito vaciado.")
