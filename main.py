# Corrected: Importing from the package structure
from library_manager.book import Book
from library_manager.inventory import LibraryInventory 
import logging

# Use the same logger setup for the CLI entry point
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='library_manager.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

def main_menu():
    [cite_start]"""Provides the main menu logic for the CLI. [cite: 28]"""
    inventory = LibraryInventory()
    logger.info("Application started.")

    while True:
        # [cite_start]Menu: Add Book, Issue Book, Return Book, View All, Search, Exit [cite: 29]
        print("\n--- Library Inventory Manager ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == '1':
                add_book_cli(inventory)
            elif choice == '2':
                issue_book_cli(inventory) # Fixes the NameError from the previous step!
            elif choice == '3':
                return_book_cli(inventory)
            elif choice == '4':
                print("\n--- Current Catalog ---")
                inventory.display_all()
            elif choice == '5':
                search_book_cli(inventory)
            elif choice == '6':
                print("Exiting Library Manager. Goodbye!")
                logger.info("Application closed normally.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                logger.warning(f"Invalid menu input received: {choice}")
        except Exception as e:
            # [cite_start]Catch critical errors in the main loop [cite: 32]
            print(f"A critical error occurred. Error: {e}")
            logger.critical(f"Unhandled exception in main loop: {e}", exc_info=True)


def add_book_cli(inventory):
    [cite_start]"""Handles user input for adding a book with validation. [cite: 30]"""
    print("\n--- Add New Book ---")
    try:
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        isbn = input("ISBN (unique identifier): ").strip()

        # [cite_start]Ensure input validation. [cite: 30]
        if not all([title, author, isbn]) or not isbn.isdigit():
            print("Error: All fields are required, and ISBN must be numeric.")
            logger.warning("Failed to add book due to invalid input.")
            return

        new_book = Book(title, author, isbn)
        inventory.add_book(new_book)
    except Exception as e:
        print(f"Input error: {e}")
        logger.error(f"Error during add_book_cli input: {e}")

def issue_book_cli(inventory):
    """Handles the user input for issuing a book."""
    print("\n--- Issue Book ---")
    isbn = input("Enter ISBN of the book to issue: ").strip()
    inventory.issue_book(isbn)

def return_book_cli(inventory):
    """Handles the user input for returning a book."""
    print("\n--- Return Book ---")
    isbn = input("Enter ISBN of the book to return: ").strip()
    inventory.return_book_by_isbn(isbn)

def search_book_cli(inventory):
    [cite_start]"""Handles the user input for searching books. [cite: 30]"""
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
            print(result)
        else:
            print("No book found with that ISBN.")
    else:
        print("Invalid search choice.")


if __name__ == "__main__":
    # Execution entry point
    main_menu()
