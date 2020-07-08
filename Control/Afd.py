# -*- coding: utf-8 -*-

class Afd:
    
    
    #el inicial lo voy a menter en el init
    
    
    
    biblioteca = {}
    recorridoLanda = []
    def creatorAFD(self,inicial, salida, recorridos = []):         
           
        recorrido = [['0','@','1'],['1','@','2'],['0','@','3'],['3','b','4']
                     ,['2','@','5'],['5','a','6']]
        
        if salida == 0:

        
            for x in recorrido:
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
        