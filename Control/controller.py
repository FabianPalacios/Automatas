    # -*- coding: utf-8 -*-

import pydot
from Clases.pila import Pila
from Clases.arbolBinario import ArbolBinario

class Controller:   
  
        
    # Separa el lenguaje incertado por el usuario
    def separadoLenguaje(self, lenguaje):
        separador = lenguaje.split("-")
        return separador
    
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
    

    x = []  
    def postorden(self, arbol):  
        if arbol != None:
            self.postorden(arbol.obtenerHijoIzquierdo())
            self.postorden(arbol.obtenerHijoDerecho())
            self.x.append(arbol.obtenerValorRaiz())
        
        
    def eliminarVacios(self,lista):
        aux = 0
        for i in lista:
            if i == '':
                aux = lista.index(i)
                lista.pop(aux)
        return lista
    
       
            
"""           
            
            arbol2 = arbol.obtenerHijoIzquierdo()
            arbol3 = arbol.obtenerHijoDerecho()
            

            if arbol2 != None and arbol3 != None:
                l.append(arbol2.obtenerValorRaiz())
                l.append(arbol3.obtenerValorRaiz())                
                b[str(arbol.obtenerValorRaiz())] = l
                self.j.append(b)
                
            elif arbol2 != None and arbol3 is None:
                l.append(arbol2.obtenerValorRaiz())
                b[str(arbol.obtenerValorRaiz())] = l
                self.j.append(b)
>>>>>>> c6b5769f01da417c376bacada123cd3870c70ad9
            
            elif arbol2 is None and arbol3 != None:
                l.append(arbol3.obtenerValorRaiz())
                b[str(arbol.obtenerValorRaiz())] = l
                self.j.append(b)
"""    
"""
    j1 = []           
    def recorridoAnchura(self,arbol, lp = []):
        b1 = {}
        l1 = []
        arbol1 = None
        if arbol != None:           
            arbol2 = arbol.obtenerHijoIzquierdo()
            arbol3 = arbol.obtenerHijoDerecho()
            
            if arbol2 != None and arbol3 != None:
                l1.append(arbol2.obtenerValorRaiz())
                l1.append(arbol3.obtenerValorRaiz())
                b1[str(arbol.obtenerValorRaiz())]=l1
                lp.append(arbol2)
                lp.append(arbol3)
                self.j1.append(b1)
                
            elif arbol2 != None and arbol3 is None:
                l1.append(arbol2.obtenerValorRaiz())
                b1[str(arbol.obtenerValorRaiz())]=l1
                lp.append(arbol2)
                self.j1.append(b1)
                
            elif arbol2 is None and arbol3 != None:
                l1.append(arbol3.obtenerValorRaiz())
                b1[str(arbol.obtenerValorRaiz())]=l1
                lp.append(arbol3)
                self.j1.append(b1)
            
            if lp != []:
                arbol1 = lp.pop(0)
                
            self.recorridoAnchura(arbol1, lp)
"""

