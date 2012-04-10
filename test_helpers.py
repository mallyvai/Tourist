import unittest
from collections import namedtuple
import shared_objects

def verifyIsUndirectedGraph(func):
    '''
    Verifies that the graph in the argument is effectively undirected.
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
    ''' 
    Verifies that dijkstra's returns a reversed path if the start and end are reversed.
    We're exploiting the convention that all tests should accept (graph, start, end).
    Of course, since this property only holds if the graph is (effectively) undirected,
    we need to verify that the graph is undirected as well.
    '''
    @verifyUndirectedGraph
    def verifier(graph, start, end):
        forward = test_func(graph, start, end)
        reverse = test_func(graph, end, start)
        unittest.assertEqual(forward, reverse[::-1])
        return func(graph, start, end)
    return verifier


