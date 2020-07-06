import pydot

from Control.Controller import Controller

class Graph:
    
    
    def __init__ (self):
        self.control = Controller()
        self.graph = pydot.Dot(graph_type='digraph')
    
    def padre(self, lista):
       cont = 0
       cont1 = 1
       a = []  
       for i in reversed(lista):
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
               cont = cont+1
       print(a)
       self.imprimir(a)
    
    def imprimir(self, listado):
        for i in listado:
            items = i.items()
            lis = list(items)
            node = pydot.Node(lis[0][0], fillcolor="red")
            for j in lis[0][1]:
               self.graph.add_edge(pydot.Edge(node, j))
        self.graph.write_png('example2_graph.png')
            
        

"""           
           for x in hijos:
                cont = cont+1
                node = pydot.Node(aux, fillcolor="red")
                self.graph.add_node(node)
                h1 = x[0]+"\n"+str(cont)
                cont = cont+1
                h2 = str(x[1])+"\n"+str(cont)
                self.graph.add_edge(pydot.Edge(node, h1))
                self.graph.add_edge(pydot.Edge(node, h2))
           cont = cont+1
           self.graph.write_png('example2_graph.png')
"""           