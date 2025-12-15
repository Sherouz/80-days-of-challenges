# Challenge #65 - Intermediate
# Breadth-First Search (BFS)
# Objective: Traverse a tree level by level using a queue.

"""
Traverse a tree using Breadth-First Search (BFS).
Demonstrates queue-based traversal and level-order exploration.
Useful for understanding shortest-path and layer-based processing.
"""

from collections import deque


def bfs(tree: dict, start):
    """Perform BFS traversal starting from the given node."""
    visited = []                    # store traversal order
    queue = deque([start])          # queue for BFS (FIFO)

    while queue:
        node = queue.popleft()      # take next node from the front

        if node not in visited:
            visited.append(node)    # mark node as visited

            # enqueue children in natural order (left to right)
            for child in tree.get(node, []):
                queue.append(child)

    return visited


if __name__ == "__main__":
    # define a simple tree structure
    tree = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": [],
        "F": []
    }

    start_node = "A"                # starting point for BFS

    print(f"Tree: {tree}")
    print(f"Starting BFS from node: {start_node}")

    traversal = bfs(tree, start_node)
    print(f"BFS Traversal Order: {traversal}")
