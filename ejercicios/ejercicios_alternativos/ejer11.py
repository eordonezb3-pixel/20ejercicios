"""Clase AnalizadorLecturas que:
(1) tenga método agregar_visita(pagina) que guarde en un diccionario contando repeticiones;
(2) tenga método pagina_mas_visitada() que retorne la página con mayor frecuencia;
(3) tenga método visitas_pagina(pagina) que retorne cuántas veces aparece."""

class AnalizadorLecturas:

    def __init__(self):
        self.visitas = {}

    def agregar_visita(self, pagina):
        if pagina in self.visitas:
            self.visitas[pagina] += 1
        else:
            self.visitas[pagina] = 1

    def pagina_mas_visitada(self):
        if not self.visitas:
            return None
        return max(self.visitas, key=self.visitas.get)

    def visitas_pagina(self, pagina):
        return self.visitas.get(pagina, 0)

cv = AnalizadorLecturas()
cv.agregar_visita("inicio")
cv.agregar_visita("contacto")
cv.agregar_visita("inicio")
cv.pagina_mas_visitada()
print(f"Página más visitada: {cv.pagina_mas_visitada()}")
print(f"Visitas a 'inicio': {cv.visitas_pagina('inicio')}")
