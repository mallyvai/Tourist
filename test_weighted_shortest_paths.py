from test_shortest_paths import TestShortestPaths
from shared_objects import Coord, WeightedEndOfEdge

class TestWeightedShortestPaths(TestShortestPaths):

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
        actual_path = self.findPath(self.trivial_graph, start, end)
        

        self.assertEqual(
            actual_path,
            desired_path,
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


        actual_path = self.findPath(self.increasing_line_graph, start, end)

        self.assertEqual(
            actual_path,
            desired_path,
        )
        

    
    def testDisconnectedGraphReturnsNone(self):
        '''A totally disconnected graph that should return None, since no path exists.'''
        
        disconnected_graph = {
            Coord(0,0): [],
            Coord(5,5): [],
            Coord(-1,-1): []
        }

        self.assertIsNone(
            self.findPath(
                disconnected_graph, Coord(0,0), Coord(5,5)
            )
        )
    
    def testRandomGraphsReturnsOptimalPaths(self):
        '''UNIMPLEMENTED Generates many random graphs ; tests them all to make sure the optimals are returned '''
        pass


