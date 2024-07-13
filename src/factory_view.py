from enums.graph_types_enum import GraphTypes
from graph_store import GraphStore
import networkx as nx

class FactoryView:
    def __init__(self) -> None:
        pass
    
    def __select_view(self, data, graph_type: GraphTypes) -> nx.Graph | nx.DiGraph | nx.MultiGraph | nx.MultiDiGraph:
        match graph_type:
            case GraphTypes.UNDIRECTED:
                return nx.Graph(data)
            case GraphTypes.DIRECTED:
                return nx.DiGraph(data)
            case GraphTypes.MULTI_UNDIRECT:
                return nx.MultiGraph(data)
            case GraphTypes.MULTI_DIRECT:
                return nx.MultiDiGraph(data)
            case _:
                raise ValueError("Not exisiting graph type.")
    
    def create_view(self, graph: GraphStore, graph_type: GraphTypes) -> nx.Graph | nx.DiGraph | nx.MultiGraph | nx.MultiDiGraph:
        G = self.__select_view(graph, graph_type)
        return G