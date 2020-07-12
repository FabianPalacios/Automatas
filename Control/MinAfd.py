# -*- coding: utf-8 -*-

class MinAfd:  
     lista1 = []
     lista2 = []   
     letras = []
     def __init__(self,estado, recorrido, dic):
         self.minGrafo = []
         self.minInicial = []
         self.minAcepta = []
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
            
        if len(self.aceptacion) > 1:
            acepta1 = self.aceptacion
            acepta2 = self.aceptacion
            for i in acepta1:
                acepta2.pop(0)
                for j in acepta2:
                    listaTuplas.append((i,j))
        print(listaTuplas)
        #LLENADO MATRIZ 
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
                if listas == []:
                    listas.append('@')
                    listas.append('@')
                elif len(listas) == 1:
                    listas.append('@')                    
                # AGREGA LAS TUPLAS SEGUN EL PESO DE LAS COLUMNAS DE LA MATRIZ    
                x[cont] = tuple(listas)
                listas = []
        self.estadosNODistinguibles(matriz)        
        
     def estadosNODistinguibles(self,matriz):
         distinguibles = []
         bucles = []
         bandera = False 
         for i in matriz:
             for j in range(1,len(i)-1):
                 if i[j][0] == i[j][1]:
                     bucles.append(True)
                 else:
                     bucles.append(False)
             for k in bucles:
                 if k == False:
                     bandera = False
                     break
                 else:
                     bandera = True
             bucles = []
             if bandera == True:
                 distinguibles.append(i[0])
                 i[len(i)-1] = 2
         print(distinguibles)
         self.estadosDistinguibles(matriz)
         
     def estadosDistinguibles(self,matriz):
         bandera = False 
         for i in matriz:
             if i[len(i)-1] != 2:
                 for j in range(1,len(i)-1):
                     if i[j][0] in self.aceptacion or i[j][1] in self.aceptacion:
                         i[len(i)-1] = 1
         #print(matriz, '1')
         self.validacionDistinguibles(matriz)
         
     def validacionDistinguibles(self, matriz):
         for i in matriz: 
             if i[len(i)-1] == 0:
                 #print(i,' iguales de cero')
                 for j in range(len(i)-1):
                     for w in matriz:
                         if w[len(i)-1] != 0:
                             for z in range(len(i)-1):           
                                 if (i[j][0] == w[z][0] and i[j][1] == w[z][1]) or (i[j][0] == w[z][1] and i[j][1] == w[z][0]):
                                     i[len(i)-1] = w[len(w)-1]
                                     break
         self.cargadoCiclos(matriz)
         
     def cargadoCiclos(self, matriz):
         ciclosAceptacion = []
         for i in matriz:
             if i[len(i)-1] == 2:
                 ciclosAceptacion.append(i[0])                 
         graf = self.grafo         
         if ciclosAceptacion != []:
             for j in ciclosAceptacion:
                 string = str(j[0])+str(j[1])
                 for x in graf:
                     if x[0] == j[0] or x[0] == j[1]:
                         x[0] = string
                         if string not in self.minAcepta:
                             self.minAcepta.append(string)
                     elif x[2] == j[0] or x[2] == j[1]:
                         x[2] = string
                         if string not in self.minAcepta:
                             self.minAcepta.append(string)
             self.minInicial = graf[0][0]
             bulen = False
             es = self.minAcepta
             for k in self.aceptacion:
                 for m in es:
                     if k not in m and k not in self.minAcepta:
                         self.minAcepta.append(k)
                         break
             Farruko = []
             for l in graf:
                 if l not in Farruko:
                     Farruko.append(l)
             self.minGrafo = Farruko
                   
                         
                     

                         
             

                             

                 
             
             
         

        
        
        