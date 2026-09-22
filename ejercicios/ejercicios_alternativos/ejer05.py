"""Clase DetectorParidad que:
(1) tenga método es_par(numero) que retorne True/False;
(2) tenga método separar(*numeros) que retorne un diccionario
{'pares': [...], 'impares': [...]} reutilizando es_par;
(3) tenga método cantidad_pares_impares() que retorne una tupla
(cant_pares, cant_impares)."""

class DetectorParidad:

    def es_par(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def separar(self, *numeros):
        pares = []
        impares = []

        for numero in numeros:

            if self.es_par(numero):
                pares.append(numero)
            else:
                impares.append(numero)
        return {'pares': pares, 'impares': impares}

    def cantidad_pares_impares(self, *numeros):
        resultado = self.separar(*numeros)

        cant_pares = len(resultado['pares'])
        cant_impares = len(resultado['impares'])

        return (f"pares: {cant_pares}, impares: {cant_impares}")


d = DetectorParidad()

print(d.separar(2, 4, 6, 7, 9, 11, 13, 15, 8, 10, 21, 33))

print(d.cantidad_pares_impares(101, 202, 303, 4, 5, 6, 7, 8, 9, 10))
