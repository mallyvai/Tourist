''' Some basic shared objects for representing our graph structures. '''
from collections import namedtuple

Coord = namedtuple('Coord', ['x','y'])
WeightedEndOfEdge = namedtuple('WeightedEndOfEdge', ['weight', 'coord'])
DNode = namedtuple('DNode', ['weight', 'coord', 'path'])

# FIXME Currently unused. Intended for storing extra metadata about the path so we don't have to shove the whole path-with-destination into memory every time we run into an appropriate one.
TourNode = namedtuple('TourNode', ['weight','coord','path','unique_coords'])
    
class LazyGraph(object):
    pass
