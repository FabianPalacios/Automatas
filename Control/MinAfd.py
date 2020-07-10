
class MinAfd:
    
    def  __init__(self, estados, recorrido):
        self.grafo = recorrido
        self.aceptacion  = estados
        
    def estados(self):
        