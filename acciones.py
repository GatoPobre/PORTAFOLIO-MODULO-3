from data import productos_disponibles, carrito
from ui import mostrar_producto
import unicodedata

def normalizar(texto):
    # 1. Convierte a minúsculas (para que 'A' sea igual a 'a')
    texto = texto.lower()
    
    # 2. Descompone los caracteres (Separa la 'á' en 'a' + '´')
    # NFD = Normalization Form Decomposition
    texto_descompuesto = unicodedata.normalize('NFD', texto)
    
    # 3. Filtra y elimina los "caracteres de marca" (los acentos)
    # 'Mn' significa Mark, Nonspacing (Tildes, diéresis, etc.)
    texto_limpio = "".join(c for c in texto_descompuesto if unicodedata.category(c) != 'Mn')
    
    return texto_limpio


def buscar():
    opcion = input("Desea buscar por Nombre (1) o por Categoría (2): ").strip()
    encontrado = False
    if opcion == "1":
        buscando = input("Ingrese el nombre: ")
        print("=============  RESULTADO DE LA BUSQUEDA: ====================")
        print("ID |         NOMBRE            |    CATEGORIA    | PRECIO")
        print("=========================================================")
        for product_id, producto in productos_disponibles.items():
            if normalizar(buscando.lower()) in normalizar(producto["nombre"]):
                mostrar_producto(product_id, producto)
                encontrado = True
        if not encontrado:
            print("No hay productos con ese nombre.")

    elif opcion == "2":
        buscando = input("Ingrese la categoría: ")
        print("=============  RESULTADO DE LA BUSQUEDA: ==================")
        print("ID |         NOMBRE            |    CATEGORIA    | PRECIO")
        print("=========================================================")
        for product_id, producto in productos_disponibles.items():
            if normalizar(buscando) in normalizar(producto["categoria"]):
                mostrar_producto(product_id, producto)
                encontrado = True
        if not encontrado:
            print("No hay productos en esa categoría.")

    else:
        print("Opción incorrecta.")


def agregar():
    product_id = int(input("Ingresa el ID del producto seleccionado: "))

    if product_id not in productos_disponibles:
        print("ID de producto inválido.")
        return

    cantidad = int(input("Ingrese cantidad del producto: "))

    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0.")
        return

    producto = productos_disponibles[product_id]
    carrito.append((product_id, producto["nombre"], producto["categoria"], producto["precio"], cantidad))
    print("Producto agregado al carrito.")
    
