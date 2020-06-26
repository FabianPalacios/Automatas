# -*- coding: utf-8 -*-

<<<<<<< HEAD
class Controller:
=======
<<<<<<< HEAD
class controller:
=======
from Clases.pila import Pila
from Clases.arbolBinario import ArbolBinario

class Controller:
>>>>>>> 05ff820a8901e31949b8b81868b4ec0ef4cb80c1
>>>>>>> master
    # Separa el lenguaje incertado por el usuario
    def separadoLenguaje(self, lenguaje):
        separado  = lenguaje.split("-")
        return separado
    
    def valores(self, clave, valor):
        print(clave)
        print(valor)
   
    
    # Separa la exprecion Regular ingresada por el usuario 
    #def separadorExprecionREgular(self, ExprecionRegular):
    #    separador = ExprecionRegular.split("")
    #    return separador
    
    # Incerta el lenguaje a los caracteres especiales y evalua que los caracteres de la
    # exprecion regular existan y retorna un true o false segun si encuentra los caracteres
    # o no
    def validacionLexico(self, lenguaje, exprecionRegular):        
<<<<<<< HEAD
        caracteresEspeciales = ['(',')','+','?','*','|','.']  
=======
        caracteresEspeciales = ['(',')','+','?','*','|','.','&']  
>>>>>>> 05ff820a8901e31949b8b81868b4ec0ef4cb80c1
        encontrado = True        
        for x in lenguaje:
            caracteresEspeciales.append(x)        
        for x in exprecionRegular:
            if x not in caracteresEspeciales:
                encontrado = False
                break       
        return encontrado
<<<<<<< HEAD
=======
    
    # Constrccion Arbol    
    def construirArbolAnalisis(self,expresionAgrupada):        
        listaSimbolos = expresionAgrupada        
        pilaPadres = Pila()
        arbolExpresion = ArbolBinario('')
        pilaPadres.incluir(arbolExpresion)
        arbolActual = arbolExpresion        
        for i in listaSimbolos:
            if i == '(':
                arbolActual.insertarIzquierdo('')
                pilaPadres.incluir(arbolActual)
                arbolActual = arbolActual.obtenerHijoIzquierdo()
            elif i not in ['+', '*', ')','|','.','?']:
                arbolActual.asignarValorRaiz(str(i))
                padre = pilaPadres.extraer()
                arbolActual = padre
            elif i in ['+', '*', '|','.','?']:
                arbolActual.asignarValorRaiz(i)
                arbolActual.insertarDerecho('')
                pilaPadres.incluir(arbolActual)
                arbolActual = arbolActual.obtenerHijoDerecho()
            elif i == ')':
                arbolActual = pilaPadres.extraer()
            else:
                raise ValueError
        return arbolExpresion
    
    def postorden(self, arbol):
        if arbol != None:
            self.postorden(arbol.obtenerHijoIzquierdo())
            self.postorden(arbol.obtenerHijoDerecho())
            print(arbol.obtenerValorRaiz())

    

    

>>>>>>> 05ff820a8901e31949b8b81868b4ec0ef4cb80c1
        

