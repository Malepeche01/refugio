from tkinter import ttk
from tkinter import W,E
from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox
from modelo import Modelito
from bd import Abmc
from log_error import RegistroLogError
from PIL import ImageTk, Image
import os

# ##############################################
# VISTA
# ##############################################

class Ventanita():
    def __init__(self,windows):
        
        self.objeto_base=Abmc()
        self.objeto_modelo=Modelito()
        self.master = windows
        self.master.title("Refugio CuchaCucha")
        self.master.geometry("700x950") # Tamaño de la ventana TKINTER
        self.s = ttk.Style()
        self.s.theme_use('clam')

        self.titulo = Label(self.master, text="Ingrese los datos de la mascota",
                    bg="Green", fg="thistle1", height=1, width=70)
        self.titulo.grid(row=0, column=0, columnspan=6, padx=1, pady=1, sticky=W+E)

        # Desplegable

        self.nombre = Label(self.master, text="Consulta")
        self.nombre.grid(row=8, column=9, sticky=W)
        self.combo = ttk.Combobox(state="readonly")
        self.combo = ttk.Combobox(self.master, width=14)
        
        # Actualizo lista de tuplas para las mascotas a mostrar

        opciones = self.objeto_base.mostrar_perritos(self.combo)
        self.combo["values"] = opciones
        self.combo.grid(row=8, column=10)

        # Imagen de la APP

        self.image = Image.open("perritoAlta.jpg")
        self.img = ImageTk.PhotoImage(self.image)
        self.background_label = Label(self.master, image=self.img)
        self.background_label.place()
        self.lbl_img = Label(self.master, image=self.img)
        self.lbl_img.place(x=80, y=340)

        # Foto mascota

        BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
        ruta = os.path.join(BASE_DIR, "chloe_ch.png")
        self.image2 = Image.open(ruta)
        self.image1 = ImageTk.PhotoImage(self.image2)
        self.background_label = Label(self.master, image=self.image1)
        self.background_label.place(x=510)

        # Declaracion de variables TKINTER

        self.var_nombre = StringVar()
        self.var_fecha_i = StringVar()
        self.var_fecha_e = StringVar()
        self.var_fecha_n = StringVar()
        self.var_tamaño = StringVar()
        self.var_peso = StringVar()

        self.nombre = Label(self.master, text="Nombre")
        self.nombre.grid(row=1, column=0, sticky=W)
        self.fecha_i = Label(self.master, text="Fecha de Ingreso")
        self.fecha_i.grid(row=2, column=0, sticky=W)
        self.fecha_e = Label(self.master, text="Fecha de Egreso")
        self.fecha_e.grid(row=3, column=0, sticky=W)
        self.fecha_n = Label(self.master, text="Fecha de Nacimiento estimado")
        self.fecha_n.grid(row=4, column=0, sticky=W)
        self.tamaño = Label(self.master, text="Tamaño")
        self.tamaño.grid(row=5, column=0, sticky=W)
        self.peso = Label(self.master, text="Peso")
        self.peso.grid(row=6, column=0, sticky=W)


        self.entry_nombre = Entry(self.master, textvariable=self.var_nombre, width=25)
        self.entry_nombre.grid(row=1, column=1)
        self.entry_fecha_i = Entry(self.master, textvariable=self.var_fecha_i, width=25)
        self.entry_fecha_i.grid(row=2, column=1)
        self.entry_fecha_e = Entry(self.master, textvariable=self.var_fecha_e, width=25)
        self.entry_fecha_e.grid(row=3, column=1)
        self.entry_fecha_n = Entry(self.master, textvariable=self.var_fecha_n, width=25)
        self.entry_fecha_n.grid(row=4, column=1)
        self.entry_tamaño = Entry(self.master, textvariable=self.var_tamaño, width=25)
        self.entry_tamaño.grid(row=5, column=1)
        self.entry_peso = Entry(self.master, textvariable=self.var_peso, width=25)
        self.entry_peso.grid(row=6, column=1)
        self.tree = ttk.Treeview(self.master)

        self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6")
        self.tree.column("#0", width=50, minwidth=50, anchor=W)
        self.tree.column("col1", width=80, minwidth=80, anchor=W)
        self.tree.column("col2", width=80, minwidth=80, anchor=W)
        self.tree.column("col3", width=80, minwidth=80, anchor=W)
        self.tree.column("col4", width=80, minwidth=80, anchor=W)
        self.tree.column("col5", width=80, minwidth=80, anchor=W)
        self.tree.column("col6", width=50, minwidth=50, anchor=W)

        # Configuro el stilo del encabezado del Treeview
        self.s.configure('Treeview.Heading', background="green", foreground='white')

        self.tree.heading("col1", text="Nombre")
        self.tree.heading("#0", text="id")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Ingreso")
        self.tree.heading("col3", text="Egreso")
        self.tree.heading("col4", text="Nacimiento")
        self.tree.heading("col5", text="Tamaño")
        self.tree.heading("col6", text="Peso")

        self.tree.grid(column=0, row=8, columnspan=6)

        self.objeto_base.actualizar_treeview(self.tree)

        
        self.boton_ingresar = Button(self.master, text="Ingresar Registro",
                            command=lambda: self.alta_vista(self.var_nombre, self.var_fecha_i,
                                                self.var_fecha_e, self.var_fecha_n, self.var_tamaño,
                                                self.var_peso, self.tree, self.entry_nombre), background="green", foreground='white')
    
             
        self.boton_ingresar.place(x=380, y=60)

        self.boton_eliminar = Button(self.master, text="Eliminar",
                                command=lambda: self.borrar_vista(self.tree,self.combo), background="coral", foreground='white')
        
        self.boton_eliminar.grid(row=9, column=3)

        self.boton_cancelar = Button(self.master, text="Cancelar",
                                command=lambda: self.objeto_modelo.limpiar_entry(self.var_nombre, self.var_fecha_i,
                                                    self.var_fecha_e, self.var_fecha_n, self.var_tamaño,
                                                    self.var_peso), background="green", foreground='white')
        self.boton_cancelar.place(x=400, y=90)

        self.boton_modificar = Button(self.master, text="Modificar",
                                command=lambda: self.d_vista(self.var_nombre, self.var_fecha_i,
                                                    self.var_fecha_e, self.var_fecha_n, self.var_tamaño,
                                                    self.var_peso, self.tree), background="peachpuff3")
        self.boton_modificar.grid(row=11, column=3)

        self.boton_combobox = Button(self.master, text="OK",
                                command=lambda: self.objeto_base.combobox(self.combo.current(),self.var_nombre, self.var_fecha_i,
                                                    self.var_fecha_e, self.var_fecha_n, self.var_tamaño,
                                                    self.var_peso, self.combo), background="peachpuff3")
        self.boton_combobox.place(x=580, y=280)

        self.boton_actualizar = Button(self.master, text="Actualizar",
                                command=lambda: self.objeto_base.modificar(self.var_nombre, self.var_fecha_i,
                                                    self.var_fecha_e, self.var_fecha_n, self.var_tamaño,
                                                    self.var_peso, self.tree, self.combo, self.entry_nombre), background="peachpuff4")
        self.boton_actualizar.grid(row=12, column=3)

    def alta_vista(self, nombre,ingreso,egreso,nacimiento,tamaño,peso,tree,entry_nombre):
        try: #Intenta dar de alta el nuevo registro
            self.objeto_base.alta(nombre,ingreso,egreso,nacimiento,tamaño,peso,tree,entry_nombre)
            messagebox.showinfo(title="Estoy en Alta", message="Perrito ingresado")
            self.objeto_base.mostrar_perritos(self.combo)
        except RegistroLogError as log: #Excepción en caso de error en el tipo de dato ingresado para "nombre"
            messagebox.showerror(title="Error en Alta", message="Hay un error en el campo Nombre. Ingrese solo letras")
            log.registrar_error()
 
    def d_vista(self,nombre,ingreso,egreso,nacimiento,tamaño,peso,tree):
        self.objeto_modelo.funcion_d(nombre,ingreso,egreso,nacimiento,tamaño,peso,tree)
        messagebox.showwarning(title="Modificación",  # si quiere modificar los campos debe ingresar datos y dar Actualizar
                            message="Ingrese los nuevos datos y clickee Actualizar")
        

    def borrar_vista(self,tree,combo):
        answer = messagebox.askyesno(  # confirma eliminación del registro seleccionado
        message="¿Desea eliminar el registro?", title="Confirmar")
        if answer:
            self.objeto_base.borrar(tree,combo)

    