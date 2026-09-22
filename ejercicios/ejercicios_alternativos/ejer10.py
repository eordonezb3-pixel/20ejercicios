"""Clase SolicitudesSoporte que: (1) tenga método agregar_reclamo(descripcion,
prioridad) que guarde en una lista de tuplas (descripción, prioridad);
(2) tenga método reclamos_prioritarios() que retorne solo los de prioridad
alta; (3) tenga método eliminar_resuelto(descripcion) que borre el reclamo de la lista."""

class SolicitudesSoporte:

    def __init__(self):
        self.reclamos = []

    def agregar_reclamo(self, descripcion, prioridad):
        self.reclamos.append((descripcion, prioridad))

    def reclamos_prioritarios(self):
        return [reclamo for reclamo in self.reclamos if reclamo[1] == 'alta']

    def eliminar_resuelto(self, descripcion):
        self.reclamos = [reclamo for reclamo in self.reclamos if reclamo[0] != descripcion]

r = SolicitudesSoporte()
r.agregar_reclamo("Falla de internet", "alta")
r.agregar_reclamo("Factura duplicada", "baja")
r.agregar_reclamo("Corte de servicio", "alta")
print(f"Reclamos prioritarios: {r.reclamos_prioritarios()}")
print(f"Reclamos: {r.reclamos}")
