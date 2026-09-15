"""Clase RegistroNotas que: 
(1) tenga método registrar(estudiante, nota) que guarde en un diccionario; 
(2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de estudiantes; 
(3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene mayor calificación."""

class RegistroNotas:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        return [estudiante for estudiante, nota in self.notas.items() if nota >= nota_minima]

    def mejor_estudiante(self):
        if not self.notas:
            return None
        mejor_estudiante = max(self.notas, key=self.notas.get)
        return mejor_estudiante, self.notas[mejor_estudiante]

rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.mejor_estudiante()
print(f"Mejor estudiante: {rn.mejor_estudiante()}")
print(f"Estudiantes aprobados (nota mínima 80): {rn.estudiantes_aprobados(80)}")
