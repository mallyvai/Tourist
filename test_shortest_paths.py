#!/usr/bin/env python3

import unittest, random


import tourist
from shared_objects import Coord, WeightedEndOfEdge
#TODO: Rename to TestGraphOperations
# Because this is used by several
# different things.
class TestShortestPaths(unittest.TestCase):
   

    trivial_graph = {
        Coord(0,0): [WeightedEndOfEdge(1, Coord(1,1))],
        Coord(1,1): [WeightedEndOfEdge(1, Coord(0,0))]
    }

    increasing_line_graph = {
        Coord(0,0): [WeightedEndOfEdge(1, Coord(1,1))],
        Coord(1,1): [WeightedEndOfEdge(1, Coord(0,0)), WeightedEndOfEdge(2, Coord(2,2))],
        Coord(2,2): [WeightedEndOfEdge(2, Coord(1,1)), WeightedEndOfEdge(1, Coord(3,3))],
        Coord(3,3): [WeightedEndOfEdge(4, Coord(2,2)), WeightedEndOfEdge(1, Coord(4,4))],
        Coord(4,4): [WeightedEndOfEdge(4, Coord(3,3))]
    } 

    unbalanced_line_graph = {
        Coord(0,0): [WeightedEndOfEdge(3, Coord(1,1))],
        Coord(1,1): [WeightedEndOfEdge(3, Coord(0,0)), WeightedEndOfEdge(1, Coord(2,2))],
        Coord(2,2): [WeightedEndOfEdge(1, Coord(1,1)), WeightedEndOfEdge(1, Coord(3,3))],
        Coord(3,3): [WeightedEndOfEdge(1, Coord(2,2))]
    }


    mesh_with_hub_graph = {
        Coord(0,0): [   WeightedEndOfEdge(1, Coord(1,1)),
                        WeightedEndOfEdge(1, Coord(2,2)), 
                        WeightedEndOfEdge(1, Coord(3,3))],

        Coord(1,1): [   WeightedEndOfEdge(1, Coord(0,0)), 
                        WeightedEndOfEdge(4, Coord(2,2)),
                        WeightedEndOfEdge(4, Coord(3,3))],

        Coord(2,2): [   WeightedEndOfEdge(1, Coord(0,0)),
                        WeightedEndOfEdge(4, Coord(1,1)),
                        WeightedEndOfEdge(4, Coord(3,3))],

        Coord(3,3): [   WeightedEndOfEdge(1, Coord(0,0)),
                        WeightedEndOfEdge(4, Coord(1,1)),
                        WeightedEndOfEdge(4, Coord(2,2))],
    }


    @classmethod
    def findPath(cls, *args, **kargs):
        ''' Facade function for tourist pathfinding function. '''
        return tourist.pathInWeightedGraph(*args, **kargs)

    ## Next two functions are unused, but could be used somewhere after twiddling.
    ''' 
    Verifies that dijkstra's returns a reversed path if the start and end are reversed.
    We're exploiting the convention that all tests should accept (graph, start, end).
    Of course, since this property only holds if the graph is (effectively) undirected,
    we need to verify that the graph is undirected as well.
    '''

    def verifyIsUndirectedGraph(func):
        '''
        UNUSED
        Verifies that the graph in the argument is effectively undirected.
        Currently an unused decorator... TODO: Use this somewhere!
        '''
        def verifier(graph, start, end):
            for node, weighted_ends_of_edges in graph.items():
                for weighted_end_of_edge in weighted_ends_of_edges:
                    weight, coord = weighted_end_of_edge
                    reverse = shared_objects.WeightedEndOfEdge(weight, node)
                    unittest.assertIn(reverse, graph[coord])
            return func(graph, start, end)
        return verifier

    def verifyReturnsSymmetricResults(test_func):
        ''' UNUSED
        '''
        def verifier(graph, start, end):
            forward = test_func(graph, start, end)
            reverse = test_func(graph, end, start)
            unittest.assertEqual(forward, reverse[::-1])
            return func(graph, start, end)
        return verifier


    @classmethod
    def setUpClass(self):
        self.longMessage = True
    
    def setUp(self):
        random.seed(1)
    
