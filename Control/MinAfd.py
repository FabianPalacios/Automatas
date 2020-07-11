# -*- coding: utf-8 -*-

class MinAfd:  
     lista1 = []
     lista2 = []   
     letras = []
     def __init__(self,estado, recorrido, dic):
         self.diccionario = dic
         self.grafo = recorrido
         self.aceptacion = estado
         self.estados()
         self.tuplasCombinaciones()

         
     # SACA LOS ESTADOS EN ORDEN   
     def estados(self):
        letras = []
        # EXTRAE LOS ESTADOS DE EL GRAFO AFD
        for parte in self.grafo:
                if parte[1] not in letras:
                    letras.append(parte[1]) 
        # ORGANIZA CADA ESTADO EN ORDEN
        letras.sort()
        # SACA LAS KEYS (LOS NODOS) DEL GRAFO Y LAS AGREGA A LA DOS LISTAS        
        lista1 = list(self.diccionario.keys())
        lista2 = list(self.diccionario.keys())
        # ELIMINA LOS ESTADOS DE ACEPTACION PARA CREAR LA SEMI-MATRIZ
        for x in self.aceptacion:
            lista1.remove(x)
            lista2.remove(x)
        # CREACION DE FILAS Y COLUMNAS DE LA SEMI-MATRIZ
        lista1.pop(0)
        lista2.pop()
        # GUARDA COLUMNA, FILAS Y LETRAS (ESTADOS)
        self.letras = letras 
        self.lista1 = lista1
        self.lista2 = lista2
        
        print(self.lista1)
        print(self.lista2)
        
     # EXTRAE LAS TUPLAS DE TODAS LAS COMBINACIONES DE LA SEMI-MATRIZ  
     def tuplasCombinaciones(self):        
        lista1 = self.lista2        
        lista2 = self.lista1
        listaTuplas = []
        # SACA LAS TUPLAS DE LAS DOS SEMI-MATRICES      
        for x in lista1:
            for e in lista2:
                listaTuplas.append((x,e))
            lista2.pop(0)
        print(lista1)
        print(lista2)
        # LLENADO MATRIZ  
        self.matrizllenado(listaTuplas)
        
     # LLENADO MATRIZ SEGUN SU ESTADO
     def matrizllenado(self,listaTuplas):
        matriz = []
        listas = []
        # CREACION MATRIZ SEGUN LAS TUPLAS SACAS DE LAS FILAS Y COLUMNAS
        for i in range(len(listaTuplas)):
            matriz.append([0]*(len(self.letras)+2))            
        
        #  ---- RECORRIDO MATRIZ ----
        # RECORRE LA MATRIZ
        for x in matriz:
            cont = 0
            parte = listaTuplas.pop(0)
            # AGREGA LAS TUPLAS A LA PRIMER POSICION DE LA MATRIZ 
            x[0]= parte
            # SACA LOS PESOS EN DE EL GRAFO (EJE: a,b,c)
            for j in self.letras:
                cont = cont +1
                # RECORRE TUPLA DE LA PRIMERA POSICION DE LA MATRIZ
                for e in parte:
                    # RECORRE EL GRAFO AFD
                    for k in self.grafo:
                        # CONDICION PARA SACAR EL SIGUIENTE NODO SEGUN EL PESO 
                        if e == k[0] and k[1] == j:
                            listas.append(k[2])
                # AGREGA LAS TUPLAS SEGUN EL PESO DE LAS COLUMNAS DE LA MATRIZ    
                x[cont] = tuple(listas)
                listas = []
        print(matriz)
        print()
        print(self.grafo)
        
        
        
        
        
        
        
        
        
