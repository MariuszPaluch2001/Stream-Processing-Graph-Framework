from graph_store import GraphStore
import networkx as nx

class FactoryView:
    def __init__(self) -> None:
        pass
    
    def __select_view(self, data, graph_type):
        match graph_type:
            case "undirect":
                G = nx.Graph(data)
                return
            case "direct":
                G = nx.DiGraph(data)
                return
            case _:
                raise NotImplementedError
    
    def create_view(self, graph: GraphStore, graph_type: str) -> nx.Graph:
        G = self.__select_view(graph, graph_type)
        return G