class GraphStore:
    def __init__(self):
        pass
    
    def get_snapshot(self):
        raise NotImplementedError
    
    def add_edge(self, edge):
        raise NotImplementedError
    
    def remove_edge(self, edge):
        raise NotImplementedError