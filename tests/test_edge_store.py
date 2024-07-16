from src.stores.edge_store import EdgeStore
from src.stores.edge_info import EdgeInfo
from src.enums.update_info_enum import UpdateInfo

def test_init():
    edge_store = EdgeStore(4)
    assert edge_store.edge_log == []
    assert edge_store.snapshot_size == 4

def test_add_edge():
    edge_store = EdgeStore(4)
    res = edge_store.add_edge((1,2))
    assert isinstance(res, EdgeInfo)
    assert res.edge == (1,2)
    assert res.update == UpdateInfo.ADD
    
    assert isinstance(edge_store.edge_log[0], EdgeInfo)
    assert edge_store.edge_log[0].edge == (1,2)
    assert edge_store.edge_log[0].update == UpdateInfo.ADD
    
def test_remove_edge():
    edge_store = EdgeStore(4)
    res = edge_store.remove_edge((1,2))
    assert isinstance(res, EdgeInfo)
    assert res.edge == (1,2)
    assert res.update == UpdateInfo.REMOVE
    
    assert isinstance(edge_store.edge_log[0], EdgeInfo)
    assert edge_store.edge_log[0].edge == (1,2)
    assert edge_store.edge_log[0].update == UpdateInfo.REMOVE

def test_get_snapshot():
    snapshot_size = 4
    
    edge_store = EdgeStore(snapshot_size)

    edge_store.update((1,2))
    edge_store.update((3,4))
    edge_store.update((5,6))
    edge_store.update((7,8))
    
    res = edge_store.get_snapshot()
    assert len(res) == snapshot_size
    
    assert res[0].edge == (1,2)
    assert res[1].edge == (3,4)
    assert res[2].edge == (5,6)
    assert res[3].edge == (7,8)
    

def test_get_historic_snapshot():
    snapshot_size = 4
    
    edge_store = EdgeStore(snapshot_size)

    edge_store.update((1,2))
    edge_store.update((3,4))
    edge_store.update((5,6))
    edge_store.update((7,8))
    edge_store.update((9,10))
    edge_store.update((11,12))
    edge_store.update((13,14))
    edge_store.update((15,16))

    res = edge_store.get_historic_snapshot(0)
    assert len(res) == snapshot_size
    assert res[0].edge == (1,2)
    assert res[1].edge == (3,4)
    assert res[2].edge == (5,6)
    assert res[3].edge == (7,8)

    res = edge_store.get_historic_snapshot(1)
    assert len(res) == snapshot_size
    assert res[0].edge == (9,10)
    assert res[1].edge == (11,12)
    assert res[2].edge == (13,14)
    assert res[3].edge == (15,16)