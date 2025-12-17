# Challenge #67 - Intermediate
# Shortest Path in Unweighted Graph
# Objective: Find the shortest path between two nodes using BFS.

"""
Find the shortest path in an unweighted graph using Breadth-First Search (BFS).
Demonstrates queue-based traversal and parent tracking for path reconstruction.
Useful for routing, networking, and graph navigation problems.
"""

from collections import deque


def shortest_path_bfs(graph: dict, start, target):
    """Return the shortest path from start to target using BFS."""
    queue = deque([start])          # queue for BFS traversal
    visited = {start}               # track visited nodes
    parent = {start: None}          # store parent to reconstruct path

    while queue:
        node = queue.popleft()      # process next node in BFS order

        if node == target:
            break                   # shortest path found

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)       # mark as visited
                parent[neighbor] = node     # record where we came from
                queue.append(neighbor)      # add to BFS queue

    # reconstruct path if target was reached
    if target not in parent:
        return None

    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = parent[curr]

    return path[::-1]               # reverse path (start -> target)


if __name__ == "__main__":
    # define an unweighted graph
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    }

    start_node = "A"
    target_node = "F"

    print("Graph:", graph)
    print(f"Finding shortest path from {start_node} to {target_node}")

    path = shortest_path_bfs(graph, start_node, target_node)

    if path is None:
        print("No path found.")
    else:
        print(f"Shortest path: {path}")
        print(f"Path length: {len(path) - 1}")
