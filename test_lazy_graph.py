import unittest
from shared_objects import LazyGraph, Coord, WeightedEndOfEdge
from test_shortest_paths import TestShortestPaths

class TestLazyGraph(TestShortestPaths):

    def setUp(self):
        self.gridonly_lazy_graph = LazyGraph(10, [], [])

    def testDefaultCentralRetrievalReturnsUnitEdgeWeights(self):
        coord = Coord(5,5)
        # All adjacent to (5,5). No self-edge.
        desired = [ WeightedEndOfEdge(1, Coord(5,6)),
                    WeightedEndOfEdge(1, Coord(5,4)),
                    WeightedEndOfEdge(1, Coord(4,5)),
                    WeightedEndOfEdge(1, Coord(6,5))]
        actual = self.gridonly_lazy_graph[coord]
        self.assertEqual(
            set(desired),
            set(actual))

    def testDefaultOriginRetrievalReturnsTwoUnitEdgeWeights(self):
        coord = Coord(0,0)
        desired = [ WeightedEndOfEdge(1, Coord(0,1)),
                    WeightedEndOfEdge(1, Coord(1,0)) ]
        actual = self.gridonly_lazy_graph[coord]

        self.assertEqual(
            set(desired),
            set(actual))
    
