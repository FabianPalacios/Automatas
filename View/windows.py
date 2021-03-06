
from tkinter import *
import tkinter as tk
from Control.Controller import Controller
from Control.Afnd import Afnd
from Control.Afd import Afd
from Control.MinAfd import MinAfd

from Control.Graph import Graph

import tkinter.messagebox

class Windows:     
# Constructor de la ventana   
    def __init__(self):
        self.ventana()                
        
# Metodo que crea una ventana e inserta un panel de trabajo
    def ventana(self):
        self.view = Tk()

        self.control = Controller()        
        self.automataFND = Afnd()      
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
        boton1 = Button(self.panel, text="ACEPTAR", width=20,height=2, background="SkyBlue2", 
                        command= self.accion).place(x=180,y=150)
        
        boton2 = Button(self.panel, text="?", width=2,height=1, background="SkyBlue2", 
                        command= self.ayuda1).place(x=335,y=39)

        boton3 = Button(self.panel, text="?", width=2,height=1, background="SkyBlue2", 
                        command= self.ayuda2).place(x=335,y=103)
        
        self.boton4 = Button(self.panel, text="No Determinista", width=13,height=2, background="SkyBlue2", 
                        command= self.NoDeterminista, state=tk.DISABLED).place(x=90,y=220)
        
        self.boton5 = Button(self.panel, text="Determinista", width=13,height=2, background="SkyBlue2", 
                        command= self.Determinista, state=tk.DISABLED).place(x=200,y=220)

        self.boton6 = Button(self.panel, text="Miniminista", width=13,height=2, background="SkyBlue2", 
                        command= self.Minimizacion, state=tk.DISABLED).place(x=310,y=220)
    

    # Evento de boton de accion
    def accion(self):
        # llamado de funcion para separar el lenguje
        variableSeparada = self.control.separadoLenguaje(self.variable_1.get())        
        # separado acciones 
        varSeparadaAccion = self.control.separadoLenguaje(self.variable_2.get())
        
        if len(variableSeparada) == len(varSeparadaAccion):        
            # Retorno validacion correccion sintaxis
            validador = self.control.validacionLexico(variableSeparada,self.variable_3.get())
            self.accionValidacion(validador) 
        else:
            tkinter.messagebox.showerror("ERROR LENGUAJE Y ACCION","LA CANTIDAD DE SIMBOLOS EN EL LENGUAJE NO COINCIDE CON LA CANTIDAD DE VALORES AGREGADOS")
            
           
        
    # Funcion para realizar acciones despues de la validacion
    def accionValidacion(self, bandera):
        
        if bandera:
            exprecion = self.variable_3.get()
            Arbol = self.control.construirArbolAnalisis(exprecion)

            self.control.postorden(Arbol)
            
            tkinter.messagebox.showinfo("EXPRECION RECULAR CARGADA","LA EXPRECION REGULAR SE HA CARGADO CORRECTAMENTE")
            
            self.boton4 = Button(self.panel, text="No Determinista", width=13,height=2, background="SkyBlue2", 
                                 command= self.NoDeterminista).place(x=90,y=220)

        else:
            tkinter.messagebox.showerror("ERROR NOT FOUND",
                                         "LA EXPRECIÓN NO CONCUERDA CON EL LENGUAJE O TIENE UN CARACTER ESPECIAL NO DEFINIDO")
        

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

    inicial = []
    final = []
    def NoDeterminista(self):
    
        lista = self.control.eliminarVacios(self.control.x)
        self.automataFND.thompson(lista)
        listaThompson = self.automataFND.lista_Trans

        if (len(self.automataFND.pila_I) == 2) and (len(self.automataFND.pila_F) == 2):
            self.inicial.append(self.automataFND.pila_I.pop())
            self.final.append(self.automataFND.pila_F.pop())     
        else: 
            self.inicial.append(self.automataFND.pila_I)
            self.final.append(self.automataFND.pila_F)

        
        self.grafico = Graph('Thompson')  
        self.grafico.Conexiones(listaThompson, self.final, self.inicial)
        
        self.boton5 = Button(self.panel, text="Determinista", width=13,height=2, background="SkyBlue2", 
                        command= self.Determinista).place(x=200,y=220)
        
    
    def Determinista(self):
        
        inicial =  self.inicial[0]
        final = self.final[0]
        
        self.automataAFD = Afd(inicial, self.automataFND.lista_Trans)
        self.automataAFD.estadodeAceptacion(final)
        
        self.grafico = Graph('Determinista')   
        self.grafico.Conexiones(self.automataAFD.grafoAFD, self.automataAFD.estadoAceptacion, self.automataAFD.estadoInicial)

        self.boton6 = Button(self.panel, text="Miniminista", width=13,height=2, background="SkyBlue2", 
                        command= self.Minimizacion).place(x=310,y=220)

    def Minimizacion(self):
        self.MinAfd = MinAfd(self.automataAFD.estadoAceptacion, self.automataAFD.grafoAFD, self.automataAFD.biblioteca)
        self.grafico = Graph('Minimizacion')   
        self.grafico.Conexiones(self.MinAfd.minGrafo, self.MinAfd.minAcepta,  self.MinAfd.minInicial)