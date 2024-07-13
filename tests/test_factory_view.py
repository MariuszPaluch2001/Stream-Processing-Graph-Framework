from src.enums.graph_types_enum import GraphTypes
from src.factory_view import FactoryView

import networkx as nx

def test_switch_case_factory_view():
    factory = FactoryView()
    
    assert type(factory.create_view([], GraphTypes.UNDIRECTED)) == nx.Graph
    assert type(factory.create_view([], GraphTypes.DIRECTED)) == nx.DiGraph
    assert type(factory.create_view([], GraphTypes.MULTI_UNDIRECT)) == nx.MultiGraph
    assert type(factory.create_view([], GraphTypes.MULTI_DIRECT)) == nx.MultiDiGraph