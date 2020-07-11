


class MinAfd:
    
    lista1 = []
    lista2 = []
    letras = []
    
    def  __init__(self, estado, recorrido,dic):
        self.diccionario = dic
        self.grafo = recorrido
        self.aceptacion  = estado
        self.estados()
        
        
        
    
    def estados(self):
        letras = []
        for parte in self.grafo:
            if parte[1] not in letras:
                letras.append(parte[1])
        letras.sort()
        
              
        lista1 =  list(self.diccionario.keys())
        lista2 =  list(self.diccionario.keys())
        
        for x in self.aceptacion:
            lista1.remove(x)
            lista2.remove(x)
            
        lista1.pop(0)
        lista2.pop()
        
        self.letras = letras
        self.lista1 = lista1
        self.lista2 = lista2
        
        print(self.lista1)
        print(self.lista2)
        
        self.tuplasCombinaciones()
    
    def tuplasCombinaciones(self):
        lista1 = self.lista2
        lista2 = self.lista1
        listaTuplas = []
        
        for x in lista1:
            for e in lista2:
                listaTuplas.append((x,e))
            lista2.pop(0)
        #self.matrizllenado(listaTuplas)
        
        
    def matrizllenado(self, listaTuplas):
        matriz = []
        listas = []
        parte =  listaTuplas
        print(parte)
        for i in range(len(listaTuplas)):
            matriz.append([0]*(len(self.letras)+2))
        
        for x in matriz:
            cont = 0
            parte =  listaTuplas.pop(0)
            x[0] = parte
            for j in self.letras:
                cont = cont +1
                
                #ES LA COMBINACION DE LOS ESTADOS
                for e in parte:
                    #Lista grafo AFD
                    for k in self.grafo:
                        if (e == k[0]  and k[1] == j):
                            listas.append(k[2])
                x[cont] = tuple(listas)
                listas = []
                
        print(matriz)
        
        
        
        
        
        