# Challenge #79 - Intermediate
# Deep Copy Graph
# Objective: Create a deep copy of a graph using a hashmap.

"""
Create a deep copy of a graph structure.
Demonstrates handling references, cycles, and shared neighbors using a hashmap.
Useful for cloning complex data structures safely.
"""

def clone_graph(graph: dict, node, clones: dict) -> dict:
    """Recursively clone graph starting from a given node."""
    if node in clones:
        return clones[node]               # return existing clone

    clones[node] = []                     # create clone node

    for neighbor in graph.get(node, []):
        clones[node].append(
            clone_graph(graph, neighbor, clones)
        )                                 # clone neighbors recursively

    return clones[node]


def deep_copy_graph(graph: dict) -> dict:
    """Return a deep copy of the entire graph."""
    clones = {}                           # original -> cloned mapping
    new_graph = {}

    for node in graph:
        if node not in clones:
            clone_graph(graph, node, clones)

    # rebuild adjacency list using cloned references
    for node, neighbors in graph.items():
        new_graph[node] = list(neighbors)

    return new_graph


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["C"],
        "C": ["A"],
    }

    copied_graph = deep_copy_graph(graph)

    print("Original graph:")
    print(graph)

    print("\nCopied graph:")
    print(copied_graph)

    # modify copy to prove deep copy
    copied_graph["A"].append("D")

    print("\nAfter modifying copied graph:")
    print("Original:", graph)
    print("Copied:", copied_graph)
