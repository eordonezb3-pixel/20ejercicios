"""Clase GestorMascotas que:
(1) tenga método agregar_mascota(nombre, edad) que guarde en un diccionario;
(2) tenga método mascotas_mayores(edad_minima) que retorne una lista de nombres
cuya edad sea ≥;
(3) tenga método edad_promedio() que retorne el promedio de edades."""

class GestorMascotas:

    def __init__(self):
        self.mascotas = {}

    def agregar_mascota(self, nombre, edad):
        self.mascotas[nombre] = edad

    def mascotas_mayores(self, edad_minima=3):
        mayores = []
        for nombre, edad in self.mascotas.items():
            if edad >= edad_minima:
                mayores.append((nombre, edad))
        return mayores

    def edad_promedio(self):
        if len(self.mascotas) == 0:
            return 0

        return sum(self.mascotas.values()) / len(self.mascotas)


gm = GestorMascotas()
gm.agregar_mascota("Rocky", 5)
gm.agregar_mascota("Luna", 1)
gm.agregar_mascota("Toby", 3)
gm.agregar_mascota("Nina", 2)
gm.agregar_mascota("Max", 6)
gm.agregar_mascota("Coco", 1)


print(gm.mascotas)
print(f"Edad promedio: {gm.edad_promedio()}")
print(f"Mascotas mayores de 3 años: {gm.mascotas_mayores(3)}")
