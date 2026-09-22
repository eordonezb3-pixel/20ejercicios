"""Clase CatalogoPeliculas que:
(1) tenga método agregar_pelicula(titulo, precio) que guarde en un diccionario {titulo: precio};
(2) tenga método total_catalogo() que retorne la suma de todos los precios;
(3) tenga método peliculas_por_rango(precio_min, precio_max) que retorne una lista con títulos dentro del rango.
Ejemplo de entrada
c = CatalogoPeliculas()
c.agregar_pelicula("El viaje lunar", 12.50)
c.agregar_pelicula("Horizonte rojo", 15.00)
c.total_catalogo()"""

class CatalogoPeliculas:

    def __init__(self):
        self.peliculas = {}

    def agregar_pelicula(self, titulo, precio):
        self.peliculas[titulo] = precio

    def total_catalogo(self):
        return sum(self.peliculas.values())

    def peliculas_por_rango(self, precio_min, precio_max):
        return [titulo for titulo, precio in self.peliculas.items()
            if precio_min <= precio <= precio_max]

c = CatalogoPeliculas()
c.agregar_pelicula("El viaje lunar", 12.50)
c.agregar_pelicula("Horizonte rojo", 18.00)

print(c.total_catalogo())
print(c.peliculas_por_rango(10.00, 20.00))
print(c.peliculas)
