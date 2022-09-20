from . import app, programing_books, API_PATH

from flask import send_from_directory, request, abort

ProgrammingBooks = programing_books.ProgrammingBooks()

@app.get(API_PATH + "/language/<language>")
def language(language:str):
    """Returns random book from language."""

    book = ProgrammingBooks.random_book(language.lower())

    if book == None:
        abort(404, "Language Not Found!")

    return send_from_directory("../files", f"{book.file_path}")