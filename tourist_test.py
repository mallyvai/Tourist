#!/usr/bin/env python3

import unittest, pprint, random
from collections import defaultdict


import tourist
from shared_objects import Coord, WeightedEndOfEdge

pp = pprint.PrettyPrinter()


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


    def setUp(self):
        self.longMessage = True
        random.seed(1)

class TestWeightedShortestPath(TestShortestPaths):

    def testTrivialGraphReturnsOnlyEdge(self):
        '''A graph with just two edges should return exactly the first edge as being in the path between the nodes. '''
        start = Coord(0,0)
        end = Coord(1,1)

        start_weighted_end_of_edge = WeightedEndOfEdge(10, end)
        end_weighted_end_of_edge = WeightedEndOfEdge(10, start)

        trivial_graph = {
            start : [start_weighted_end_of_edge],
            end: [end_weighted_end_of_edge]
        }
    
        desired_path = [start, end]

        actual_path = tourist.pathInWeightedGraph(self.trivial_graph, start, end)
        

        self.assertEqual(
            actual_path,
            desired_path,
            "start: " + str(start) + ", end: " + str(end) + "\n"+pp.pformat(actual_path) + "\n" + pp.pformat(desired_path)
        )

    
    def testLineGraphReturnsLinePath(self):
        '''A degenerate list-graph should return the the whole list if the start and end nodes are the head and tail of the list. '''
        
        start = Coord(0,0)
        end = Coord(4,4)

        desired_path = [
            Coord(0,0),
            Coord(1,1),
            Coord(2,2),
            Coord(3,3),
            Coord(4,4)
        ]


        actual_path = tourist.pathInWeightedGraph(self.increasing_line_graph, start, end)

        self.assertEqual(
            actual_path,
            desired_path,
            "start: " + str(start) + ", end: " + str(end) + "\n"+pp.pformat(actual_path) + "\n" + pp.pformat(desired_path)
        )
        

    
    def testDisconnectedGraphReturnsNone(self):
        '''A totally disconnected graph that should return None, since no path exists.'''
        disconnected_graph = {
            Coord(0,0): [],
            Coord(5,5): [],
            Coord(-1,-1): []
        }

        self.assertIsNone(
            tourist.pathInWeightedGraph(
                disconnected_graph, Coord(0,0), Coord(5,5)
            )
        )
    
    def testRandomGraphsReturnsOptimalPaths(self):
        '''UNIMPLEMENTED Generates many random graphs ; tests them all to make sure the optimals are returned '''
        pass

    
class TestConstrainedRepeatingWeightedShortestPath(TestWeightedShortestPath):

    def _simpleTouristAlgorithm(self):
        ''' Brute-force algorithm to check the more complicated Dijkstra's-based variant. '''

        pass

    def testSecondNodeStartInUnbalancedLineGraphWithConstraintReturnsAllNodes(self):
        ''' A line graph with the tourist starting at the 2nd point should return the whole line.

        Suppose we have
        A line graph:
            A -3- B -1- C -1- D
        We are starting at "B" and ending at "D",
        Our threshold is 8.

        We should go [ B, A, B, C, D ] for a total cost of 8.
        '''
        start = Coord(1,1)
        end = Coord(3,3)

        desired_path = [
            Coord(1,1),
            Coord(0,0),
            Coord(1,1),
            Coord(2,2),
            Coord(3,3)
        ]

        actual_path = tourist.pathInWeightedGraph(self.unbalanced_line_graph, start, end, constraint=8, tourist=True)

        self.assertEqual(
            actual_path,
            desired_path
        )

    def testDistantToHubInMeshHubGraphWithConstraintReturnsStarPath(self):

        start, end, constraint = Coord(1,1), Coord(0,0), 5
        
        desired_path = [Coord(1,1), Coord(0,0), Coord(2,2), Coord(0,0), Coord(3,3), Coord(0,0)]
        
        actual_path = tourist.pathInWeightedGraph(self.mesh_with_hub_graph, start, end, constraint=constraint, tourist=True )

        self.assertEqual(
            actual_path,
            desired_path
        )

#TODO: Implement the load_tests protocol
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeightedShortestPath)
    unittest.TextTestRunner(verbosity=2, descriptions=True).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestConstrainedRepeatingWeightedShortestPath)
    unittest.TextTestRunner(verbosity=2, descriptions=True).run(suite)
