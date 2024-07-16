from src.stores.adj_store import AdjacencyStore
from src.stores.edge_info import EdgeInfo
from src.enums.update_info_enum import UpdateInfo

def test_init():
    adj_store = AdjacencyStore()
    assert adj_store.vertex_array == dict()

def test_update():
    adj_store = AdjacencyStore()
    adj_store.update([
            EdgeInfo((1,2), UpdateInfo.ADD),
            EdgeInfo((4,6), UpdateInfo.ADD),
            EdgeInfo((2,3), UpdateInfo.ADD),
            EdgeInfo((5,1), UpdateInfo.ADD),
            EdgeInfo((1,7), UpdateInfo.ADD),
        ])

    assert adj_store.vertex_array[1] == [(2, UpdateInfo.ADD), (5, UpdateInfo.ADD), (7, UpdateInfo.ADD)]
    assert adj_store.vertex_array[2] == [(1, UpdateInfo.ADD), (3, UpdateInfo.ADD)]
    assert adj_store.vertex_array[3] == [(2, UpdateInfo.ADD)]
    assert adj_store.vertex_array[4] == [(6, UpdateInfo.ADD)]
    assert adj_store.vertex_array[5] == [(1, UpdateInfo.ADD)]
    assert adj_store.vertex_array[6] == [(4, UpdateInfo.ADD)]
    assert adj_store.vertex_array[7] == [(1, UpdateInfo.ADD)]
    
def test_get_snapshot():
    adj_store = AdjacencyStore()
    adj_store.update([
            EdgeInfo((1,2), UpdateInfo.ADD),
            EdgeInfo((4,6), UpdateInfo.ADD),
            EdgeInfo((2,3), UpdateInfo.ADD),
            EdgeInfo((5,1), UpdateInfo.ADD),
            EdgeInfo((1,7), UpdateInfo.ADD),
        ])
    
    assert adj_store.vertex_array == {
        1: [(2, UpdateInfo.ADD), (5, UpdateInfo.ADD), (7, UpdateInfo.ADD)],
        2: [(1, UpdateInfo.ADD), (3, UpdateInfo.ADD)],
        3: [(2, UpdateInfo.ADD)],
        4: [(6, UpdateInfo.ADD)],
        5: [(1, UpdateInfo.ADD)],
        6: [(4, UpdateInfo.ADD)],
        7: [(1, UpdateInfo.ADD)],
    }