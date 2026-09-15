"""Clase CombinadorListas que: 
(1) tenga método intercalar(lista1, lista2) que retorne una lista alternando elementos de ambas; 
(2) tenga método intercalar_multiples(*listas) que reutilice para varias listas."""

class CombinadorListas:

    def intercalar(self, lista1, lista2):
        resultado = []
        for a, b in zip(lista1, lista2):
            resultado.append(a)
            resultado.append(b)
        # Agregar elementos restantes si las listas son de diferente longitud
        resultado.extend(lista1[len(lista2):])
        resultado.extend(lista2[len(lista1):])
        return resultado

    def intercalar_multiples(self, *listas):
        if not listas:
            return []
        resultado = []
        max_len = max(len(lst) for lst in listas)
        for i in range(max_len):
            for lst in listas:
                if i < len(lst):
                    resultado.append(lst[i])
        return resultado

cl = CombinadorListas()
cl.intercalar([1,2], [3,4])
print(f"Intercalar dos listas: {cl.intercalar([1,2], [3,4])}")
cl.intercalar_multiples([1,2], [3,4], [5,6])
print(f"Intercalar múltiples listas: {cl.intercalar_multiples([1,2], [3,4], [5,6])}")
print(f"Intercalar listas de diferente longitud: {cl.intercalar([1,2,3], [4,5])}")
print(f"Intercalar listas vacías: {cl.intercalar([], [])}")