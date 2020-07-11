import graphviz

class Graph:
    
    
    def __init__ (self, nombre):
        self.graph = graphviz.Digraph(nombre,format='png')
        self.graph.attr(rankdir='LR', size='8,5')
        
    
    def Conexiones(self, lista, aceptacion, inicial):
        
       self.graph.node('ini', shape="point")
       self.graph.edge('ini',str(inicial[0]))
           
       for x in aceptacion: 
           self.graph.attr('node', shape='doublecircle')
           self.graph.node(str(x))
           
       
       self.graph.attr('node', shape='circle')
       for i in lista:
           self.graph.edge(i[0], i[2], label=i[1])
       self.graph.view()