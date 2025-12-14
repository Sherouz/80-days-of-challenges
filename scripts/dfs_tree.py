# Challenge #64 - Intermediate
# Depth-First Search (DFS)
# Objective: Traverse a tree deeply using a stack-based DFS approach.

"""
Traverse a tree structure using Depth-First Search (DFS).
Demonstrates stack usage and deep traversal without recursion.
Useful for understanding tree exploration and graph-like structures.
"""

def dfs(tree: dict, start):
    """Perform DFS traversal starting from the given node."""
    visited = []                 # store traversal order
    stack = [start]              # stack for DFS (LIFO)

    while stack:
        node = stack.pop()       # take the top node from stack

        if node not in visited:
            visited.append(node) # mark node as visited

            # push children in reverse order to maintain left-to-right traversal
            for child in reversed(tree.get(node, [])):
                stack.append(child)

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

    start_node = "A"             # starting point for DFS

    print("Tree:", tree)
    print(f"Starting DFS from node: {start_node}")

    traversal = dfs(tree, start_node)
    print(f"DFS Traversal Order: {traversal}")
