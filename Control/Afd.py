# -*- coding: utf-8 -*-

class Afd:
    
    
    #el inicial lo voy a menter en el init
    def  __init__(self,inicial, recorrido):
        self.grafo = recorrido
        self.biblioteca = {}
        self.recorridoLanda = []
        self.recorridoLanda.append(inicial)
    
    
    def creatorAFD(self,inicial, salida, recorridos = []):         
           
      
        if salida == 0:

        
            for x in self.grafo:
                if inicial == x[0]:
                    if x[1] == '@':
                        recorridos.append(x[2]) 
                        self.recorridoLanda.append(x[2])
                    
            if recorridos == []:
                self.creatorAFD(inicial,1,recorridos)
            else:
                ini = recorridos.pop(0)
                self.creatorAFD(ini, salida, recorridos)                
            
        else:
            numero = [1,2,3,4,5,6]
            c = numero.pop()
            print(c)
            self.biblioteca[chr(65)] = self.recorridoLanda
            print(self.biblioteca)
            l1 = [1,2,3,4]
            l2 = [1,2,3,5]
            print(l1==l2)
        
    
        #print(chr(65))
        