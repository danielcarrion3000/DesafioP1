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
        self.titulo = nuevo_titulo
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
        self.tareas = [tarea for tarea in self.tareas if tarea.titulo != titulo_tarea] 
    #recorre toda la lista de tareas hasta llegar a la tarea que tenga el titulo igual al ingresado


    def obtener_tareas(self):
        return self.tareas
    
#Clase sistema de gestion de tareas
class SistemaGestionTareas:
    #inicializacion del sistema de gestion de un archivo
    def __init__(self, archivo_datos ="datos_usuario.json"):
        self.usuarios = {}
        self.archivos_datos = archivo_datos
        self.cargar_datos()

    def cargar_datos(self):
        #cargar datos de los usuarios en json
        try:
            with open(self.archivos_datos, "r") as archivo:
                datos = json.load(archivo)
                for nombre_usuario, info in datos.items():
                    #crea un objeto usuario para cada usuario en los datos
                    usuario = usuario(nombre_usuario, info["contrasena"])
                    for tarea_info in info["tareas"]:
                        #crea un objeto tareas para cada tarea del usuario
                        tarea = Tarea(tarea_info["titulo"], tarea_info["descripcion"], tarea_info["fecha_vencimiento"])
                        usuario.agregar_tarea(tarea)
                    self.usuarios[nombre_usuario] = usuario
        except FileNotFoundError:
            print("Archivo de datos no encontrado, se creara uno nuevo al guardar")
    
    def guardar_datos(self):
        #Guardar los datos de los usuarios en el archivo, este es un diccionario de datos
        datos = {}
        for nombre_usuario, usuario in self.usuarios.items():
            #organiza las tareas y la informacion del usuario en un diccionario
            datos[nombre_usuario] = {
                "contrasena" : usuario.contrasena,
                "tareas" :[
                    {"titulo": tarea.titulo, "descripcion" : tarea.descripcion, "fecha_vencimiento" : tarea.fecha_vencimiento, "completado": tarea.completada}
                    for tarea in usuario.tareas    
                ]
            }
        with open(self.archivos_datos, "W") as archivo:
            json.dump(datos, archivo)

    def registrar_usuario(self, nombre_usuario, contrasena):
        #registrar un nuevo usuario si el nombre de usuario no existe
        if nombre_usuario in self.usuarios:
            print("El nombre de usuario ya existe")
            return False
        else:
            self.usuarios[nombre_usuario] = Usuario(nombre_usuario, contrasena)
            self.guardar_datos()
            print("Usuario registrado con exito")
            return True
    
    def iniciar_sesion(self, nombre_usuario, contrasena):
        #inicia sesion su el usuario y la contrasena coinciden
        Usuario = self.usuarios.get(nombre_usuario)
        if Usuario and Usuario.contrasena == contrasena:
            print("Inicio de secion exitoso")
            return Usuario
        else:
            print("Nombre de usuario o contrasena incorrectos.")
            return None

    def menu_usuario(self, Usuario):
        while True:
            print("\n1. Crear tarea")
            print("2. Ver tareas")
            print("3. Editar tarea")
            print("4. Completar tarea")
            print("5. Eliminar tarea")
            print("6. Cerrar sesion")

            opcion = input("Selecciona una opcion: ")
            if opcion == "1":
                titulo = input("Titulo de tarea: ")
                descripcion = input("Ingresa la descripcion: ")
                fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
                tarea = Tarea(titulo, descripcion, fecha_vencimiento)
                Usuario.agregar_tarea(tarea)
                self.guardar_datos()
                print("Tarea creada con exito")
            elif opcion == "2":
                tareas = Usuario.obtener_tareas()
                if not tareas: 
                    print("No tienes tareas")
                for idx, tarea in enumerate(tarea, start=1):
                    estado = "Completado" if tarea.completado else "Pendiente"
                    print(f"{idx}. {tarea.titulo} - {estado} (Vence: {tarea.fecha_vencimiento})")
                
            elif opcion == "3":
                titulo_tarea = input("Titulo de la tarea a editar: ")
                tarea = next((t for t in Usuario.tareas if t.titulo == titulo_tarea), None)
                if tarea:
                    nuevo_titulo = input("Nuevo titulo: ")
                    nueva_descripcion = input("Nueva descripcion: ")
                    nueva_fecha = input("Nueva fecha de vencimiento (YYYY-MM-DD): ")
                    tarea.editar_tarea(nuevo_titulo, nueva_descripcion, nueva_fecha)
                    self.guardar_datos()
                    print("Tarea actualizada con exito")
                else:
                    print("Tarea no encontrada")

            elif opcion == "4":
                #Marcar una tarea como completada
                titulo_tarea = input("Titulo de la tarea a completar: ")
                tarea = next((t for t in Usuario.tareas if t.titulo == titulo_tarea), None)
                if tarea:
                    tarea.marcar_competada()
                    self.guardar_datos()
                    print("Tarea marcada como completadad.")
                else:
                    print("Tarea no encontrada.")
            
            elif opcion == "5":
                #Eliminar una tarea
                titulo_tarea = input("Titulo de la tarea a eliminar: ")
                Usuario.eliminar_tarea(titulo_tarea)
                self.guardar_datos()
                print("Tarea eliminada con exito.")
            
            elif opcion == "6":
                #Cerrar sesion
                print("Cerrando sesion...")
                break
            else:
                print("Opcion no valida. Intentalo de nuevo.")


#Ejecusion del sistema

if __name__ == "__main__":
    sistema = SistemaGestionTareas()
    while True:
        print("\n----- Sitema de Gestion de tareas-----")
        print("1. Registrar usuario")
        print("2. Iniciar sesion")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")  

        if opcion == "1":
            nombre_usuario = input("Ingrese nombre de usuario:")
            contrasena = input("Ingrese la contrasena: ")
            sistema.registrar_usuario(nombre_usuario, contrasena)
        
        elif opcion == "2":
            nombre_usuario = input("Nombre de usuario: ")
            contrasena = input("Contrasena: ")
            Usuario = sistema.iniciar_sesion(nombre_usuario, contrasena)
            if Usuario:
                sistema.menu_usuario(Usuario)

        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida, Intentalo denuevo.")



        







