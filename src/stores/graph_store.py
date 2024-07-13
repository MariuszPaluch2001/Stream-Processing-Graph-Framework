class GraphStore:
    def __init__(self):
        pass
    
    def get_graph(self):
        raise NotImplementedError
    
    def update_graph(self, edges):
        raise NotImplementedError