from grafo import Grafo

class Network:

    graph: Grafo
    length: int

    def __init__(self, length: int):
        self.graph = Grafo()
        self.length = length

    def generate_graph(self) -> Grafo:


        return self.graph