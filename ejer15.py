"""Clase DivisorFinder que: 
(1) tenga método encontrar_divisores(numero) que retorne una tupla con todos los divisores; 
(2) tenga método es_perfecto(numero) que retorne True si la suma de sus divisores (excepto él mismo) es igual a él; 
(3) tenga método encontrar_multiples_divisores(*numeros) que retorne un diccionario {número: tupla_divisores}."""

class DivisorFinder:

    def encontrar_divisores(self, numero):
        divisores = [i for i in range(1, numero + 1) if numero % i == 0]
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma_divisores = sum(divisores) - numero
        return suma_divisores == numero

    def encontrar_multiples_divisores(self, *numeros):
        return {numero: self.encontrar_divisores(numero) for numero in numeros}

df = DivisorFinder()
df.encontrar_divisores(12)
df.es_perfecto(6)
df.encontrar_multiples_divisores(6, 12, 28)
print(f"Divisores de 12: {df.encontrar_divisores(12)}")
print(f"¿Es 6 un número perfecto? {df.es_perfecto(6)}")
print(f"Divisores de múltiples números: {df.encontrar_multiples_divisores(6, 12, 28)}")
