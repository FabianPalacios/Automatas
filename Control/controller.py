# -*- coding: utf-8 -*-


from Clases.pila import Pila
from Clases.arbolBinario import ArbolBinario

class Controller:
    # Separa el lenguaje incertado por el usuario
    def separadoLenguaje(self, lenguaje):
        separador = lenguaje.split("-")
        return separador
    
    # Separa la exprecion Regular ingresada por el usuario 
    #def separadorExprecionREgular(self, ExprecionRegular):
    #    separador = ExprecionRegular.split("")
    #    return separador
    
    # Incerta el lenguaje a los caracteres especiales y evalua que los caracteres de la
    # exprecion regular existan y retorna un true o false segun si encuentra los caracteres
    # o no
    def validacionLexico(self, lenguaje, exprecionRegular):        
        caracteresEspeciales = ['(',')','+','?','*','|','.','&']  
        encontrado = True        
        for x in lenguaje:
            caracteresEspeciales.append(x)        
        for x in exprecionRegular:
            if x not in caracteresEspeciales:
                encontrado = False
                break       
        return encontrado
    
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
    
    x= []
    j = []
    def postorden(self, arbol):
        if arbol != None:
            self.postorden(arbol.obtenerHijoIzquierdo())
            self.postorden(arbol.obtenerHijoDerecho())
            self.x.append(arbol.obtenerValorRaiz())
 

    
            
    
