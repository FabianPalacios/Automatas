from tkinter import *
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
        self.variable_1 = StringVar();
        self.label_1 = Label(self.panel,text="Instruccion: ").place(x=405, y=44)
        self.input_1 = Entry(self.panel,textvariable = self.variable_1, width=10).place(x=475, y=44)
        self.btn =  Button(self.panel, text="ACEPTAR", width=20, height=1, 
                           command= lambda : self.control.separadoLenguaje(self.variable_1.get()), 
                           background="SkyBlue2").place(x=415, y=80)
        
   
        
    
