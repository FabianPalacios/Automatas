import sys

class Afnd:
    
    lpos = []
    lista_Trans=[]
    pila_I=['n']
    pila_F=['n']	
    aux = []
    
    def suma (self,elem1, elem2):
        
        ini = elem1
        fin = elem2
        
        ini1 = self.pila_I.pop()
        fin1 = self.pila_F.pop()
        ini2 = self.pila_I.pop()
        fin2 = self.pila_F.pop()
        
        self.lista_Trans.append([str(ini),'@',str(ini2)])
        self.lista_Trans.append([str(fin2),'@',str(ini2)])
        self.lista_Trans.append([str(fin2),'@',str(fin)])        
        self.lista_Trans.append([str(fin),'@',str(ini1)])
        
        self.pila_I.append(ini)
        self.pila_F.append(fin1)
        
    def  interrogacion(self,elem1, elem2):
         
         ini = elem1
         fin = elem2
         
         ini1 = self.pila_I.pop()
         fin1 = self.pila_F.pop()
         ini2 = self.pila_I.pop()
         fin2 = self.pila_F.pop()
         
         self.lista_Trans.append([str(ini),'@',str(fin)])
         self.lista_Trans.append([str(ini),'@',str(ini2)])  
         self.lista_Trans.append([str(fin2),'@',str(fin)])
        
         self.lista_Trans.append([str(fin),'@',str(ini1)])
         
         self.pila_I.append(ini)
         self.pila_F.append(fin1)
    
    def klean(self, elem1, elem2):

        ini = elem1
        fin = elem2 
        
        ini1 = self.pila_I.pop()
        fin1 = self.pila_F.pop()
        ini2 = self.pila_I.pop()
        fin2 = self.pila_F.pop()        
        self.lista_Trans.append([str(ini),'@',str(fin)])
        self.lista_Trans.append([str(ini),'@',str(ini2)])
        self.lista_Trans.append([str(fin2),'@',str(ini2)])   
        self.lista_Trans.append([str(fin2),'@',str(fin)])        
        self.lista_Trans.append([str(fin),'@',str(ini1)])
        self.pila_I.append(ini)
        self.pila_F.append(fin1)
        
# OR(|) CORREGIDO    
    def union(self,elem1,elem2):
        inicio = elem1
        f = elem2 
        ini1 = self.pila_I.pop()
        ini2 = self.pila_I.pop()
        f1 = self.pila_F.pop()
        f2 = self.pila_F.pop()
        self.lista_Trans.append([str(inicio),'@',str(ini1)])
        self.lista_Trans.append([str(inicio),'@',str(ini2)])
        self.lista_Trans.append([str(f1),'@',str(f)])
        self.lista_Trans.append([str(f2),'@',str(f)])
        self.pila_I.append(inicio)
        self.pila_F.append(f)

# CONCATENACION CORREGIDA    
    def conc(self):
        ini1 = self.pila_I.pop()
        ini2 = self.pila_I.pop()
        fin1 = self.pila_F.pop()
        fin2 = self.pila_F.pop()
        self.lista_Trans.append([str(fin2),'@',str(ini1)])
        self.pila_I.append(ini2)
        self.pila_F.append(fin1)   
        
    def thompson(self, cadena):
        cont  =0
        cont2 =1
        for c in cadena:
            if((ord(c)>=97 and ord(c)<=122) or (ord(c)>=65 and ord(c)<=90) or (ord(c)>=48 and ord(c)<=57)):
                self.lista_Trans.append([str(cont),c,str(cont2)])
                self.pila_I.append(cont)
                self.pila_F.append(cont2)
                cont = cont+2
                cont2 = cont+1
            elif (c == '.'):
                self.conc()
            elif (c == '|'):
                self.union(cont,cont2)
                cont = cont+2
                cont2 = cont+1
            elif (c == '*'):
                self.klean(cont,cont2)
                cont = cont+2
                cont2 = cont+1
            elif (c == '+'):
                self.suma(cont,cont2)
                cont = cont+2
                cont2 = cont+1
            elif (c == '?'):
                self.interrogacion(cont,cont2)
                cont = cont+2
                cont2 = cont+1

