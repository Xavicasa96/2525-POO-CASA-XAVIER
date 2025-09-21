# Clase para representar un evento de la agenda
class Event:
    def __init__(self, fecha, hora, descripcion):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion

    def as_tuple(self):
        """Devuelve el evento en forma de tupla, útil para insertar en TreeView"""
        return (self.fecha, self.hora, self.descripcion)
