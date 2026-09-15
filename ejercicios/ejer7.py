"""Clase GestorPersonas que: 
(1) tenga método agregar_persona(nombre, edad) que guarde en un diccionario; 
 (2) tenga método personas_mayores(edad_minima) que retorne una lista de nombres 
 cuya edad sea ≥;
  (3) tenga método edad_promedio() que retorne el promedio de edades."""

class GestorPersonas:

    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima = 18):
        mayores = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                mayores.append((nombre, edad))
        return mayores
    
    def edad_promedio(self):
        if len(self.personas) == 0:
            return 0

        return sum(self.personas.values())/ len(self.personas)





gp = GestorPersonas()
gp.agregar_persona("Ana",28)
gp.agregar_persona("Bob",17)
gp.agregar_persona("Anai", 20)
gp.agregar_persona("Luis", 17)
gp.agregar_persona("Maria", 25)
gp.agregar_persona("Carlos", 15)


print(gp.personas)
print(f"Edad promedio: {gp.edad_promedio()}")
print(f"Personas mayores de 18: {gp.personas_mayores(18)}")
