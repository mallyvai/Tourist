"""
1) You have some number of hours 
2) You have some number of "interesting destinations" you would (like? need?) to visit
3) 

> Map of US is an (n * n) grid
> List of interesting places [(x_0,y_0,name_0),(x_1, y_1, name_1)...]
> Can only move North, South, East, West (no diagonals) -> 
> List of weights [(x_0, y_0, x_1, y_1, weight_0)] 
> Given:
>   x_start, y
> 


> TSP variant
>   Undirected weighted graph
> Unbreakable constraint - finite amount of time
> "looser" constraint
> 1) Maximize number of intermediate nodes
> 2) Make sure that we don't exceed some net travel time




http://en.wikipedia.org/wiki/Traveling_purchaser_problem -> Not the same problem
http://en.wikipedia.org/wiki/Travelling_salesman_problem


We want to go from some GlobalStart to some GlobalEnd
Some number of "interesting" nodes
Run dijkstras between all interesting nodes (??)
The start and end are also interesting nodes , but we should run dijkstra's starting from GlobalStart
"""

import heapq
from shared_objects import Coord, WeightedEndOfEdge, DNode

def pathInWeightedGraph(graph, start, end, constraint=None, tourist=False):
    '''
    Classic priority-queue-based Dijkstra's implementation to find shortest path
    between two graphs in a weighted, directed graph.

    Based heavily on heapq module: http://docs.python.org/library/heapq.html
    
    Params::
        graph:: Adjacency list ; Coord -> [WeightedEndOfEdge1, WeightedEndOfEdge2...] 
        start:: Coord representing the start node 
        end::   Coord representing the end node
        constraint:: Number that's an upper bound on the cost of the path. If there is no
                     path <= the constraint, returns None.
                    
    Returns::   
        The shortest path as a list of WeightedEndOfEdges.
    '''
    if start not in graph:
        raise Exception("Start coordinate not in graph")

    if end not in graph:
        raise Exception("End coordinate not in graph")
   
    visited = set()
    heap = [DNode(0, start, [])]
    
    destinations = []
    while len(heap) > 0:
        current = heapq.heappop(heap)
        if tourist:
            if current.coord == end:
                destinations.append(current)

        else:
            if current.coord in visited:
                continue
            visited.add(current.coord)

            if current.coord == end:
                destinations.append(current)
                break

        for weighted_end_of_edge in graph[current.coord]:
            weight, next_coord = weighted_end_of_edge
            next_weight = current.weight + weight
            next_path = [current.path, current.coord]

            # If there's a constraint on the path, we need to make sure it's maintained 
            if constraint is not None and next_weight > constraint:
                continue
            node = DNode(next_weight, next_coord, next_path) # Store reference to the path instead of recreating it every time.
            heap.append(node)
        heapq.heapify(heap)

    if len(destinations) is 0:
        return None

    # The tourist condition needs us to return the path that includes as many nodes as possible
    # TODO Run this check at insertion and only store one destination so we don't waste memory
    # This is really obnoxious right now...
    if tourist:
        best_unique, best_path = 0, 0
        for destination in destinations:
            
            flat_path = []
            path = destination.path[:]

            #TODO this flattening algorithm is used in two places ; should be a helper function.

            while len(path) > 0:
                flat_path.insert(0, path.pop(-1))
                path = path[0][:]
            flat_path += [destination.coord]

            unique_destinations = len(set(flat_path))
            if unique_destinations > best_unique:
                best_unique, best_path = unique_destinations, flat_path
            
        return best_path
    destination = destinations[0]
    path = destination.path
    flat_path = []
    

    # Flatten our list-of-reference-lists structure
    while len(path) > 0:
        flat_path.insert(0, path.pop(-1))
        path = path[0]

    return flat_path + [destination.coord]

    """
    '''
def findTheMostInterestingPathInTheWorld(global_start, global_end, grid, weights, interesting_places):
    '''
        grid: n * n list of lists
    '''
    # First we reduce the general graph to one of just the interesting places
    # TODO: Convert the "grid" we are given to an appropriate adjacency list.
    # TODO: Maybe optimize this conversion out later.
    
    interesting_place_graph = defaultdict(list)

    for interesting_start in interesting_places:
        for interesting_end in interesting_places:
            if interesting_start != interesting_end:
                # TODO Since this is actually undirected:
                #   1) Don't bother calculating this if the reverse path is already calculated. 
                #   2) Insert both this path and the reverse path into the interesting_place_graph
                
                path = shortestPathInWeightedGraph(interesting_place_graph, interesting_start, interesting_end)
                weight = sum((end_of_edge.weight for end_of_edge in path))
                weighted_end_of_edge =  WeightedEndOfEdge()
                interesting_place_graph[interesting_start].append((shortest_time, interesting_end))

    
            
    # Now we have the graph of interesting places
    # We want to:
    #   > 1) Maximize number of intermediate nodes
    #   > 2) Make sure that we don't exceed some net travel time

    # Run dijkstra's from start to all interesting places.
    # Then for all that are still under the net travel time,
    #   run it again until we get to the end.
    
    """
