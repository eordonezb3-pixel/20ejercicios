"""Clase AnalizadorPaquetes que:
(1) tenga método encontrar_factores(numero) que retorne una tupla con todos los divisores;
(2) tenga método es_perfecto(numero) que retorne True si la suma de sus divisores (excepto él mismo) es igual a él;
(3) tenga método encontrar_multiples_factores(*numeros) que retorne un diccionario {número: tupla_factores}."""

class AnalizadorPaquetes:

    def encontrar_factores(self, numero):
        factores = [i for i in range(1, numero + 1) if numero % i == 0]
        return tuple(factores)

    def es_perfecto(self, numero):
        factores = self.encontrar_factores(numero)
        suma_factores = sum(factores) - numero
        return suma_factores == numero

    def encontrar_multiples_factores(self, *numeros):
        return {numero: self.encontrar_factores(numero) for numero in numeros}

bf = AnalizadorPaquetes()
bf.encontrar_factores(28)
bf.es_perfecto(28)
bf.encontrar_multiples_factores(6, 28, 496)
print(f"Factores de 28: {bf.encontrar_factores(28)}")
print(f"¿Es 28 un número perfecto? {bf.es_perfecto(28)}")
print(f"Factores de múltiples números: {bf.encontrar_multiples_factores(6, 28, 496)}")
