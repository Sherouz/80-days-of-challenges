# Challenge #66 - Intermediate
# Invert Binary Tree
# Objective: Mirror a binary tree by swapping left and right children.

"""
Invert (mirror) a binary tree by swapping left and right nodes.
Demonstrates recursive tree traversal and structural transformation.
Useful for understanding tree symmetry and recursion basics.
"""

def invert_tree(tree: dict, node):
    """Recursively invert the binary tree starting from the given node."""
    if node is None:
        return

    left, right = tree.get(node, (None, None))   # get left and right children

    tree[node] = (right, left)                   # swap children

    invert_tree(tree, left)                      # invert left subtree
    invert_tree(tree, right)                     # invert right subtree


if __name__ == "__main__":
    # define a simple binary tree: node -> (left, right)
    tree = {
        "A": ("B", "C"),
        "B": ("D", "E"),
        "C": (None, "F"),
        "D": (None, None),
        "E": (None, None),
        "F": (None, None),
    }

    root = "A"                    # root of the tree

    print("Original tree:")
    print(tree)

    invert_tree(tree, root)     # invert the tree in-place

    print("\nInverted tree:")
    print(tree)
