"""Clase AnalizadorPatrones que:
 (1) tenga método encontrar_palabras(texto, patron) que busque palabras que inicien con el patrón y retorne una lista; 
 (2) tenga método agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]}; 
 (3) tenga método palabras_unicas() usando un conjunto."""

class AnalizadorPatrones:
    def __init__(self):
        self.palabras = set()

    def encontrar_palabras(self, texto, patron):
        palabras_encontradas = [palabra for palabra in texto.split() if palabra.startswith(patron)]
        self.palabras.update(palabras_encontradas)
        return palabras_encontradas

    def agrupar_por_longitud(self, texto):
        agrupadas = {}
        for palabra in texto.split():
            longitud = len(palabra)
            if longitud not in agrupadas:
                agrupadas[longitud] = []
            agrupadas[longitud].append(palabra)
        return agrupadas

    def palabras_unicas(self):
        return list(self.palabras)

ap = AnalizadorPatrones()
ap.agrupar_por_longitud("el gato está aquí")
print(f"Agrupadas por longitud: {ap.agrupar_por_longitud('el gato está aquí')}")
print(f"Palabras que inician con 'g': {ap.encontrar_palabras('el gato está aquí', 'g')}")
print(f"Palabras únicas encontradas: {ap.palabras_unicas()}")
print(f"Palabras que inician con 'e': {ap.encontrar_palabras('el gato está aquí', 'e')}")
print(f"Palabras únicas encontradas después de buscar con 'e': {ap.palabras_unicas()}")