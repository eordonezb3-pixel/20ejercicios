"""Clase AnalizadorString que: 
(1) tenga método solo_vocales(letra) que retorne True si es vocal; 
(2) tenga método contar_por_tipo(texto) que retorne un diccionario 
{'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos; 
(3) tenga atributo que guarde el texto más largo analizado."""

class AnalizadorString:

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in 'aeiou'

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        conteo = {'vocales': 0, 'consonantes': 0, 'digitos': 0}
        for char in texto:
            if char.isdigit():
                conteo['digitos'] += 1
            elif char.isalpha():
                if self.solo_vocales(char):
                    conteo['vocales'] += 1
                else:
                    conteo['consonantes'] += 1
        return conteo

astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))
print(astr.contar_por_tipo("Python es genial!"))
print(f"Texto más largo: {astr.texto_mas_largo}")
