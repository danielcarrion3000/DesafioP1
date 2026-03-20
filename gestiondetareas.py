import json
from datetime import datetime

#class Tarea

class Tarea:
    def __init__(self, titulo, descripcion, fecha_vencimiento):
        self.titulo = self.titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completado = False  # hasta que no le demos una indicacion  de que esta completado, debe mantenerse en falso

    def marcar_completada(self):
        self.completado = True

    def editar_tarea(self, nuevo_titulo, nueva_descripcion, nueva_fecha):
        self.titulo =nuevo_titulo
        self.descripcion = nueva_descripcion
        self.fecha_vencimiento = nueva_fecha

#clase usuario
class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, titulo_tarea):
        self.tareas = [tarea for tarea in self.tareas if tarea.titulo !=titulo_tarea] 
    #recorre toda la lista de tareas hasta llegar a la tarea que tenga el titulo igual al ingresado


    def obtener_tareas(self):
        return self.tareas
    