"""Clase `GestorProductos` que:

1. Tenga un método `agregar_producto(producto)` que agregue el producto a un **conjunto** para evitar duplicados y también a una **lista** para conservar el orden de ingreso.
2. Tenga un método `contar_productos()` que retorne la cantidad de **productos únicos** registrados.
3. Tenga un método `agregar_multiples(*args)` que reutilice el método `agregar_producto()` para agregar varios productos.
4. Crear un objeto de la clase, agregar algunos productos individualmente y otros mediante `agregar_multiples()`.
5. Mostrar en pantalla el **conjunto**, la **lista** y la cantidad de productos únicos."""
class GestorProductos:

    def __init__(self):
        self.productos = set()
        self.lista = []

    def agregar_producto(self, producto):
        self.productos.add(producto)
        self.lista.append(producto)

    def contar_productos(self):
        return len(self.productos)

    def agregar_multiples(self, *args):
        for producto in args:
            self.agregar_producto(producto)


p = GestorProductos()

p.agregar_producto("Laptop")
p.agregar_producto("Mouse")
p.agregar_producto("Laptop")

p.agregar_multiples("Teclado", "Monitor", "Mouse")

print("Conjunto:", p.productos)
print("Lista:", p.lista)
print("Productos unicos:", p.contar_productos())