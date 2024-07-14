from ..enums.update_info_enum import UpdateInfo

from typing import Tuple

class EdgeInfo:
    def __init__(self, edge: Tuple[int, int], update: UpdateInfo) -> None:
        self.edge = edge
        self.update = update