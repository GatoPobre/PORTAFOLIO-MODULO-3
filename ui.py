def mostrar_producto(product_id, producto):
    print(
        f"{product_id:2} | "
        f"{producto['nombre']:25} | "
        f"{producto['categoria']:15} |"
        f" ${producto['precio']:,}".replace(",", ".")
    )
