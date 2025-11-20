import pytest
import json
from pathlib import Path
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def setup_function():
    # Clean catalog before every test
    catalog = Path("library_catalog.json")
    if catalog.exists():
        catalog.unlink()

def test_add_book():
    inv = LibraryInventory()
    b1 = Book("Test", "A", "111")

    inv.add_book(b1)
    assert len(inv.books) == 1

def test_add_duplicate_book():
    inv = LibraryInventory()
    b1 = Book("Test", "A", "111")
    b2 = Book("Another", "B", "111")  # same ISBN

    inv.add_book(b1)
    inv.add_book(b2)  # should not add

    assert len(inv.books) == 1

def test_search_by_title():
    inv = LibraryInventory()
    inv.add_book(Book("Python Basics", "A", "101"))
    inv.add_book(Book("Advanced Python", "B", "102"))

    results = inv.search_by_title("Python")
    assert len(results) == 2

def test_search_by_isbn():
    inv = LibraryInventory()
    inv.add_book(Book("Math", "Author", "123"))

    book = inv.search_by_isbn("123")
    assert book is not None
    assert book.title == "Math"

def test_issue_book():
    inv = LibraryInventory()
    inv.add_book(Book("IssueMe", "X", "500"))

    inv.issue_book("500")
    assert inv.search_by_isbn("500").status == "issued"

def test_return_book():
    inv = LibraryInventory()
    book = Book("ReturnMe", "Y", "600", status="issued")
    inv.add_book(book)

    inv.return_book_by_isbn("600")
    assert inv.search_by_isbn("600").status == "available"
