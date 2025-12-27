from catalogo import ver_productos
from acciones import buscar, agregar
from carrito import ver_carrito_total, vaciar_carrito


def main():
    while True:
        print(
            "\nBienvenido/a a tu Ecommerce\n"
            "1) Ver catálogo de productos\n"
            "2) Buscar producto por nombre o categoría\n"
            "3) Agregar producto al carrito\n"
            "4) Ver carrito y total\n"
            "5) Vaciar carrito\n"
            "0) Salir"
        )

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ver_productos()
        elif opcion == "2":
            buscar()
        elif opcion == "3":
            ver_productos()
            agregar()
        elif opcion == "4":
            ver_carrito_total()
        elif opcion == "5":
            vaciar_carrito()
        elif opcion == "0":
            print("\nGracias por visitar nuestro Ecommerce. ¡Hasta luego!")
            break
        else:
            print("Opción incorrecta.")


if __name__ == "__main__":
    main()
