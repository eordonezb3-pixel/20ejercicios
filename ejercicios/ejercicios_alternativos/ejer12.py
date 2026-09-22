"""Clase GeneradorTurnos que:
(1) tenga método crear_secuencia(inicio, fin) que retorne una tupla con números en ese rango;
(2) tenga método elementos_en_multiples_secuencias(*secuencias) que reciba múltiples tuplas (inicio,fin)
y retorne una lista combinada sin duplicados usando un conjunto."""

class GeneradorTurnos:

    def crear_secuencia(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_secuencias(self, *secuencias):
        elementos = set()
        for secuencia in secuencias:
            elementos.update(self.crear_secuencia(*secuencia))
        return list(elementos)

gs = GeneradorTurnos()
gs.elementos_en_multiples_secuencias((1, 4), (3, 6))
print(f"Elementos en múltiples secuencias: {gs.elementos_en_multiples_secuencias((1, 4), (3, 6))}")
print(f"Secuencia de 7 a 12: {gs.crear_secuencia(7, 12)}")
