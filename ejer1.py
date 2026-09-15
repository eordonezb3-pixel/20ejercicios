"""Clase Calificador que: 
(1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100, False en caso contrario; 
(2) tenga método cargar_notas(*args) que reciba múltiples notas, las valide, agregue 
solo las válidas a una lista interna, y retorne esa lista; 
(3) tenga método promedio() que retorne el promedio de notas almacenadas."""

class Calificador:


    def validar_nota(self, nota):
        if 0 <= nota <= 100:
            return True
        else:
            return False

    def cargar_notas(self, *args):
        notas = []

        for nota in args:
            if self.validar_nota(nota):
                notas.append(nota)
            else:
                print(f"Nota inválida: {nota}. Debe estar entre 0 y 100.")

        return notas

    def promedio(self, notas):
        if len(notas) == 0:
            return 0

        return sum(notas) / len(notas)


c = Calificador()

notas = c.cargar_notas(85, 92, 110, 78, -5, 88)

print("Notas válidas:", notas)
print("Promedio:", c.promedio(notas))