"""Clase CifradorDesplazamiento que:
(1) tenga método cifrar_letra(letra, desplazamiento) que retorne la letra desplazada en el alfabeto (usar operador %);
(2) tenga método cifrar_palabra(palabra, desplazamiento) que reutilice para toda la palabra;
(3) tenga un diccionario como atributo para historial de cifrados."""

class CifradorDesplazamiento:
    def __init__(self):
        self.historial = {}

    def cifrar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            return chr((ord(letra) - base + desplazamiento) % 26 + base)
        return letra

    def cifrar_palabra(self, palabra, desplazamiento):
        cifrada = ''.join(self.cifrar_letra(letra, desplazamiento) for letra in palabra)
        self.historial[palabra] = cifrada
        return cifrada

cd = CifradorDesplazamiento()
cd.cifrar_palabra("mundo", 5)
print(f"Palabra cifrada: {cd.cifrar_palabra('mundo', 5)}")
print(f"Historial de cifrados: {cd.historial}")
