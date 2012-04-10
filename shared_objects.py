''' Some basic shared objects for representing our graph structures. '''
from collections import namedtuple

Coord = namedtuple('Coord', ['x','y'])
WeightedEndOfEdge = namedtuple('WeightedEndOfEdge', ['weight', 'coord'])
DNode = namedtuple('DNode', ['weight', 'coord', 'path'])
TourNode = namedtuple('TourNode', ['weight','coord','path','unique_coords'])
    
TouristNode = namedtuple('TouristNode

class LazyGraph(object):
    pass
