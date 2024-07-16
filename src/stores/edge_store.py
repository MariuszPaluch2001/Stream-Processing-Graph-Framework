from ..enums.update_info_enum import UpdateInfo
from .graph_store import GraphStore
from .edge_info import EdgeInfo

from typing import List

class EdgeStore(GraphStore):
    def __init__(self, snapshot_size: int) -> None:
        super().__init__()
        self.edge_log = []
        self.snapshot_size = snapshot_size

    def get_historic_snapshot(self, snapshot_idx: int) -> List[EdgeInfo]:
        return self.edge_log[snapshot_idx*self.snapshot_size:(snapshot_idx + 1)*self.snapshot_size]
    
    def get_snapshot(self) -> List[EdgeInfo]:
        return self.edge_log[-self.snapshot_size:]

    def update(self, edge) -> EdgeInfo:
        edge_info = EdgeInfo(edge, UpdateInfo.ADD)
        self.edge_log.append(edge_info)
        return edge_info

    def remove_edge(self, edge) -> EdgeInfo:
        edge_info = EdgeInfo(edge, UpdateInfo.REMOVE)
        self.edge_log.append(edge_info)
        return edge_info