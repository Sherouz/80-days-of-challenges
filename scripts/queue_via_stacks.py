# Challenge #61 - Intermediate
# Queue via Two Stacks
# Objective: Implement a FIFO queue using two simple stack lists.

"""
Implement a FIFO queue using two plain stacks (lists).
Demonstrates how LIFO structures can simulate queue behavior.
"""

def enqueue(stack_in, value):
    """Push value into the input stack."""
    stack_in.append(value)  # normal push operation


def dequeue(stack_in, stack_out):
    """Remove and return front element using two-stack transfer logic."""
    if not stack_out:                           # if output stack is empty,
        while stack_in:                         # transfer all items from input
            stack_out.append(stack_in.pop())    # reversing their order

    if not stack_out:    # queue is empty
        return None

    return stack_out.pop()    # pop gives FIFO


def print_queue(stack_in, stack_out):
    """Show queue contents in FIFO order."""
    # out_stack holds front (but reversed), so reverse it + add in_stack
    items = list(reversed(stack_out)) + stack_in
    print(f"Queue (front -> back): {items}")


def main():
    raw = input("Enter queue elements (space-separated): ").strip()
    if raw == "":
        print("No input provided.")
        return

    stack_in = []    # stack for enqueue operations (push here)
    stack_out = []   # stack for dequeue operations (pop here after transfer)

    for val in raw.split():
        # add each input value into the queue
        enqueue(stack_in, val)

    # show initial queue state
    print_queue(stack_in, stack_out)

    # ask how many elements to remove
    k_raw = input("How many dequeues? ").strip()
    if k_raw == "":
        # avoid empty input
        print("No dequeue count provided.")
        return

    # convert request to integer count
    k = int(k_raw)

    for _ in range(k):
        # remove one element FIFO-style
        removed = dequeue(stack_in, stack_out)
        if removed is None:    # queue became empty
            print("Queue empty. Stopping.")
            break

        # show which element was removed
        print(f"Dequeued: {removed}")
        # show queue after removal
        print_queue(stack_in, stack_out)


if __name__ == "__main__":
    main()
