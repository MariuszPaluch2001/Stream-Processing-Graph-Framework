from .graph_store import GraphStore
from typing import List, Dict
from .edge_info import EdgeInfo

class AdjacencyStore(GraphStore):
    def __init__(self) -> None:
        super().__init__()
        self.vertex_array = {}
    
    def get_snapshot(self) -> Dict:
        return self.vertex_array
    
    def update(self, snapshot: List[EdgeInfo]) -> None:
        for edge_info in snapshot:
            buff = self.vertex_array.setdefault(edge_info.first, [])
            buff.append((edge_info.second, edge_info.update))
            buff = self.vertex_array.setdefault(edge_info.second, [])
            buff.append((edge_info.first, edge_info.update))
