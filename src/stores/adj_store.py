from .graph_store import GraphStore
from typing import List
from .edge_info import EdgeInfo

class AdjacencyStore(GraphStore):
    def __init__(self) -> None:
        super().__init__()
        self.vertex_array = {}
    
    def get_snapshot(self):
        return self.vertex_array
    
    def update(self, snapshot: List[EdgeInfo]):
        for edge_info in snapshot:
            buff = self.vertex_array.setdefault(edge_info.edge[0], [])
            buff.append((edge_info.edge[1], edge_info.update))
            buff = self.vertex_array.setdefault(edge_info.edge[1], [])
            buff.append((edge_info.edge[0], edge_info.update))
