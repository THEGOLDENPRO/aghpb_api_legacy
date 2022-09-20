from . import app, programing_books, API_PATH

from flask import send_from_directory

ProgrammingBooks = programing_books.ProgrammingBooks()

@app.get(API_PATH + "/random")
def random():
    """Returns completely random book."""
    book = ProgrammingBooks.random_book(ProgrammingBooks.random_language())

    return send_from_directory("../files", f"{book.file_path}")