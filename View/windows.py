
from tkinter import *
import tkinter as tk
<<<<<<< HEAD
from Control.controller import controller
=======
from Control.Controller import Controller
>>>>>>> 05ff820a8901e31949b8b81868b4ec0ef4cb80c1
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
        self.botones()
        self.view.mainloop()
        
#Metodo de diseño de la ventana 
    def diseño(self):
        self.view.title("AUTOMATAS Y LENGUAJES FORMALES")
        self.view.geometry('500x350+380+180')
        self.panel = Frame(self.view,width=500, height=350).pack()
         
# Inserta al panel un label y una variable que resive un string
    def labelAndInput(self):               
        self.variable_1 = StringVar()
<<<<<<< HEAD
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
=======
        label_1 = Label(self.panel,text="Alfabeto: ").place(x=121, y=44)
        input_1 = Entry(self.panel,textvariable = self.variable_1, width=25).place(x=175, y=44)
        
        self.variable_2 = StringVar()
        label_2 = Label(self.panel,text="Estados: ").place(x=125, y=75)
        input_2 = Entry(self.panel,textvariable = self.variable_2, width=25).place(x=175, y=75)
        
        self.variable_3 = StringVar()
        label_3 = Label(self.panel,text="Expresión Regular: ").place(x=70, y=106)
        input_3 = Entry(self.panel,textvariable = self.variable_3, width=25).place(x=175, y=106)
        
              
        # Botones         
    def botones(self):
        boton1 = Button(self.panel, text="ACEPTAR", width=8,height=2, background="SkyBlue2", 
                        command= self.accion).place(x=180,y=150)
        
        boton2 = Button(self.panel, text="?", width=2,height=1, background="SkyBlue2", 
                        command= self.ayuda1).place(x=335,y=39)
        
        boton3 = Button(self.panel, text="?", width=2,height=1, background="SkyBlue2", 
                        command= self.ayuda2).place(x=335,y=103)

>>>>>>> 05ff820a8901e31949b8b81868b4ec0ef4cb80c1
    
    # Evento de boton de accion
    def accion(self):
        # llamado de funcion para separar el lenguje
        variableSeparada = self.control.separadoLenguaje(self.variable_1.get())        
        # Retorno validacion correccion sintaxis
        validador = self.control.validacionLexico(variableSeparada,self.variable_3.get())
        self.accionValidacion(validador)
        
    # Funcion para realizar acciones despues de la validacion
    def accionValidacion(self, bandera):
<<<<<<< HEAD
        if bandera:
            print('no hay errores')
=======
        print(bandera)
        if bandera:
            exprecion = self.variable_3.get()
            Arbol = self.control.construirArbolAnalisis(exprecion)
            print(exprecion)
            self.control.postorden(Arbol)
>>>>>>> 05ff820a8901e31949b8b81868b4ec0ef4cb80c1
        else:
            tkinter.messagebox.showerror("ERROR NOT FOUND",
                                         "LA EXPRECIÓN NO CONCUERDA CON EL LENGUAJE O TIENE UN CARACTER ESPECIAL NO DEFINIDO")
        
<<<<<<< HEAD
=======
    def ayuda1(self):
        tkinter.messagebox.showinfo("AYUDA ALFABETO",
                                         "EL ALFABETO DEBE SER ESCRITO SIN ESTACIO Y PRECEDIDO DE RAYA AL MEDIO O GUIÓN."+'\n\n'+"EJEMPLO:"
                                         +"   A - B - C - D - E - F")
    def ayuda2(self):
        tkinter.messagebox.showinfo("AYUDA EXPRECION REGULAR ",
                                         "CARACTERES ESPECILAES: ' ( ', ' ) ', ' + ', ' ? ', ' * ' , ' | ', ' . ', ' & '."+"\n\n"+
                                         "LA EXPRECION REGULAR DEBE SER BINARIA Y COMENZAR EN ' ( ' Y TERMINAR EN ' ) '."+'\n\n'
                                         +"EJEMPLOS: "+'\n'+
                                         "                  ( ( A | ( B . C ) )"+'\n'
                                         "                  ( ( C | ( ( D . E ) | C ) ) . D )" + '\n' 
                                         "                  ( ( A | ( B . C ) ) . ( ( C | ( ( D . E ) | C ) ) . D ) )")   
        
        
>>>>>>> 05ff820a8901e31949b8b81868b4ec0ef4cb80c1

       
        
        
    

