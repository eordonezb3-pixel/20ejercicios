"""Clase GestorPrecios que:
(1) tenga método registrar_precio(precio) que guarde en una lista;
(2) tenga método minimo(), maximo(), promedio() que calculen estadísticas;
(3) tenga método registrar_multiples(*precios) que reutilice el registro para varios precios."""

class GestorPrecios:

    def __init__(self):
        self.precios = []

    def registrar_precio(self, precio):
        self.precios.append(precio)

    def minimo(self):
        return min(self.precios)

    def maximo(self):
        return max(self.precios)

    def promedio(self):
        return sum(self.precios) / len(self.precios)

    def registrar_multiples(self, *precios):
        for precio in precios:
            self.registrar_precio(precio)

gp = GestorPrecios()
gp.registrar_multiples(15.50, 22.00, 8.75, 30.10)
print(gp.precios)
print(gp.promedio())
print(gp.minimo())
print(gp.maximo())
