"""Clase ControlTemperatura que:
Tenga un método validar_temperatura(temperatura) que retorne True si la temperatura está entre -20 y 50 grados, y False en caso contrario.
Tenga un método cargar_temperaturas(*args) que reciba múltiples temperaturas, valide cada una, agregue únicamente las válidas a una lista interna y retorne esa lista.
Tenga un método promedio() que retorne el promedio de las temperaturas almacenadas.
Crear un objeto de la clase, ingresar varias temperaturas, mostrar las temperaturas válidas y calcular su promedio."""

class ControlTemperatura:

    def validar_temperatura(self, temperatura):
        if -20 <= temperatura <= 50:
            return True
        else:
            return False

    def cargar_temperaturas(self, *args):
        temperaturas = []

        for temperatura in args:
            if self.validar_temperatura(temperatura):
                temperaturas.append(temperatura)
            else:
                print(f"Temperatura inválida: {temperatura}. Debe estar entre -20 y 50.")

        return temperaturas

    def promedio(self, temperaturas):
        if len(temperaturas) == 0:
            return 0

        return sum(temperaturas) / len(temperaturas)


c = ControlTemperatura()

temperaturas = c.cargar_temperaturas(22, 18, 55, 25, -30, 20)

print("Temperaturas válidas:", temperaturas)
print("Promedio:", c.promedio(temperaturas))