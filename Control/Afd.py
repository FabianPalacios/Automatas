# -*- coding: utf-8 -*-

class Afd:
    
    global grafo
    global biblioteca
    global recorridoLanda
    cont = 65
    cont2 = 1
    estadoInicial = []
    estadoAceptacion = []
    #el inicial lo voy a menter en el init

    def __init__(self,inicial, recorrido):
        self.grafo = recorrido
        self.biblioteca = {}
        self.recorridoLanda = []
        self.recorridoLanda.append(inicial)        
        self.estados = self.estado()
        self.listaPopTupla = []
        self.arregloRecorridos = []
        self.grafoAFD = []
        self.recorridoInicial(inicial)   
        self.creatorAFD(self.recorridoLanda)
        
    def recorridoInicial(self,inicial):
        liss = []
        liss.append(inicial)
        self.recorridosLambdaEstados(liss)
        self.biblioteca[chr(self.cont)] = self.recorridoLanda
        self.estadoInicial.append(chr(self.cont))
        self.cont = self.cont+1
        self.arregloRecorridos.append(self.recorridoLanda)
        self.listaPopTupla.append(self.recorridoLanda)
        
    def creatorAFD(self, arreglo):       
               
        parte = arreglo
        self.recorridoLanda = [] 
        lista = []       
        for x in self.estados:
            for j in x:
                if j[0] in parte:
                    lista.append(j[2])
                    self.recorridoLanda.append(j[2])            
            self.recorridosLambdaEstados(lista)
            
            if self.recorridoLanda != []:
                self.auxiliar(parte, j[1], self.recorridoLanda)
            self.recorridoLanda = []           
        self.evaluarEscape()
            
    def evaluarEscape(self):
        digito = len(self.biblioteca)-1
        if self.cont2 <= digito:
            listaTuplas = list(self.biblioteca.items()) 
            tupla = listaTuplas[self.cont2]
            self.cont2 = self.cont2+1
            self.creatorAFD(tupla[1])
            
        
    def auxiliar(self, partes, estado, recorrido):
        
        #print(partes,' - ', estado,' - ', recorrido)        
        tuplas = list(self.biblioteca.items())        
        if recorrido not in self.arregloRecorridos:
            self.arregloRecorridos.append(recorrido)
            self.biblioteca[chr(self.cont)] = self.recorridoLanda
            self.cont = self.cont+1            
            for x in tuplas:
                if x[1] == partes:
                    self.grafoAFD.append([x[0],estado,chr(self.cont-1)])
        else:
            for x in tuplas:
                if x[1] == recorrido:
                    repetido = x[0]
                if x[1] == partes:
                    anterior = x[0]
            self.grafoAFD.append([anterior,estado,repetido])         

        
    # RECORRIDOS LAMBDA SEGUN LOS ESTADOS
    def recorridosLambdaEstados(self, lista):        
        if lista != []:
            inicial = lista.pop()           
            for x in self.grafo:
                if str(inicial) == str(x[0]):
                    if str(x[1]) == '@':
                        lista.append(x[2]) 
                        self.recorridoLanda.append(x[2])                                       
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
    
    def estadodeAceptacion(self,acepta):
        tuplas = list(self.biblioteca.items())
        print(acepta, 'acepta')
        for x in tuplas:
            print(x[1])
            if str(acepta) in x[1]:
                self.estadoAceptacion.append(x[0])
        
                
        
