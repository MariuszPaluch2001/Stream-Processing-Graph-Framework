from .factory_view  import FactoryView
from .enums.processing_mode_enum import ProcessingTypes
from .enums.graph_types_enum import GraphTypes
from .stores.graph_store import GraphStore
from .stores.edge_store import EdgeStore
from .stores.adj_store import AdjacencyStore

import networkx as nx

class Source:
    def __init__(self) -> None:
        self.edge_store = EdgeStore()
        self.adj_store = AdjacencyStore()
    
    def ingest(self, data) -> None:
        ...
    
    def __get_store_for_process_mode(self, mode: ProcessingTypes) -> GraphStore:
        if mode not in ProcessingTypes:
            raise ValueError("Not existing processing type")
        return self.edge_store if mode == ProcessingTypes.STREAM else self.adj_store
    
    def get_view(self, mode: ProcessingTypes, graph_type: GraphTypes) -> nx.Graph:
        factory = FactoryView()
        return factory.create_view(
            self.__get_store_for_process_mode(mode),
            graph_type
        )