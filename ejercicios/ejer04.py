"""Clase InversorSecuencia que: 
(1) tenga método invertir_lista(lista) que retorne la lista invertida sin usar reversed() (usa manual con bucles); 
(2) tenga método invertir_multiples(*listas) que reutilice el anterior para invertir 
varias listas y retorne un diccionario {lista_original: lista_invertida}."""

class InversorSecuencia:


    def invertir_lista(self,lista):
        invertida = []
        
        for i in range(len(lista) -1,-1,-1):
            invertida.append(lista[i])

        return invertida
    
    def invertir_listas(self, *listas):
        result = []

        for lista in listas:
            invertida = self.invertir_lista(lista)
            result.append((tuple(lista), invertida))

        return  result

c = InversorSecuencia()

lista1 = [1,2,4,5,6,8,9,13,55]
lista2 = [11,22,33,454,12,5]
lista3 = [2, 1, 0]

print("Lista invertida:", c.invertir_lista([1,2,4,5,6,8,9,13,55]))

print("Varias listas:", c.invertir_listas(lista1, lista2, lista3))


    