import graphviz

class Graph:
    
    
    def __init__ (self):
        self.graph = graphviz.Digraph('finite_state_machine', filename='fsm.gv',format='png')
        self.graph.attr(rankdir='LR', size='8,5')
        
    
    def Conexiones(self, lista, aceptacion, inicial):
       print(inicial, ' - ', aceptacion)
       self.graph.node('ini', shape="point")
       self.graph.edge('ini',str(inicial))
       
       
       self.graph.attr('node', shape='doublecircle')
       self.graph.node(str(aceptacion))
       
       
       
       self.graph.attr('node', shape='circle')
       for i in lista:
           self.graph.edge(i[0], i[2], label=i[1])
       self.graph.view()