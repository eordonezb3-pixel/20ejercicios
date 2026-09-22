"""Clase AnalizadorRecetas que:
(1) tenga método encontrar_palabras(texto, patron) que busque palabras que inicien con el patrón y retorne una lista;
(2) tenga método agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]};
(3) tenga método palabras_unicas() usando un conjunto."""

class AnalizadorRecetas:
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

bp = AnalizadorRecetas()
bp.agrupar_por_longitud("la luna brilla mucho")
print(f"Agrupadas por longitud: {bp.agrupar_por_longitud('la luna brilla mucho')}")
print(f"Palabras que inician con 'l': {bp.encontrar_palabras('la luna brilla mucho', 'l')}")
print(f"Palabras únicas encontradas: {bp.palabras_unicas()}")
print(f"Palabras que inician con 'm': {bp.encontrar_palabras('la luna brilla mucho', 'm')}")
print(f"Palabras únicas encontradas después de buscar con 'm': {bp.palabras_unicas()}")
