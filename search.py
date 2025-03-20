import csv
import random
from math import radians, sin, cos, sqrt, asin
from time import perf_counter

import matplotlib.pyplot as plt


def load_map(node_file="nodes.csv", edge_file="edges.csv"):
    """Loads nodes and edges for a given map

    :param node_file: CSV file representing nodes
    :param edge_file: CSV file representing edges
    :returns: Tuple containing a node dict and edge list

    See example files for correct input data format.

    The node dictionary has the following form:

    {'node42': {'lat': -85.0, 'lon': 40.0} ... }

    The edge list has the following form:

    [{'a': 'node42', 'b': 'node43', 'length': 12}]
    """

    nodes = {n["id"]: n for n in csv.DictReader(open(node_file))}
    edges = list(csv.DictReader(open(edge_file)))

    for node in nodes.values():
        node["lat"] = float(node["lat"])
        node["lon"] = float(node["lon"])

    for edge in edges:
        edge["length"] = float(edge["length"])

    return (nodes, edges)


def get_heuristic(nodes, start, end):
    """Return a heuristic that will never underestimate the cost
    to travel from node_a to node_b

    :param nodes: Dictionary of nodes on map
    :param start: Starting node
    :param end: Ending node
    """

    a = nodes[start]
    b = nodes[end]

    return haversine_distance(a["lat"], a["lon"], b["lat"], b["lon"])


def show_path(nodes, edges, path=[]):
    """Display path using matplotlib

    :param nodes: Dictionary of nodes on map
    :param edges: List of edges on map
    :param path: Path as list of node ids
    """
    data = []

    for e in edges:
        data.append([nodes[e["a"]]["lon"], nodes[e["b"]]["lon"]])
        data.append([nodes[e["a"]]["lat"], nodes[e["b"]]["lat"]])
        if e["a"] in path and e["b"] in path:
            data.append("blue")
        else:
            data.append("gray")

    plt.plot(*data)
    plt.show()


def haversine_distance(lat1, lon1, lat2, lon2):
    """Compute the spherical distance between two locations"""

    R = 6371 * 1000  # Earth's radius in meters

    # Convert latitude and longitude to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Compute deltas
    dlat, dlon = lat2 - lat1, lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))

    distance = R * c
    return distance


def search_depth_first(start, goal, nodes, edges):
    """Perform depth-first search

    :param start: Starting node id
    :param goal: Goal node id
    :param nodes: Dictionary of nodes on map
    :param edges: List of edges on map
    :returns: Path leading to the goal as a list of node ids
    """

    pass


def search_breadth_first(start, goal, nodes, edges):
    """Perform breadth-first search

    :param start: Starting node id
    :param goal: Goal node id
    :param nodes: Dictionary of nodes on map
    :param edges: List of edges on map
    :returns: Path leading to the goal as a list of node ids
    """

    pass


def search_dijkstra(start, goal, nodes, edges):
    """Perform best-first search

    :param start: Starting node id
    :param goal: Goal node id
    :param nodes: Dictionary of nodes on map
    :param edges: List of edges on map
    :returns: Path leading to the goal as a list of node ids
    """

    pass


def search_astar(start, goal, nodes, edges):
    """Perform A-star search

    :param start: Starting node id
    :param goal: Goal node id
    :param nodes: Dictionary of nodes on map
    :param edges: List of edges on map
    :returns: Path leading to the goal as a list of node ids

    You may select your own heuristic, or you may use the `get_heuristic`
    method.

    Using the provided heuristic, this search should always return the
    optimal path while being nearly as fast as depth-first search.
    """

    pass


def validate_path(start, goal, edges, path):
    """Confirms that a path is a valid solution

    :returns: Path length

    >>> validate_path(1, 2, [{'a':1, 'b':2, 'length': 12}], [1, 2])
    12
    """

    if path[0] != start:
        raise Exception(f"Invalid start state (expecting {start}) for {path}")
    if path[-1] != goal:
        raise Exception(f"Path misses goal (expecting {goal}) for {path}")

    length = 0

    for a, b in zip(path, path[1:]):
        for edge in edges:
            if {edge["a"], edge["b"]} == {a, b}:
                length += edge["length"]
                break
        else:
            raise Exception(f"Unable to reach {b} for {path}")

    return length


if __name__ == "__main__":
    nodes, edges = load_map()

    random.seed(42)
    ids = list(nodes.keys())
    tests = [(random.choice(ids), random.choice(ids)) for _ in range(200)]

    for fn in [
        search_depth_first,
        search_breadth_first,
        search_dijkstra,
        search_astar,
    ]:
        elapsed = 0
        path = fn("9585187701", "5441879433", nodes, edges)
        validate_path("9585187701", "5441879433", edges, path)

        length = 0
        for start, goal in tests:
            start_time = perf_counter()
            path = fn(start, goal, nodes, edges)
            elapsed += perf_counter() - start_time
            length += validate_path(start, goal, edges, path)

        print(
            f"{fn.__name__} passed "
            f"in {elapsed:.03f}s "
            f"with total length {length:.02f}"
        )
