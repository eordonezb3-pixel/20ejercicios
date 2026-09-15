"""Clase Inventario que:
(1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario; 
(2) tenga método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente; 
(3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo."""

class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo ):
        return [producto for producto, cantidad in self.stock.items() if cantidad < minimo]

inv = Inventario()
inv.agregar_stock("pan", 50)
inv.restar_stock("pan", 30)
inv.productos_bajo_stock(15)
print(f"Stock actual: {inv.stock}")
print(f"Productos bajo stock de 15: {inv.productos_bajo_stock(15)}")
print(f"Intento de restar más stock del disponible: {inv.restar_stock('pan', 30)}")
print(f"Stock después de intentar restar más: {inv.stock}")
print(f"Intento de restar stock suficiente: {inv.restar_stock('pan', 10)}")