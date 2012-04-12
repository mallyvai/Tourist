''' Some basic shared objects for representing our graph structures. '''
from collections import namedtuple
from collections import defaultdict

Coord = namedtuple('Coord', ['x','y'])
WeightedEndOfEdge = namedtuple('WeightedEndOfEdge', ['weight', 'coord'])
DNode = namedtuple('DNode', ['weight', 'coord', 'path'])

# FIXME Currently unused. Intended for storing extra metadata about the path so we don't have to shove the whole path-with-destination into memory every time we run into an appropriate one.
TourNode = namedtuple('TourNode', ['weight','coord','path','unique_coords'])
    
class LazyGraph(defaultdict):
    default_weight = 1
    def _isValidNode(self, coord):
        return (0 <= coord.x < self.grid_size) and (0 <= coord.y < self.grid_size)

    def _getAllValidAdjacentCoords(self, coord):
        potential_coords = (Coord(coord.x + 0, coord.y + 1),
                            Coord(coord.x + 0, coord.y + -1),
                            Coord(coord.x + -1, coord.y + 0),
                            Coord(coord.x + 1, coord.y + 0))
    
        return [coord for coord in potential_coords if self._isValidNode(coord)]

    def __init__(self, grid_size, special_weights, interesting_destinations, *args, **kargs):
        '''
        Adjacency-list-style graph object made for this problem. Does not explicitly store
        all nodes as a graph. Instead only stores those nodes which have special weights,
        and returns 1 for all other relevant edge weights. This is a huge memory saver.

        Technically a defaultdict, but we're adding additional constraints/checks around it.

        Params::
            grid_size:: Integer representing the number of cells on one side in the square grid;
                        Number of grid cells = grid_size * grid_size

            special_weights::   Iterable of tuples like this: [(Coord(1,2), Coord(1,1), 3),
                                                               (Coord(3,3), Coord(1,1), 3)
                                                              ]
                                Represents special edge weights from the first coord to the
                                second coord.

            interesting_destinations:: An iterable representing interesting destinations that
                                       should be visited.

            *args::     Any additional arguments that might be passed to a builtin dictionary

            **kargs::   Any additional keyword arguments that might be passed to a builtin dictionary
        '''
        
        super(type(self), self).__init__(list, *args, **kargs)
        
        self.grid_size = grid_size
        self.interesting_destinations = interesting_destinations
        
        # According to the original spec we can only move up/down/left/right.
        # So if someone is trying to define a weight to a location that
        # isn't up/down/left/right, this is a kind of input validation exception.
        #
        # Also this graph is effectively undirected, so we define both the forward
        # and backward edges in this case.
        #
        # TODO: Implement defensive coding check to make sure that
        # there are no multiedges in the graph.

        for edge_weight in special_weights:
            start, end, weight = edge_weight
            
            vector = Coord(abs(end.x - start.x), abs(end.y - start.y))
            valid = (vector.x == 1 and vector.y == 0) or (vector.x == 0 and vector.y == 1)

            if not (self._isValidNode(start) and self._isValidNode(end)):
                raise RuntimeError(str(edge_weight) + " has invalid coordinates.")

            if not valid:
                raise RuntimeError(str((edge_weight) + " is not a valid edge."))


            end_of_edge = WeightedEndOfEdge(weight, end)
            super(type(self), self).__getitem__(start).append(end_of_edge)
            reverse_end_of_edge = WeightedEndOfEdge(weight, start)
            super(type(self), self).__getitem__(end).append(reverse_end_of_edge)

    def __getitem__(self, node):
        if not self._isValidNode(node):
            raise RuntimeError(str(node) + " is an invalid coordinate.")
        
        coords = self._getAllValidAdjacentCoords(node)
        existing_ends_of_edges = super(type(self), self).__getitem__(node)
    
        for existing_end_of_edge in existing_ends_of_edges:
            coords.remove(existing_end_of_edge.coord)

        default_ends_of_edges = [WeightedEndOfEdge(self.default_weight, coord) for coord in coords]

        return super(type(self), self).__getitem__(node) + default_ends_of_edges
        
    ''' 
    def __setitem__(self, node, adjacents):
        
        super(type(self), self).__setitem__(node, adjacents)
    '''

    def __contains__(self, coord):
        return self._isValidNode(coord)

# TODO: Implement this
# TODO: An @unimplemented("log message, hooray") decorator might be nice? maybe?
    def __iter__(self):
        '''Unimplemented for now.'''
        pass

    pass
