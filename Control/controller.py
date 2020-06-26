# -*- coding: utf-8 -*-

class Controller:
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
        caracteresEspeciales = ['(',')','+','?','*','|','.']  
        encontrado = True        
        for x in lenguaje:
            caracteresEspeciales.append(x)        
        for x in exprecionRegular:
            if x not in caracteresEspeciales:
                encontrado = False
                break       
        return encontrado
        

