"""Version unificada de los 20 ejercicios alternativos."""


# Ejercicio 1: temperaturas
class MonitorTemperaturas:
    def validar_temperatura(self, temperatura):
        return -20 <= temperatura <= 50

    def cargar_temperaturas(self, *args):
        temperaturas = []
        for temperatura in args:
            if self.validar_temperatura(temperatura):
                temperaturas.append(temperatura)
        return temperaturas

    def promedio(self, temperaturas):
        if not temperaturas:
            return 0
        return sum(temperaturas) / len(temperaturas)


# Ejercicio 2: productos
class GestorProductos:
    def __init__(self):
        self.productos = set()
        self.lista = []

    def agregar_producto(self, producto):
        self.productos.add(producto)
        self.lista.append(producto)

    def contar_productos(self):
        return len(self.productos)

    def agregar_multiples(self, *args):
        for producto in args:
            self.agregar_producto(producto)


# Ejercicio 3: peliculas
class CatalogoPeliculas:
    def __init__(self):
        self.peliculas = {}

    def agregar_pelicula(self, titulo, precio):
        self.peliculas[titulo] = precio

    def total_catalogo(self):
        return sum(self.peliculas.values())

    def peliculas_por_rango(self, precio_min, precio_max):
        return [titulo for titulo, precio in self.peliculas.items()
                if precio_min <= precio <= precio_max]


# Ejercicio 4: listas invertidas
class InversorListas:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = []
        for lista in listas:
            resultado.append((tuple(lista), self.invertir_lista(lista)))
        return resultado


# Ejercicio 5: paridad
class DetectorParidad:
    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        pares = []
        impares = []
        for numero in numeros:
            if self.es_par(numero):
                pares.append(numero)
            else:
                impares.append(numero)
        return {'pares': pares, 'impares': impares}

    def cantidad_pares_impares(self, *numeros):
        resultado = self.separar(*numeros)
        return (f"pares: {len(resultado['pares'])}, "
                f"impares: {len(resultado['impares'])}")


# Ejercicio 6: precios
class GestorPrecios:
    def __init__(self):
        self.precios = []

    def registrar_precio(self, precio):
        self.precios.append(precio)

    def minimo(self):
        return min(self.precios)

    def maximo(self):
        return max(self.precios)

    def promedio(self):
        return sum(self.precios) / len(self.precios)

    def registrar_multiples(self, *precios):
        for precio in precios:
            self.registrar_precio(precio)


# Ejercicio 7: mascotas
class GestorMascotas:
    def __init__(self):
        self.mascotas = {}

    def agregar_mascota(self, nombre, edad):
        self.mascotas[nombre] = edad

    def mascotas_mayores(self, edad_minima=3):
        return [(nombre, edad) for nombre, edad in self.mascotas.items()
                if edad >= edad_minima]

    def edad_promedio(self):
        if not self.mascotas:
            return 0
        return sum(self.mascotas.values()) / len(self.mascotas)


# Ejercicio 8: departamentos
class Departamentos:
    def __init__(self):
        self.departamentos = {}

    def crear_departamento(self, nombre_departamento):
        self.departamentos[nombre_departamento] = []

    def agregar_empleado(self, departamento, empleado):
        if departamento in self.departamentos:
            self.departamentos[departamento].append(empleado)

    def departamento_mayor_integrantes(self):
        if not self.departamentos:
            return None
        return max(self.departamentos,
                   key=lambda depto: len(self.departamentos[depto]))


# Ejercicio 9: analisis de claves
class AnalizadorClave:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in 'aeiou'

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
        conteo = {'vocales': 0, 'consonantes': 0, 'digitos': 0}
        for char in texto:
            if char.isdigit():
                conteo['digitos'] += 1
            elif char.isalpha():
                if self.solo_vocales(char):
                    conteo['vocales'] += 1
                else:
                    conteo['consonantes'] += 1
        return conteo


