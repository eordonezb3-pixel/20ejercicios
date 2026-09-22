"""Clase Departamentos que: (1) tenga método crear_departamento(nombre_departamento)
que inicie un departamento como una lista vacía en un diccionario;
(2) tenga método agregar_empleado(departamento, empleado) que añada el empleado
al departamento; (3) tenga método departamento_mayor_integrantes() que retorne
el nombre del departamento con más empleados."""

class Departamentos:

    def __init__(self):
        self.departamentos = {}

    def crear_departamento(self, nombre_departamento):
        self.departamentos[nombre_departamento] = []

    def agregar_empleado(self, departamento, empleado):
        if departamento in self.departamentos:
            self.departamentos[departamento].append(empleado)

    def departamento_mayor_integrantes(self):
        if not self.departamentos:
            return None

        return max(self.departamentos, key=lambda depto: len(self.departamentos[depto]))

d = Departamentos()
d.crear_departamento("Ventas")
d.crear_departamento("Soporte")
d.agregar_empleado("Ventas", "Sofía")
d.agregar_empleado("Ventas", "Diego")
d.agregar_empleado("Soporte", "Elena")
d.agregar_empleado("Soporte", "Marco")
d.agregar_empleado("Soporte", "Iván")

print(d.departamentos)
print(f"Departamento con más integrantes: {d.departamento_mayor_integrantes()}")
