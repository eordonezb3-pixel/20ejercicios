"""Clase ClasificadorTemperaturas que:
(1) tenga método clasificar_temperatura(temp) que retorne la categoría ("frío", "templado", "cálido", "muy caliente");
(2) tenga método agrupar_por_categoria(*temperaturas) que retorne un diccionario con {categoría: [temperaturas]};
(3) tenga método promedio_categoria(categoria, temperaturas)."""

class ClasificadorTemperaturas:

    def clasificar_temperatura(self, temp):
        if temp < 10:
            return "frío"
        elif 10 <= temp < 20:
            return "templado"
        elif 20 <= temp < 30:
            return "cálido"
        else:
            return "muy caliente"

    def agrupar_por_categoria(self, *temperaturas):
        categorias = {}
        for temp in temperaturas:
            categoria = self.clasificar_temperatura(temp)
            if categoria not in categorias:
                categorias[categoria] = []
            categorias[categoria].append(temp)
        return categorias

    def promedio_categoria(self, categoria, temperaturas):
        temps_categoria = [temp for temp in temperaturas if self.clasificar_temperatura(temp) == categoria]
        if temps_categoria:
            return sum(temps_categoria) / len(temps_categoria)
        return None

ct = ClasificadorTemperaturas()
print(f"Clasificación de 18 grados: {ct.clasificar_temperatura(18)}")
ct.agrupar_por_categoria(5, 18, 25, 35)
print(f"Agrupación por categoría: {ct.agrupar_por_categoria(5, 18, 25, 35)}")
print(f"Promedio de días cálidos: {ct.promedio_categoria('cálido', [5, 18, 25, 35])}")
