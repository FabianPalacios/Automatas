# -*- coding: utf-8 -*-

class controller:
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
        caracteresEspeciales = ['(',')','+','?','*','|','.']  
        encontrado = True        
        for x in lenguaje:
            caracteresEspeciales.append(x)        
        for x in exprecionRegular:
            if x not in caracteresEspeciales:
                encontrado = False
                break       
        return encontrado
        

