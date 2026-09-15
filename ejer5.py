"""Clase AnalizadorNumeros que: 
(1) tenga método es_par(numero) que retorne True/False; 
(2) tenga método separar(*numeros) que retorne un diccionario 
{'pares': [...], 'impares': [...]} reutilizando es_par; 
(3) tenga método cantidad_pares_impares() que retorne una tupla 
(cant_pares, cant_impares)."""

class AnalizadorNumeros:

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
        
        paress = len(resultado['pares'])
        imparess = len(resultado['impares'])
        
        return (f"pares: {paress}, impares: {imparess}")


c = AnalizadorNumeros()

print(c.separar(1, 2, 3, 4, 5,111,12,3, 6, 7, 8, 9, 10))

print(c.cantidad_pares_impares(109,111,123, 2, 3, 4, 5, 6, 7, 8, 9, 10))
