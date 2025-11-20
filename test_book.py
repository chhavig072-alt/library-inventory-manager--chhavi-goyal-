import pytest
from library_manager.book import Book

def test_book_initialization():
    book = Book("Title", "Author", "123")
    assert book.title == "Title"
    assert book.author == "Author"
    assert book.isbn == "123"
    assert book.status == "available"

def test_issue_book_when_available():
    book = Book("Test", "Writer", "999")
    assert book.issue() is True
    assert book.status == "issued"

def test_issue_book_when_already_issued():
    book = Book("ABC", "PQR", "555", status="issued")
    assert book.issue() is False
    assert book.status == "issued"

def test_return_book():
    book = Book("ABC", "PQR", "555", status="issued")
    book.return_book()
    assert book.status == "available"

def test_to_dict():
    book = Book("XYZ", "Author", "777")
    d = book.to_dict()
    assert d["title"] == "XYZ"
    assert d["author"] == "Author"
    assert d["isbn"] == "777"
    assert d["status"] == "available"
