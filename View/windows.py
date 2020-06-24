from tkinter import *
import tkinter as tk
from tkinter import messagebox

from Control.controller import controller

from tkinter import ttk

class windows:
    
    
    
# Constructor de la ventana   
    def __init__(self):
        self.ventana()
        
        
# Metodo que crea una ventana e inserta un panel de trabajo
    def ventana(self):
        self.view = Tk()
        self.control = controller()
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
        self.variable_1 = StringVar();
        self.variable_2 = StringVar();
        self.label_1 = Label(self.panel,text="Instruccion: ").place(x=20, y=44)
        self.input_1 = Entry(self.panel,textvariable = self.variable_1, width=10).place(x=100, y=44)
        self.btn =  Button(self.panel, text="ACEPTAR", width=20, height=1, 
                           command= self.panel2, 
                           background="SkyBlue2").place(x=200, y=42)
        
        
    
        
    
    def panel2(self):
        if (self.variable_1.get() != ''):
            alfabeto = self.control.separadoLenguaje(self.variable_1.get())
            labelTop = Label(self.view, text = "Elegir").place(x=20, y=80)
            comboExample = ttk.Combobox(self.view, values=alfabeto).place(x=20, y=100)
            
            self.label_2 = Label(self.panel,text="Instruccion: ").place(x=200, y=80)
            self.input_2 = Entry(self.panel,textvariable = self.variable_2, width=10).place(x=200, y=100)
            
##print(comboExample.get(), ' ',self.variable_2.get())

        else:
            messagebox.showinfo(message="EL ALFABETO NO ES CORRECTO", title="ERROR")

   
        
    
