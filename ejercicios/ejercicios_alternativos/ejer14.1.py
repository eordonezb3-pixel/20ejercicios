"""Clase RegistroVentas que:
(1) tenga método registrar(vendedor, monto) que guarde en un diccionario;
(2) tenga método vendedores_destacados(monto_minimo) que retorne lista de vendedores;
(3) tenga método mejor_vendedor() que retorne nombre y monto del que tiene mayor venta."""

class RegistroVentas:

    def __init__(self):
        self.ventas = {}

    def registrar(self, vendedor, monto):
        self.ventas[vendedor] = monto

    def vendedores_destacados(self, monto_minimo):
        return [vendedor for vendedor, monto in self.ventas.items() if monto >= monto_minimo]

    def mejor_vendedor(self):
        if not self.ventas:
            return None
        mejor_vendedor = max(self.ventas, key=self.ventas.get)
        return mejor_vendedor, self.ventas[mejor_vendedor]

rv = RegistroVentas()
rv.registrar("Sara", 4200)
rv.registrar("Tomás", 1800)
rv.mejor_vendedor()
print(f"Mejor vendedor: {rv.mejor_vendedor()}")
print(f"Vendedores destacados (monto mínimo 2000): {rv.vendedores_destacados(2000)}")
