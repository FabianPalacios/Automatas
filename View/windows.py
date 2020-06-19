
from tkinter import *
import tkinter as tk
from Control.controller import controller

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
        self.variable_1 = StringVar()
        label_1 = Label(self.panel,text="Alfabeto: ").place(x=421, y=44)
        input_1 = Entry(self.panel,textvariable = self.variable_1, width=25).place(x=475, y=44)
        
        self.variable_2 = StringVar()
        label_2 = Label(self.panel,text="Estados: ").place(x=425, y=75)
        input_2 = Entry(self.panel,textvariable = self.variable_2, width=25).place(x=475, y=75)
        
        self.variable_3 = StringVar()
        label_3 = Label(self.panel,text="Expresión Regular: ").place(x=370, y=106)
        input_3 = Entry(self.panel,textvariable = self.variable_3, width=25).place(x=475, y=106)
        
        
        
        boton1 = Button(self.panel,
                             text="ACEPTAR",
                             width=8,height=2,
                             background="SkyBlue2",
                             command= self.accion
                             ).place(x=480,y=150)
    
    def accion(self):
        self.control.separadoLenguaje(self.variable_1.get())
        caracter = tk.Toplevel(self.view)
        caracter.geometry('500x150+420+250')
        caracter.title("Caracteristicas")
       
        
        
    

