from test_weighted_shortest_paths import TestWeightedShortestPaths
from shared_objects import Coord, WeightedEndOfEdge

class TestConstrainedTouristWeightedShortestPaths(TestWeightedShortestPaths):

    def testSecondNodeStartInUnbalancedLineGraphReturnsAllNodes(self):
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

        actual_path = self.findPath(self.unbalanced_line_graph, start, end, constraint=8, tourist=True)

        self.assertEqual(
            actual_path,
            desired_path
        )

    def testDistantToHubInMeshHubGraphReturnsStarPath(self):
        ''' A complete graph with a cheap "hub" should always go through the hub. Here we start at (1,1) and end at the hub (0,0).

        We have 4 coordinates, with (0,0) being the hub node. Each node is connected to the
        other nodes via an edge of weight 4, with the exception of the hub node, which is
        connected via an edge of weight 1.
        '''
        
        start, end, constraint = Coord(1,1), Coord(0,0), 5
        desired_path = [Coord(1,1), Coord(0,0), Coord(2,2), Coord(0,0), Coord(3,3), Coord(0,0)]
        
        actual_path = self.findPath(self.mesh_with_hub_graph, start, end, constraint=constraint, tourist=True )

        self.assertEqual(
            actual_path,
            desired_path
        )

    def testHubToHubInMeshHubGraphReturnsStarPathButIgnoresLast(self):
        '''A complete graph with a cheap "hub" should always go through the hub. Here we start and end at the hub, but don't give enough constraint to go to the final node.'''

        start, end, constraint = Coord(0,0), Coord(0,0), 4
        desired_path = [Coord(0,0), Coord(1,1), Coord(0,0), Coord(2,2), Coord(0,0)]

        actual_path = self.findPath(self.mesh_with_hub_graph, start, end, constraint=constraint, tourist=True)
        
        self.assertEqual(
            actual_path,
            desired_path
        )

