def return_book_cli(inventory):
    """Handles the user input for returning a book."""
    print("\n--- Return Book ---")
    isbn = input("Enter ISBN of the book to return: ").strip()
    inventory.return_book_by_isbn(isbn)


def search_book_cli(inventory):
    """Handles the user input for searching books."""
    print("\n--- Search Book ---")
    print("1. Search by Title (partial match)")
    print("2. Search by ISBN (exact match)")
    
    search_choice = input("Enter search type (1 or 2): ").strip()

    if search_choice == '1':
        query = input("Enter title keyword: ").strip()
        results = inventory.search_by_title(query)
        print("\n--- Search Results (Title) ---")
        if results:
            for i, book in enumerate(results, 1):
                print(f"{i}. {book}")
        else:
            print("No books found matching the title keyword.")

    elif search_choice == '2':
        query = input("Enter ISBN: ").strip()
        result = inventory.search_by_isbn(query)
        print("\n--- Search Result (ISBN) ---")
        if result:

