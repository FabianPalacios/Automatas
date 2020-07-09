# -*- coding: utf-8 -*-

class Afd:
    
    global grafo
    global biblioteca
    global recorridoLanda
    
    #el inicial lo voy a menter en el init
    def __init__(self,inicial, recorrido):
        self.grafo = recorrido
        self.biblioteca = {}
        self.recorridoLanda = []
        self.recorridoLanda.append(inicial)        
        self.estados = self.estado()
        self.listaPopTupla = []
        self.creatorAFD(inicial)
        
        
        
    def creatorAFD(self,inicial):
        self.lambdas(inicial,0)
        self.recorridoEstado()
        
        

        
    # SACA EL RECORRIDO DE LANDAS DE EL ESTADO INICIAL
    def lambdas(self,inicial, salida, recorridos = []):        
        if salida == 0:           
            for x in self.grafo:
                if str(inicial) == str(x[0]):
                    if str(x[1]) == '@':
                        recorridos.append(x[2]) 
                        self.recorridoLanda.append(x[2])                    
            if recorridos == []:
                self.lambdas(inicial,1,recorridos)
            else:
                ini = recorridos.pop(0)
                self.lambdas(ini, salida, recorridos)                
            
        elif salida == 1:
            self.biblioteca[chr(65)] = self.recorridoLanda
            self.recorridoLanda = []
            self.listaPopTupla.append(list(self.biblioteca.items()))
            print(list(self.biblioteca.items()))
    
    # SACA LOS RECORRIDOS SEGUN LOS ESTADO Y LAS LAMBDAS
    def recorridoEstado(self):
        lista = []
        if len(self.biblioteca.values()) > 1:
            print()
        else:
            lis = self.listaPopTupla.pop()
            tupla = lis.pop()
            for x in self.estados:
                for j in x:
                    if j[0] in tupla[1]:
                        lista.append(j[2])
                        
                print(lista)
                
                    
                self.recorridosLambdaEstados(lista)                        
                print(self.recorridoLanda)
                self.recorridoLanda = []

    
    # RECORRIDOS LAMBDA SEGUN LOS ESTADOS
    def recorridosLambdaEstados(self, lista):
        
        if lista != []:
            inicial = lista.pop()           
            for x in self.grafo:
                if str(inicial) == str(x[0]):
                    if str(x[1]) == '@':
                        lista.append(x[2]) 
                        self.recorridoLanda.append(x[2])
                    else:
                        
                        
                self.recorridosLambdaEstados(lista)
        
                        
                
            
        
            
    
    
    
    
    
    
    # SACA TODOS LOS ESTADOS EN ORDEN Y EN LISTA
    def estado(self):
        lista = []
        letras = []
        for parte in self.grafo:
            if parte[1] != '@':
                lista.append(parte)
                if parte[1] not in letras:
                    letras.append(parte[1])      
        letras.sort()
        aux = []
        listaU =[]
        for x in letras:
            for j in lista:
                if x == j[1]:
                    aux.append(j)
            listaU.append(aux)
            aux = []        
        return listaU
                
        
        