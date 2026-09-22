"""Clase Bodega que:
(1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario;
(2) tenga método retirar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente;
(3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo."""

class Bodega:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def retirar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        return [producto for producto, cantidad in self.stock.items() if cantidad < minimo]

b = Bodega()
b.agregar_stock("harina", 40)
b.retirar_stock("harina", 25)
b.productos_bajo_stock(20)
print(f"Stock actual: {b.stock}")
print(f"Productos bajo stock de 20: {b.productos_bajo_stock(20)}")
print(f"Intento de retirar más stock del disponible: {b.retirar_stock('harina', 25)}")
print(f"Stock después de intentar retirar más: {b.stock}")
print(f"Intento de retirar stock suficiente: {b.retirar_stock('harina', 5)}")
