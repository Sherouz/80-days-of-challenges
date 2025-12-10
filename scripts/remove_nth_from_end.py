# Challenge #60 - Intermediate
# Remove Nth Node From End of Linked List
# Objective: Use two-pointer technique to remove a node efficiently in one pass.

"""
Remove the Nth node from the end of a singly linked list using two pointers.
Demonstrates pointer spacing, safe traversal, and in-place linked list modification.
Useful for mastering one-pass linked list algorithms.
"""

class Node:
    """Simple singly linked list node."""
    def __init__(self, value: int):
        self.value = value
        self.next = None


def remove_nth_from_end(head: Node, n: int) -> Node:
    """
    Remove the Nth node from the end using fast/slow pointers.
    Returns the new head after deletion.
    """
    dummy = Node(0)    # dummy node to simplify edge cases (like deleting head)
    dummy.next = head

    fast = dummy    # fast pointer
    slow = dummy    # slow pointer

    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        if fast is None:
            return head    # n is larger than list length
        fast = fast.next

    # Move both fast and slow together until fast hits the end
    while fast is not None:
        fast = fast.next
        slow = slow.next

    # slow is now just before the node to delete
    slow.next = slow.next.next

    return dummy.next    # new head of the list


def build_linked_list(values: list[int]) -> Node:
    """Build a linked list from a list of integers."""
    if not values:
        return None

    head = Node(values[0])    # create the first node using the first element
    curr = head    # 'curr' will track the last node while building the list

    for v in values[1:]:      # iterate through the remaining values
        curr.next = Node(v)   # create a new node and attach it to the current one
        curr = curr.next      # move to the newly added node

    return head     # return the head of the constructed linked list


def print_linked_list(head: Node) -> None:
    """Print linked list values cleanly."""
    curr = head    # start traversal from the head
    nodes = []    # store node values for formatted output

    while curr is not None:         # iterate until the end of the list
        nodes.append(str(curr.value))  # record current node's value
        curr = curr.next            # move to the next node

    print(f"Linked List: {' -> '.join(nodes)}")   # print values joined by arrows


def main():
    # read user input for list elements
    raw_nums = input("Enter list values (space-separated): ").strip()

    # read user input for the 'n' value
    raw_n = input("Enter n (which node from the end to remove): ").strip()
                                     
    # validate that both inputs exist
    if raw_nums == "" or raw_n == "":  
        print("Invalid input. Exiting.")
        return

    # convert input string into a list of integers
    nums = list(map(int, raw_nums.split()))

    # convert the second input to an integer (nth from the end)
    n = int(raw_n)

    # create a linked list from the provided numbers
    head = build_linked_list(nums)   
    print(f"Original list:")         # show the initial list before deletion
    print_linked_list(head)

    # remove the nth node from the end using two-pointer method
    new_head = remove_nth_from_end(head, n)

    # show the modified linked list after deletion
    print(f"List after removing {n}th node from the end:")
                                     
    # print the final structure of the list
    print_linked_list(new_head)      


# Entry point for script execution
if __name__ == "__main__":
    main()
