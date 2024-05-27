import os

class RegistroLogError(Exception):
    
    # Define archivo y ubicación para registro de errores

    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = os.path.join(BASE_DIR, "logerror.txt")

    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha
    
    # Abre el archivo en modo "append" y agrega el último error detectado

    def registrar_error(self):
        log = open(self.ruta,"a") 
        print("Se ha dado un error con el nombre:", self.nombre, self.fecha, file = log)




