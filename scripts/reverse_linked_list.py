# Challenge #59 - Intermediate
# Reverse a Singly Linked List
# Objective: Reverse a linked list using pointer manipulation (iterative method).

"""
Reverse a singly linked list by reassigning next pointers.
Demonstrates pointer updates, state tracking, and data-structure manipulation.
Useful for understanding how non-array sequences are traversed and modified.
"""

class Node:
    """Simple singly linked list node."""
    def __init__(self, value: int):
        self.value = value
        self.next = None


def reverse_list(head: Node) -> Node:
    """
    Reverse a linked list iteratively.
    Returns the new head of the reversed list.
    """
    prev = None
    current = head

    while current is not None:
        nxt = current.next        # store next
        current.next = prev       # reverse pointer
        prev = current            # move prev forward
        current = nxt             # move current forward

    return prev


def build_linked_list(values: list[int]) -> Node:
    """Build a linked list from a list of integers and return the head."""
    if not values:
        return None

    head = Node(values[0])          # create the first node using the first list element
    curr = head                     # pointer 'curr' will track the end of the list as we build

    for v in values[1:]:            # iterate through all remaining values
        curr.next = Node(v)         # create a new node and attach it to the current node
        curr = curr.next            # move 'curr' forward to the newly created node

    return head                     # return the head of the fully built linked list


def print_linked_list(head: Node) -> None:
    """Print linked list values cleanly."""
    curr = head   # start traversing from the head node
    nodes = []    # store node values as strings for pretty output

    # continue until the end of the list
    while curr is not None:
        nodes.append(str(curr.value))  # append the current node's value
        curr = curr.next    # move to the next node in the list

    # print values joined with arrows
    print(f"Linked List: {' -> '.join(nodes)}")   



def main():
    raw = input("Enter numbers for the linked list (space-separated): ").strip()

    if raw == "":    # check for empty input
        print("No input provided. Exiting.")   # notify user and stop
        return

    # split input into numbers and convert to integers
    nums = list(map(int, raw.split())) 

    # construct a linked list from the input numbers
    head = build_linked_list(nums)    
    print_linked_list(head)           # display the original list

    # reverse the linked list using pointer manipulation
    reversed_head = reverse_list(head)
    print_linked_list(reversed_head)   # display the reversed list


if __name__ == "__main__":
    main()
