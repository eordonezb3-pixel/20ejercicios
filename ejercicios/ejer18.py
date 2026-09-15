"""Clase CalculadorDistancia que: 
(1) tenga método distancia_euclidiana(p1, p2) que reciba dos tuplas (x,y) y calcule la distancia; 
(2) tenga método punto_mas_cercano(referencia, *puntos) que retorne el punto más cercano a referencia; 
(3) tenga un atributo lista para guardar todas las distancias calculadas."""

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        distancia = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
        self.distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        if not puntos:
            return None
        punto_cercano = min(puntos, key=lambda p: self.distancia_euclidiana(referencia, p))
        return punto_cercano

cd = CalculadorDistancia()
print(f"Distancia entre (1,2) y (4,6): {cd.distancia_euclidiana((1, 2), (4, 6))}")
print(f"Punto más cercano a (0,0) entre (1,1), (2,2), (3,3): {cd.punto_mas_cercano((0, 0), (1, 1), (2, 2), (3, 3))}")
print(f"Lista de distancias calculadas: {cd.distancias}")