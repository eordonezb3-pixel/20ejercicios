"""Clase AgrupadorEdades que: 
(1) tenga método clasificar_edad(edad) que retorne la categoría ("niño", "adolescente", "adulto", "mayor"); 
(2) tenga método agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]}; 
(3) tenga método edad_promedio_categoria(categoria)."""

class AgrupadorEdades:

    def clasificar_edad(self, edad):
        if edad < 13:
            return "niño"
        elif 13 <= edad < 20:
            return "adolescente"
        elif 20 <= edad < 60:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        categorias = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            if categoria not in categorias:
                categorias[categoria] = []
            categorias[categoria].append(edad)
        return categorias

    def edad_promedio_categoria(self, categoria, edades):
        edades_categoria = [edad for edad in edades if self.clasificar_edad(edad) == categoria]
        if edades_categoria:
            return sum(edades_categoria) / len(edades_categoria)
        return None

ae = AgrupadorEdades()
print(f"Clasificación de edad 15: {ae.clasificar_edad(15)}")
ae.agrupar_por_categoria(5, 15, 30, 70)
print(f"Agrupación por categoría: {ae.agrupar_por_categoria(5, 15, 30, 70)}")
print(f"Edad promedio de adultos: {ae.edad_promedio_categoria('adulto', [5, 15, 30, 70])}") 
