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
        self.view.title("AUTOMATAS Y LENGUAJES FORMALES")
        self.view.geometry('1000x600+180+60')
        self.panel = Frame(self.view,width=1000, height=600).pack()
        self.labelAndInput()
        self.view.mainloop()

# Inserta al panel un label y una variable que resive un string
    def labelAndInput(self):               
        self.variable_1 = StringVar()
        label_1 = Label(self.panel,text="Instruccion: ").place(x=405, y=44)
        input_1 = Entry(self.panel,textvariable = self.variable_1, width=10).place(x=475, y=44)
        boton1 = Button(self.panel,
                             text="ACEPTAR",
                             width=8,height=2,
                             background="SkyBlue2",
                             command= lambda: self.control.separadoLenguaje(self.variable_1.get())
                             ).place(x=425,y=70)

       
        
        
    

