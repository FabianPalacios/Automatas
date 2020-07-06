# -*- coding: utf-8 -*-
import pydot
import graphviz

class Graph:
    
     def __init__(self):
        self.graph = pydot.Dot(graph_type='digraph')
        self.dot = graphviz.Digraph()
        
    
