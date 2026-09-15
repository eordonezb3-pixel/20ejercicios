"""Clase CodificadorCesar que: 
(1) tenga método codificar_letra(letra, desplazamiento) que retorne la letra desplazada en el alfabeto (usar operador %); 
(2) tenga método codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra; 
(3) tenga un diccionario como atributo para historial de codificaciones."""

class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            return chr((ord(letra) - base + desplazamiento) % 26 + base)
        return letra

    def codificar_palabra(self, palabra, desplazamiento):
        codificada = ''.join(self.codificar_letra(letra, desplazamiento) for letra in palabra)
        self.historial[palabra] = codificada
        return codificada   

cc = CodificadorCesar()
cc.codificar_palabra("hola", 3)
print(f"Palabra codificada: {cc.codificar_palabra('hola', 3)}")
print(f"Historial de codificaciones: {cc.historial}")
