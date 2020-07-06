# -*- coding: utf-8 -*-
import pydot
import graphviz

class Graph:
    
     def __init__(self):
        self.graph = pydot.Dot(graph_type='digraph')
        self.dot = graphviz.Digraph()
        
    
"""        
     def graphicTree(self, lista):
       cont = 0
       cont1 = 1
       a = []
       for i in lista:
           b = {}
           z = []
           padres = list(i.keys())
           hijos =  list(i.values()) 
           
           aux = padres[0]+"-"+str(cont)
           
          
           for x in hijos:
               h1 = x[0]+"-"+str(cont1)
               z.append(h1)
               cont1 = cont1+1
               h2 = x[1]+"-"+str(cont1)
               z.append(h2)
               b[aux] = z
               a.append(b)
               cont = cont + 1
               
       print(a) 

       self.imprimir(a)
       
     def imprimir(self, listado):
         for x in listado:
             items = x.items()
             lis = list(items)             
             for i in lis[0][1]:
                 self.dot.edge(lis[0][0], i)
         self.dot.render('test-output/round-table.png', view=True)
  
"""
         
            
   
