from factory_view  import FactoryView

class Source:
    def __init__(self) -> None:
        self.stream_store = None
        self.batch_store = None
    
    def ingest(self, data):
        # update structure
        ...
        
    def get_view(self, mode: str, graph_type: str):
        # get stream/batch snapshot
        factory = FactoryView()
        return factory.create_view(
            1 if mode == "stream" else 2,
            graph_type
        )