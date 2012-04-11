#!/usr/bin/env python3

import unittest, pprint, random
from collections import defaultdict


import tourist
from shared_objects import Coord, WeightedEndOfEdge

pp = pprint.PrettyPrinter()


    

#TODO: Implement the load_tests protocol
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeightedShortestPath)
    unittest.TextTestRunner(verbosity=2, descriptions=True).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestConstrainedTouristWeightedShortestPath)
    unittest.TextTestRunner(verbosity=2, descriptions=True).run(suite)
