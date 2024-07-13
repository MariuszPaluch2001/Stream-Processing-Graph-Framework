from factory_view  import FactoryView
from enums.processing_mode_enum import ProcessingTypes
from enums.graph_types_enum import GraphTypes

class Source:
    def __init__(self) -> None:
        self.edge_store = None
        self.adj_store = None
    
    def ingest(self, data):
        ...
    
    def __get_store_for_process_mode(self, mode: ProcessingTypes):
        if mode not in ProcessingTypes:
            raise ValueError("Not existing processing type")
        return self.edge_store if mode == ProcessingTypes.STREAM else self.adj_store
    
    def get_view(self, mode: ProcessingTypes, graph_type: GraphTypes):
        factory = FactoryView()
        return factory.create_view(
            self.__get_store_for_process_mode(mode),
            graph_type
        )