# Ejercicio 10: reclamos
class Reclamos:
    def __init__(self):
        self.reclamos = []

    def agregar_reclamo(self, descripcion, prioridad):
        self.reclamos.append((descripcion, prioridad))

    def reclamos_prioritarios(self):
        return [reclamo for reclamo in self.reclamos
                if reclamo[1] == 'alta']

    def eliminar_resuelto(self, descripcion):
        self.reclamos = [reclamo for reclamo in self.reclamos
                         if reclamo[0] != descripcion]


# Ejercicio 11: visitas
class ContadorVisitas:
    def __init__(self):
        self.visitas = {}

    def agregar_visita(self, pagina):
        self.visitas[pagina] = self.visitas.get(pagina, 0) + 1

    def pagina_mas_visitada(self):
        if not self.visitas:
            return None
        return max(self.visitas, key=self.visitas.get)

    def visitas_pagina(self, pagina):
        return self.visitas.get(pagina, 0)


# Ejercicio 12: secuencias
class GeneradorSecuencias:
    def crear_secuencia(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_secuencias(self, *secuencias):
        elementos = set()
        for secuencia in secuencias:
            elementos.update(self.crear_secuencia(*secuencia))
        return list(elementos)


# Ejercicio 13: listas intercaladas
class MezcladorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        for a, b in zip(lista1, lista2):
            resultado.extend([a, b])
        resultado.extend(lista1[len(lista2):])
        resultado.extend(lista2[len(lista1):])
        return resultado

    def intercalar_multiples(self, *listas):
        if not listas:
            return []
        resultado = []
        for i in range(max(len(lista) for lista in listas)):
            for lista in listas:
                if i < len(lista):
                    resultado.append(lista[i])
        return resultado


# Ejercicio 14: ventas
class RegistroVentas:
    def __init__(self):
        self.ventas = {}

    def registrar(self, vendedor, monto):
        self.ventas[vendedor] = monto

    def vendedores_destacados(self, monto_minimo):
        return [vendedor for vendedor, monto in self.ventas.items()
                if monto >= monto_minimo]

    def mejor_vendedor(self):
        if not self.ventas:
            return None
        vendedor = max(self.ventas, key=self.ventas.get)
        return vendedor, self.ventas[vendedor]


# Ejercicio 15: factores
class BuscadorFactores:
    def encontrar_factores(self, numero):
        return tuple(i for i in range(1, numero + 1) if numero % i == 0)

    def es_perfecto(self, numero):
        factores = self.encontrar_factores(numero)
        return sum(factores) - numero == numero

    def encontrar_multiples_factores(self, *numeros):
        return {numero: self.encontrar_factores(numero) for numero in numeros}


# Ejercicio 16: cifrado
class CifradorDesplazamiento:
    def __init__(self):
        self.historial = {}

    def cifrar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            return chr((ord(letra) - base + desplazamiento) % 26 + base)
        return letra

    def cifrar_palabra(self, palabra, desplazamiento):
        cifrada = ''.join(self.cifrar_letra(letra, desplazamiento)
                           for letra in palabra)
        self.historial[palabra] = cifrada
        return cifrada


# Ejercicio 17: temperaturas por categoria
class ClasificadorTemperaturas:
    def clasificar_temperatura(self, temp):
        if temp < 10:
            return "frio"
        if temp < 20:
            return "templado"
        if temp < 30:
            return "calido"
        return "muy caliente"

    def agrupar_por_categoria(self, *temperaturas):
        categorias = {}
        for temp in temperaturas:
            categoria = self.clasificar_temperatura(temp)
            categorias.setdefault(categoria, []).append(temp)
        return categorias

    def promedio_categoria(self, categoria, temperaturas):
        valores = [temp for temp in temperaturas
                   if self.clasificar_temperatura(temp) == categoria]
        if not valores:
            return None
        return sum(valores) / len(valores)


# Ejercicio 18: puntos
class LocalizadorPuntos:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        distancia = ((p1[0] - p2[0]) ** 2 +
                     (p1[1] - p2[1]) ** 2) ** 0.5
        self.distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        if not puntos:
            return None
        return min(puntos, key=lambda p: self.distancia_euclidiana(referencia, p))


# Ejercicio 19: bodega
class Bodega:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def retirar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        return [producto for producto, cantidad in self.stock.items()
                if cantidad < minimo]


# Ejercicio 20: palabras
class BuscadorPalabras:
    def __init__(self):
        self.palabras = set()

    def encontrar_palabras(self, texto, patron):
        encontradas = [palabra for palabra in texto.split()
                       if palabra.startswith(patron)]
        self.palabras.update(encontradas)
        return encontradas

    def agrupar_por_longitud(self, texto):
        agrupadas = {}
        for palabra in texto.split():
            agrupadas.setdefault(len(palabra), []).append(palabra)
        return agrupadas

    def palabras_unicas(self):
        return list(self.palabras)


def main():
    """Ejecuta una demostracion breve de los 20 ejercicios."""
    gestor_productos = GestorProductos()
    gestor_productos.agregar_multiples("Laptop", "Mouse", "Laptop")

    catalogo = CatalogoPeliculas()
    catalogo.agregar_pelicula("El viaje lunar", 12.50)
    catalogo.agregar_pelicula("Horizonte rojo", 18.00)

    gestor_precios = GestorPrecios()
    gestor_precios.registrar_multiples(15.50, 22.00, 8.75)

    mascotas = GestorMascotas()
    mascotas.agregar_mascota("Rocky", 5)
    mascotas.agregar_mascota("Luna", 1)

    departamentos = Departamentos()
    departamentos.crear_departamento("Ventas")
    departamentos.crear_departamento("Soporte")
    departamentos.agregar_empleado("Ventas", "Sofia")
    departamentos.agregar_empleado("Soporte", "Marco")
    departamentos.agregar_empleado("Soporte", "Elena")

    reclamos = Reclamos()
    reclamos.agregar_reclamo("Falla de internet", "alta")

    visitas = ContadorVisitas()
    visitas.agregar_visita("inicio")
    visitas.agregar_visita("inicio")

    ventas = RegistroVentas()
    ventas.registrar("Sara", 4200)

    bodega = Bodega()
    bodega.agregar_stock("harina", 40)
    bodega.retirar_stock("harina", 25)

    palabras = BuscadorPalabras()
    palabras.encontrar_palabras("la luna brilla", "l")

    ejercicios = [
        ("01", MonitorTemperaturas().cargar_temperaturas(22, 18, 55, 25)),
        ("02", gestor_productos.contar_productos()),
        ("03", catalogo.total_catalogo()),
        ("04", InversorListas().invertir_lista([1, 2, 3])),
        ("05", DetectorParidad().separar(2, 3, 4)),
        ("06", gestor_precios.promedio()),
        ("07", mascotas.mascotas_mayores(3)),
        ("08", departamentos.departamento_mayor_integrantes()),
        ("09", AnalizadorClave().contar_por_tipo("Clave99")),
        ("10", reclamos.reclamos_prioritarios()),
        ("11", visitas.pagina_mas_visitada()),
        ("12", GeneradorSecuencias().crear_secuencia(1, 4)),
        ("13", MezcladorListas().intercalar([1, 3], [2, 4])),
        ("14", ventas.mejor_vendedor()),
        ("15", BuscadorFactores().encontrar_factores(28)),
        ("16", CifradorDesplazamiento().cifrar_palabra("mundo", 5)),
        ("17", ClasificadorTemperaturas().clasificar_temperatura(18)),
        ("18", LocalizadorPuntos().punto_mas_cercano((0, 0), (2, 2), (1, 1))),
        ("19", bodega.productos_bajo_stock(20)),
        ("20", palabras.palabras_unicas()),
    ]
    for numero, resultado in ejercicios:
        print(f"Ejercicio {numero}: {resultado}")


if __name__ == "__main__":
    main()
