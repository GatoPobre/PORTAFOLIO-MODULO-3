# 🛒 E-commerce de Consola en Python

¡Bienvenido a tu nuevo sistema de gestión de compras favorito! 🚀
Este proyecto es una aplicación de comercio electrónico basada en terminal, diseñada para ser rápida, eficiente y fácil de usar.

---

## 📄 Descripción

Este programa simula una experiencia de compra completa desde la línea de comandos. Permite a los usuarios explorar un catálogo de productos, buscar artículos específicos, gestionar un carrito de compras y ver el total a pagar. Es ideal para aprender sobre lógica de programación, manejo de estructuras de datos y modularización en Python.

---

## 🛠️ Tecnologías Aplicadas

El proyecto está construido íntegramente con **Python 3**, utilizando programación estructurada y modular.

*   **🐍 Python**: Lenguaje principal.
*   **🗂️ Estructuras de Datos**: Uso de diccionarios (`dict`) y listas (`list`) para gestionar productos y el carrito.
*   **🔡 Unicodedata**: Para normalización de texto y búsquedas inteligentes (insensibles a acentos).
*   **🖥️ Interfaz CLI**: Interfaz de Línea de Comandos limpia y legible.

---

## 📂 Estructura del Programa

El código está organizado en módulos para facilitar su mantenimiento y escalabilidad:

*   **`main.py`**: 🏁 **Punto de entrada**. Contiene el bucle principal y el menú de navegación.
*   **`data.py`**: 💾 **Base de datos**. Almacena el inventario de `productos_disponibles` y el estado actual del `carrito`.
*   **`acciones.py`**: ⚡ **Lógica de negocio**. Maneja la búsqueda de productos y la adición de artículos al carrito.
*   **`catalogo.py`**: 📖 **Visualización**. Se encarga de mostrar el listado completo de productos formateado.
*   **`carrito.py`**: 🛒 **Gestión del carrito**. Muestra el resumen de compras, calcula totales y permite vaciar el carrito.
*   **`ui.py`**: 🎨 **Interfaz**. Funciones auxiliares para mostrar información de productos de forma consistente.

---

## ✨ Características Destacadas

*   **🔍 Búsqueda Inteligente**: Encuentra productos por *nombre* o *categoría*. ¡No importa si olvidas las tildes o usas mayúsculas/minúsculas!
*   **💰 Cálculo Automático**: El carrito calcula subtotales y totales automáticamente, formateando los precios para una fácil lectura.
*   **🛡️ Validaciones**: Evita errores al ingresar IDs inexistentes o cantidades inválidas.

---

## 🚀 ¿Cómo ejecutarlo?

Sigue estos sencillos pasos para iniciar la aplicación:

1.  **Asegúrate de tener Python instalado**:
    ```bash
    python --version
    ```

2.  **Ejecuta el archivo principal**:
    Navega a la carpeta del proyecto y corre el siguiente comando:
    ```bash
    python main.py
    ```

3.  **¡Disfruta comprando!** 🎉
    Sigue las instrucciones en pantalla para navegar por el menú.

---
*Desarrollado con ❤️ por GatoPobre.*
