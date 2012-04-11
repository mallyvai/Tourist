#!/usr/bin/env python3

import unittest, random


import tourist
from shared_objects import Coord, WeightedEndOfEdge

class TestShortestPaths(unittest.TestCase):
   
    # Very ghetto (or pythonic?) way to essentially dicard 'self' so we can
    # make calls like self.findPath.
    # But TestShortestPaths.findPath won't work!
    findPath = lambda self, *args, **kargs: tourist.pathInWeightedGraph(*args, **kargs)

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

    
