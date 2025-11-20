class Book:
    """Represents a single book in the library catalog."""

    def __init__(self, title, author, isbn, status="available"):
        """Initializes a new Book object with title, author, isbn, and status."""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status  # 'available' or 'issued' [cite: 16]

    def __str__(self):
        """Returns a user-friendly string representation."""
        return f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | Status: {self.status.capitalize()}"

    def to_dict(self):
        """Returns a dictionary representation for JSON serialization."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def issue(self):
        """Sets the book's status to 'issued' if available[cite: 18]."""
        if self.is_available():
            self.status = "issued"
            return True
        return False

    def return_book(self):
        """Sets the book's status to 'available'[cite: 18]."""
        self.status = "available"

    def is_available(self):
        """Checks if the book is currently available[cite: 18]."""
        return self.status == "available"