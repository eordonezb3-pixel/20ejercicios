"""Clase CatalogoLibros que:
(1) tenga método agregar_libro(titulo, precio) que guarde en un diccionario {titulo: precio};
(2) tenga método total_catalogo() que retorne la suma de todos los precios;
(3) tenga método libros_por_rango(precio_min, precio_max) que retorne una lista con títulos dentro del rango.
Ejemplo de entrada
c = CatalogoLibros()
c.agregar_libro("Cien años de soledad", 12.50)
c.agregar_libro("Rayuela", 15.00)
c.total_catalogo()"""

class CatalogoLibros:

    def __init__(self):
        self.libros = {}

    def agregar_libro(self, titulo, precio):
        self.libros[titulo] = precio

    def total_catalogo(self):
        return sum(self.libros.values())

    def libros_por_rango(self, precio_min, precio_max):
        return [titulo for titulo, precio in self.libros.items()
            if precio_min <= precio <= precio_max]

c = CatalogoLibros()
c.agregar_libro("Cien años de soledad", 12.50)
c.agregar_libro("Rayuela", 18.00)

print(c.total_catalogo())
print(c.libros_por_rango(10.00, 20.00))
print(c.libros)
