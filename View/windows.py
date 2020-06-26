
from tkinter import *
import tkinter as tk
from Control.Controller import Controller
import tkinter.messagebox

class Windows:     

# Constructor de la ventana   
    def __init__(self):
        self.ventana()                
        
# Metodo que crea una ventana e inserta un panel de trabajo
    def ventana(self):
        self.view = Tk()
        self.control = Controller()
        self.diseño()
        self.labelAndInput()
        self.view.mainloop()
        
#Metodo de diseño de la ventana 
    def diseño(self):
        self.view.title("AUTOMATAS Y LENGUAJES FORMALES")
        self.view.geometry('1000x600+180+60')
        self.panel = Frame(self.view,width=1000, height=600).pack()
         
# Inserta al panel un label y una variable que resive un string
    def labelAndInput(self):               
        self.variable_1 = StringVar()
        label_1 = Label(self.panel,text="Alfabeto: ").place(x=421, y=44)
        input_1 = Entry(self.panel,textvariable = self.variable_1, width=25).place(x=475, y=44)
        
        self.variable_2 = StringVar()
        label_2 = Label(self.panel,text="Estados: ").place(x=425, y=75)
        input_2 = Entry(self.panel,textvariable = self.variable_2, width=25).place(x=475, y=75)
        
        self.variable_3 = StringVar()
        label_3 = Label(self.panel,text="Expresión Regular: ").place(x=370, y=106)
        input_3 = Entry(self.panel,textvariable = self.variable_3, width=25).place(x=475, y=106)
        
        # Boton de accion        
        boton1 = Button(self.panel,
                             text="ACEPTAR",
                             width=8,height=2,
                             background="SkyBlue2",
                             command= self.accion
                             ).place(x=480,y=150)
    
    # Evento de boton de accion
    def accion(self):
        # llamado de funcion para separar el lenguje
        variableSeparada = self.control.separadoLenguaje(self.variable_1.get())        
        # Retorno validacion correccion sintaxis
        validador = self.control.validacionLexico(variableSeparada,self.variable_3.get())
        self.accionValidacion(validador)
        
    # Funcion para realizar acciones despues de la validacion
    def accionValidacion(self, bandera):
        if bandera:
            print('no hay errores')
        else:
            tkinter.messagebox.showerror("ERROR NOT FOUND",
                                         "LA EXPRECIÓN NO CONCUERDA CON EL LENGUAJE O TIENE UN CARACTER ESPECIAL NO DEFINIDO")
        


"""
    def panel2(self):
        if (self.variable_1.get() != ''):
            alfabeto = self.control.separadoLenguaje(self.variable_1.get())
            labelTop = Label(self.view, text = "Elegir").place(x=20, y=80)
            comboExample = ttk.Combobox(self.view, values=alfabeto).place(x=20, y=100)
            
            self.label_2 = Label(self.panel,text="Instruccion: ").place(x=200, y=80)
            self.input_2 = Entry(self.panel,textvariable = self.variable_2, width=10).place(x=200, y=100)
            
            print(comboExample.get(), ' ',self.variable_2.get())

        else:
            messagebox.showinfo(message="EL ALFABETO NO ES CORRECTO", title="ERROR")
"""
       
        
        
    

