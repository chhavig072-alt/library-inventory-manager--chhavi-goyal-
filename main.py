# CORRECTED: Importing from the package structure
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
    """Provides the interactive CLI menu[cite: 28]."""
    inventory = LibraryInventory()
    logger.info("Application started.")

    while True:
        print("\n--- Library Inventory Manager ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit") # [cite: 29]

        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == '1':
                add_book_cli(inventory)
            elif choice == '2':
                issue_book_cli(inventory)
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
            # Catch critical errors in the main loop [cite: 32]
            print(f"A critical error occurred. Error: {e}")
            logger.critical(f"Unhandled exception in main loop: {e}", exc_info=True)


def add_book_cli(inventory):
    """Handles the user input for adding a book with validation[cite: 30]."""
    print("\n--- Add New Book ---")
    try:
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        isbn = input("ISBN (unique identifier): ").strip()

        if not all([title, author, isbn]) or not isbn.isdigit():
            print("Error: All fields are required, and ISBN must be numeric.")
            logger.warning("Failed to add book due to invalid input.")
            return

        new_book = Book(title, author, isbn)
        inventory.add_book(new_book)
    except Exception as e:
        print(f"Input error: {e}")
        logger.error(f"Error during add_book_cli input: {e}")

# (issue_book_cli, return_book_cli, and search_book_cli functions are similar
# to the simple code provided before, ensuring they call the inventory methods.)

if __name__ == "__main__":
    # Crucial step: The package must be run as a module for imports to work.
    main_menu()