"""Clase InversorListas que:
(1) tenga método invertir_lista(lista) que retorne la lista invertida sin usar reversed() (usa manual con bucles);
(2) tenga método invertir_multiples(*listas) que reutilice el anterior para invertir
varias listas y retorne una lista de pares (lista_original, lista_invertida)."""

class InversorListas:

    def invertir_lista(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida

    def invertir_multiples(self, *listas):
        resultado = []

        for lista in listas:
            invertida = self.invertir_lista(lista)
            resultado.append((tuple(lista), invertida))

        return resultado

o = InversorListas()

lista1 = [3, 7, 1, 9, 4, 2, 8, 6, 5]
lista2 = [10, 20, 30, 40, 50]
lista3 = [9, 5, 1]

print("Lista invertida:", o.invertir_lista([3, 7, 1, 9, 4, 2, 8, 6, 5]))

print("Varias listas:", o.invertir_multiples(lista1, lista2, lista3))
