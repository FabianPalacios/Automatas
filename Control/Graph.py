import graphviz

from Control.Controller import Controller

class Graph:
    
    
    def __init__ (self):
        self.control = Controller()
        self.graph = graphviz.Digraph('finite_state_machine', filename='fsm.gv')
        self.graph.attr(rankdir='LR', size='8,5')
        
    
    def Conexiones(self, lista, aceptacion, inicial):
       self.graph.node('ini', shape="point")
       self.graph.edge('ini',str(inicial[1]))
       
       
       self.graph.attr('node', shape='doublecircle')
       self.graph.node(str(aceptacion[1]))
       
       
       
       self.graph.attr('node', shape='circle')
       for i in lista:
           self.graph.edge(i[0], i[2], label=i[1])
       self.graph.view()