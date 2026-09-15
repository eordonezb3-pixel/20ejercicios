"""Clase CarroCompras que: 
(1) tenga método agregar_articulo(nombre, precio) que guarde en un diccionario {nombre: precio}; 
(2) tenga método total_carrito() que retorne la suma de todos los precios; 
(3) tenga método articulos_por_rango(precio_min, precio_max) que retorne una lista con artículos dentro del rango.
Ejemplo de entrada
c = CarroCompras()
c.agregar_articulo("pan",2.50)
c.agregar_articulo("leche",3.00)
c.total_carrito()"""

class CarroCompras:

    def __init__(self):
        self.lista = {}

    def agregar_articulo(self, nombre, precio):
        self.lista[nombre] = precio

    def total_carrito(self):
        return sum(self.lista.values())
    
    def articulos_por_rango(self, precio_min, precio_max):
        return [nombre for nombre, precio in self.lista.items() 
            if precio_min <= precio <= precio_max]

c = CarroCompras()
c.agregar_articulo("pan",2.50)
c.agregar_articulo("leche",5.00)

print(c.total_carrito())
print(c.articulos_por_rango(2.00, 5.75))
print(c.lista)