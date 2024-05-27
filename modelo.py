class Modelito():
    def __init__(self): pass
       
    # Función para vaciar los campos de entrada una vez dada un A/B/M

    def limpiar_entry(self,nombre,ingreso,egreso,nacimiento,tamaño,peso):
        nombre.set(''),
        ingreso.set(''),
        egreso.set(''),
        nacimiento.set(''),
        tamaño.set(''),
        peso.set(''),
        

    # Función para traer los campos y hacerlos visibles de una selección dada del treeview

    def funcion_d(self,nombre,ingreso,egreso,nacimiento,tamaño,peso,tree):
        item = tree.focus()
        datos = tree.item(item).get("values")
        nombre.set(datos[0]),
        ingreso.set(datos[1]),
        egreso.set(datos[2]),
        nacimiento.set(datos[3]),
        tamaño.set(datos[4]),
        peso.set(datos[5]),
        return True        