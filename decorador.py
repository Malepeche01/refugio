import time

t = time.localtime(time.time())
localtime = time.asctime(t)
hora = time.asctime(t)

def decorador_alta(valor=True):
    def alta(funcion):
        def envoltura(*args, **kwargs):
            valor = args[0]
            if valor:
                archivo = open('logdeco.txt', "a")
                archivo.write('Alta OK ' + hora + ' ' + args[0] + '\n')
                archivo.close()
                print("Alta completada: " + hora)
            else:
                print("No se pudo completar el alta: " + hora)

            funcion(*args, **kwargs)
        return envoltura
    return alta

@decorador_alta(True)
def alta_perrito(self):
    pass
# ##########################################################################################

def decorador_borrar(valor=True):
    def borrar(funcion):
        def envoltura(*args, **kwargs):
            valor = args[0]
            if valor:
                archivo = open('logdeco.txt', "a")
                archivo.write('Baja OK ' + hora + ' ' + args[0] + '\n')
                archivo.close()
                print("Baja completada: " + hora)
            else:
                print("No se pudo completar la baja: " + hora)

            funcion(*args, **kwargs)
        return envoltura
    return borrar

@decorador_borrar(True)
def baja_perrito(self):
    pass