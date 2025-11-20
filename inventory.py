import json
import logging
from pathlib import Path
from .book import Book # CORRECTED: Relative import within the package

# --- Task 5: Logging Configuration ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='library_manager.log',
    filemode='a'
)
logger = logging.getLogger(__name__)
# -----------------------------------

CATALOG_FILE = Path("library_catalog.json")

class LibraryInventory:
    """Manages the collection of Book objects and handles file persistence[cite: 20]."""

    def __init__(self):
        self.books = []  # Maintain a list of Book objects [cite: 21]
        self._load_catalog()

    def _load_catalog(self):
        """Loads book data from the JSON file, handling exceptions[cite: 24, 26, 32]."""
        try:
            if CATALOG_FILE.exists():
                with CATALOG_FILE.open('r') as f:
                    data = json.load(f)
                    # Recreate Book objects from dictionary data
                    self.books = [Book(**item) for item in data]
                logger.info(f"Catalog loaded successfully. {len(self.books)} books found.")
            else:
                logger.info("Catalog file not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print("Error: Catalog file is corrupted. Starting with an empty inventory.")
            logger.error("JSONDecodeError: Catalog file is corrupted.", exc_info=True)
        except Exception as e:
            print(f"An unexpected error occurred during loading: {e}")
            logger.critical(f"Critical error during loading: {e}", exc_info=True)
        finally:
            # Ensures code inside finally runs regardless of errors
            pass 

    def _save_catalog(self):
        """Saves the current book data to the JSON file[cite: 24]."""
        try:
            data = [book.to_dict() for book in self.books]
            with CATALOG_FILE.open('w') as f:
                json.dump(data, f, indent=4)
            logger.info("Catalog saved successfully.")
        except Exception as e:
            print(f"Error saving catalog: {e}")
            logger.error(f"Error saving catalog: {e}", exc_info=True)

    def add_book(self, book):
        """Adds a new Book object[cite: 22]."""
        if any(b.isbn == book.isbn for b in self.books):
            print(f"Error: Book with ISBN {book.isbn} already exists.")
            logger.warning(f"Attempted to add duplicate ISBN: {book.isbn}")
            return
        self.books.append(book)
        self._save_catalog()
        logger.info(f"Book added: {book.title}")
        print(f"Book '{book.title}' added.")

    def search_by_title(self, title_query):
        """Searches books by title[cite: 22]."""
        return [book for book in self.books if title_query.lower() in book.title.lower()]

    def search_by_isbn(self, isbn_query):
        """Searches for a book by its exact ISBN[cite: 22]."""
        return next((book for book in self.books if book.isbn == isbn_query), None)

    def display_all(self):
        """Prints the details of all books[cite: 22]."""
        if not self.books:
            print("The library catalog is empty.")
            return
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

    # The issue_book and return_book_by_isbn methods will interact with the Book methods and call _save_catalog().
    def issue_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book and book.issue():
            self._save_catalog()
            logger.info(f"Book issued: {book.title}")
            print(f"Successfully issued: {book.title}")
            return
        logger.warning(f"Failed to issue book with ISBN: {isbn}")
        print("Error: Book not found or already issued.")

    def return_book_by_isbn(self, isbn):
        book = self.search_by_isbn(isbn)
        if book and book.status == "issued":
            book.return_book()
            self._save_catalog()
            logger.info(f"Book returned: {book.title}")
            print(f"Successfully returned: {book.title}")
            return
        logger.warning(f"Failed to return book with ISBN: {isbn}")
        print("Error: Book not found or was not issued.")