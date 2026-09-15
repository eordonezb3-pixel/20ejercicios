"""Clase AnalizadorTexto que: 
(1) tenga método agregar_palabra(palabra) que agregue la palabra a un conjunto (para evitar duplicados) 
y a una lista (para el orden);
 (2) tenga método contar_palabras() que retorne cuántas palabras únicas hay; 
 (3) tenga método agregar_multiples(*args) que reutilice agregar_palabra para varios."""

class AnalizadorTexto:

    def __init__(self):
        self.palabras = set()
        self.lista = []

    def agregar_palabra(self, palabra):
        self.palabras.add(palabra)
        self.lista.append(palabra)

    def contar_palabras(self):
        return len(self.palabras)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


c = AnalizadorTexto()

c.agregar_palabra("casa")
c.agregar_palabra("perro")
c.agregar_palabra("casa")

c.agregar_multiples("gato", "sol", "perro")

print("Conjunto:", c.palabras)
print("Lista:", c.lista)
print("Palabras unicas:", c.contar_palabras())