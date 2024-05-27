import re
import datetime
from modelo import Modelito
from peewee import *
from log_error import RegistroLogError
from observador import Sujeto
from decorador import alta_perrito, baja_perrito


# Crea la base / la conecta

db = SqliteDatabase("mascotas_bd.db")

class BaseModel(Model):
    class Meta:
        database = db
 
# Crea la tabla mascotas 

class Mascota(BaseModel):
    nombre= CharField()
    fecha_i= DateField()
    fecha_e= DateField()
    fecha_n= DateField()
    tamaño= CharField()
    peso= FloatField()

db.connect()
db.create_tables([Mascota])

class Abmc(Sujeto):
    def __init__(self,):
        self.objeto_modelo=Modelito()
    

    # Método para dar de alta un registro con validación y excepción

    def alta(self,nombre, ingreso, egreso, nacimiento, tamaño, peso, tree, entry_nombre):
        cadena = nombre.get()
        patron = "^[A-Za-záéíóú]*$"  # Regex para el campo nombre solo texto
        if (re.match(patron, cadena)):
            mascota = Mascota()
            mascota.nombre=nombre.get()
            mascota.fecha_i=ingreso.get()
            mascota.fecha_e=egreso.get()
            mascota.fecha_n=nacimiento.get()
            mascota.tamaño=tamaño.get()
            mascota.peso=peso.get()
            mascota.save()
            self.actualizar_treeview(tree)
            self.objeto_modelo.limpiar_entry(nombre,ingreso,egreso,nacimiento,tamaño,peso)
            entry_nombre.focus_set()
            alta_perrito(mascota.nombre)
            #self.notificar(mascota.nombre, mascota.fecha_i, mascota.fecha_e)
            return True
        else:
            #Se genera la Excepción para el caso que ingrese un caracter que no sea texto
            raise RegistroLogError(cadena, datetime.datetime.now())
       
    # Método para borrar un registro en BD y treeview

    def borrar(self, tree, combo):
        valor = tree.selection()
        item = tree.item(valor)
        nombre = item['values'][0]
        borrar=Mascota.get(Mascota.id==item["text"])
        borrar.delete_instance()
        baja_perrito(nombre)
        self.actualizar_treeview(tree)  # muestro treeview actualizada
        self.mostrar_perritos(combo)  # actualizo el deplegable
        

    # Método para modificar un registro seleccionado desde el treeview una vez actualizado los datos

    def modificar(self, nombre, ingreso, egreso, nacimiento, tamaño, peso, tree, combo, entry_nombre):
        valor = tree.selection()
        item = tree.item(valor)
        actualizar=Mascota.update(nombre=nombre.get(), fecha_i=ingreso.get(), fecha_e = egreso.get(), fecha_n = nacimiento.get(), tamaño = tamaño.get(), peso = peso.get()).where(Mascota.id==item["text"])
        actualizar.execute()
        self.actualizar_treeview(tree)  # actualizo en treeview
        self.mostrar_perritos(combo)
        self.notificar(nombre.get(), ingreso.get(), egreso.get())
        self.objeto_modelo.limpiar_entry(nombre, ingreso, egreso, nacimiento, tamaño, peso)  # limpio campos de entrada
        entry_nombre.focus_set()
        
    # Método para mostrar la treeview actualizada luego de cualquier cambio o al abrir la app en reiterados usos
    
    def actualizar_treeview(self, mitreview):
        records = mitreview.get_children()  # borro todo
        for element in records:
            mitreview.delete(element)
        # recorro BD y muestro en treeview
        for fila in Mascota.select():
            mitreview.insert("", 0, text=fila.id, values=(fila.nombre, fila.fecha_i, fila.fecha_e, fila.fecha_n, fila.tamaño, fila.peso))
               

    # Método para actualizar la lista a desplegar segun modificaciones

    def mostrar_perritos(self,combo):
        lista = []
        for row in Mascota.select():
            lista.insert(row.id, (row.id, row.nombre))
        combo["values"] = lista
        return lista
        

    # Método para conformar el desplegable

    def combobox(self, index, nombre, ingreso, egreso, nacimiento, tamaño, peso, combo):
        lista = self.mostrar_perritos(combo)
        tupla = lista[index]
        comboid = tupla[0]
        mi_id = int(comboid)
        for fila in Mascota.select().where(Mascota.id==mi_id): 
            nombre.set(fila.nombre),
            ingreso.set(fila.fecha_i),
            egreso.set(fila.fecha_e),
            nacimiento.set(fila.fecha_n),
            tamaño.set(fila.tamaño),
            peso.set(fila.peso)