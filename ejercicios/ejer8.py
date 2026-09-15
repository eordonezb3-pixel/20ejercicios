"""Clase Equipos que: (1) tenga método crear_equipo(nombre_equipo) 
que inicie un equipo como una lista vacía en un diccionario; 
(2) tenga método agregar_jugador(equipo, jugador) que añada el jugador 
al equipo; (3) tenga método equipo_mayor_integrantes() que retorne 
el nombre del equipo con más jugadores."""

class Equipos:

    def __init__(self):
        self.equipos = {}

    def crear_equipos(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if not self.equipos:
            return None

        return max(self.equipos, key=lambda equipo: len(self.equipos[equipo]))

eq = Equipos()
eq.crear_equipos("A")
eq.crear_equipos("B")
eq.agregar_jugador("A","Juan")
eq.agregar_jugador("A","Pedro")
eq.agregar_jugador("B","Luis")
eq.agregar_jugador("B","Ana")
eq.agregar_jugador("B","Maria")

print(eq.equipos)
print(f"Equipo con más integrantes: {eq.equipo_mayor_integrantes()}")