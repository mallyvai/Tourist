#!/usr/bin/env python3
import unittest
import os

if __name__ == "__main__":
    this_dir = os.path.dirname(os.path.realpath(__file__))
    suite = unittest.TestLoader().discover(this_dir)
    unittest.TextTestRunner(verbosity=2, descriptions=True).run(suite)
