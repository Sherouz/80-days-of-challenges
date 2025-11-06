# Challenge #26 - Beginner
# Sort library by number of pages
# Objective: Practice using sorted(), lambda functions, and key-based sorting

"""
Sort a list of books by their page count in ascending order.
Each item in the list is a tuple: (book_name, page_count).
Demonstrates lambda usage with the sorted() function.
"""

def sort_library_by_pages(library_list):
    """
    Return a list of books sorted by their number of pages (ascending).
    """
    # Use the sorted() function with a key to specify sorting by page count
    # key=lambda book: book[1] tells Python to sort each tuple by its 2nd element (page count)
    sorted_list = sorted(library_list, key=lambda book: book[1])
    return sorted_list


# Example usage:
books = [
    ("The Hitchhiker's Guide", 42),
    ("Pride and Prejudice", 279),
    ("Moby Dick", 378),
    ("1984", 328)
]

sorted_books = sort_library_by_pages(books)
print("--- Sorted book list ---")
for book, pages in sorted_books:
    print(f"- {book}: {pages} pages")
