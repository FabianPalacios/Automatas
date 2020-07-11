# -*- coding: utf-8 -*-

class Afd:
    
    global grafo
    global biblioteca
    global recorridoLanda
    cont = 65
    cont2 = 1
    estadoInicial = []
    estadoAceptacion = []
    
    # INIT CREACION OBJETO CON EL ESTADO INICIAL Y EL GRAFO
    def __init__(self,inicial, recorrido):
        self.grafo = recorrido
        self.biblioteca = {}
        self.recorridoLanda = []
        self.recorridoLanda.append(inicial)        
        self.estados = self.estado()
        self.arregloRecorridos = []
        self.grafoAFD = []
        self.recorridoInicial(inicial)   
        self.creatorAFD(self.recorridoLanda)
        
    # SACA EL PRIMER RECORRIDO DESDE EL ESTADO INICIAL SEGUN LAS LAMBDAS
    def recorridoInicial(self,inicial):
        liss = []
        liss.append(inicial)
        # LLAMADO ESTADO PARA SACAR EL RECORRIDO DE LAMBDAS         
        self.recorridosLambdaEstados(liss)
        # CREA LA DICCIONARIO DE DATO  SEGUN EL RECORRIDO LAMDA (EJ: A:[1,4,5,6,7])
        self.biblioteca[chr(self.cont)] = self.recorridoLanda
        # GUARDA EL ESTADO INICIAL PARA CREAR EL GRAFO AFD
        self.estadoInicial.append(chr(self.cont))
        # SUMA UNA MAS AL CONTADOR PARA ASCII SIGIENTE SEA 'B'
        self.cont = self.cont+1
        # GUARDA EL RECORRIDO PARA EVALUAR SI YA EXISTE PARA LAS SIGUIENTES
        self.arregloRecorridos.append(self.recorridoLanda)
        
    # ARREGLO PARA CREAR EL GRAFO AFD
    def creatorAFD(self, arreglo):       
        # PRIMER RECORRIDO LAMBDA DONDE SE EVALUARAN SEGUN SUS ESTADOS 
        parte = arreglo
        self.recorridoLanda = [] 
        lista = []      
        # RECORRE ESTADOS DONDE PUEDE LLEGAR SEGUN SU PESO (A,a,b)
        for x in self.estados:
            # RECORRE TODOS LOS ESTADOS DONDE PUEDE LLEGAR CON EL PESO (a,b,c)
            for j in x:
                # CONDICION PARA EVALUAR SI LOS RECORRIDOS QUE PUEDE HACER SI
                # EN LA LISTA EXISTE SU NODO
                if j[0] in parte:
                    # LO AGREGA A UNA LISTA PARA EVALUAR SUS LAMBDAS SEGUN SU
                    # RECORRIDOS LAMBDAS
                    lista.append(j[2])
                    self.recorridoLanda.append(j[2])
            # LLAMADO METODO PARA EVALUAR LAS LAMBDAS DE LOS ESTADOS DONDE PUEDE 
            # LLEGAR SEGUN SI EXISTE EL PESO
            self.recorridosLambdaEstados(lista)
            
            # RECORRIDOS LAMBDA SEGUN SI EXISTE EL NODO SEGUN SU PESO  
            if self.recorridoLanda != []:
                # METODO PARA CREAR EL GRAFO SEGUN SUS RECORRIDOS
                self.auxiliar(parte, j[1], self.recorridoLanda)
            self.recorridoLanda = []
        # METODO PARA CREAR LA RECURSIVIDAD Y EVALUAR TODOS RECORRIDOS Y SUS
        # NUEVOS DICCIONARIOS (A:[1,2,3,4,5], B:[3,6,2,1,])
        self.evaluarEscape()
    
    # METODO PARA LA RECURSIVIDAD Y LA EVALUCION DE TODOS LOS DICCIONARIOS
    def evaluarEscape(self):
        # CANTIDAD DE ELEMENTOS QUE POSEE LA BIBLIOTECA 
        digito = len(self.biblioteca)-1
        # CONDICION PARA LLAMAR RECURSIVAMENTE A TODOS LOS ELEMENTOS SIN 
        # QUE EL LLAMADO RECURSIVO SE ROPA
        if self.cont2 <= digito:
            listaTuplas = list(self.biblioteca.items()) 
            tupla = listaTuplas[self.cont2]
            self.cont2 = self.cont2+1
            self.creatorAFD(tupla[1])
            
    # METODO PARA CREAR EL GRAFO 
    def auxiliar(self, partes, estado, recorrido):
        # VUELVE LOS ELEMENTOS DENTRO DE LA BIBLIOTECA UNA TUPLA
        # [(A,[1,2,34,5]), (B,[2,3,4,5])]        
        tuplas = list(self.biblioteca.items()) 
        # CONDICION PARA EVALUAR SI EL RECORRIDO YA EXISTE 
        if recorrido not in self.arregloRecorridos:
            # CREA UN NUEVO DICCIONARIO SI EL RECORRIDO NO EXISTE
            self.arregloRecorridos.append(recorrido)
            self.biblioteca[chr(self.cont)] = self.recorridoLanda
            self.cont = self.cont+1            
            for x in tuplas:
                if x[1] == partes:
                    self.grafoAFD.append([x[0],estado,chr(self.cont-1)])
        else:
            # SI EL RECORRIDO EXITE AGREGA LA CONECCIO HACIA DONDE SE DIRIJE
            # EL NODO QUE ETA SIENDO EVALUADO
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
        # RECORRE EL GRAFO SACANDO PARTE POR PARTE
        for parte in self.grafo:
            # CONDICION PARA EVALUAR QUE NO EXISTAN LAMBDAS
            if parte[1] != '@':
                lista.append(parte)
                # CONDICION PARA EVALUAR QUE NO SE REPITAN
                if parte[1] not in letras:
                    letras.append(parte[1])
        # ORGANIZA LAS LETRAS O PESOS
        letras.sort()
        aux = []
        listaU =[]
        # ORGANIZA LOS ESTADOS CON SUS RECORRIDOS SEGUN SU NODO INCIAL 
        # Y LA LETRA CORRESPONDIENTE
        for x in letras:
            for j in lista:
                if x == j[1]:
                    aux.append(j)
            listaU.append(aux)
            aux = []        
        return listaU
    
    # SACA LOS ESTADOS DE ACEPATACION
    def estadodeAceptacion(self,acepta):
        tuplas = list(self.biblioteca.items())
        for x in tuplas:
            if str(acepta) in x[1]:
                self.estadoAceptacion.append(x[0])
        
                
        
