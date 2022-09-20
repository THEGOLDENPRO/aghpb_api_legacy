import os
from . import app, programing_books, API_PATH

from flask import jsonify

ProgrammingBooks = programing_books.ProgrammingBooks()

@app.get(API_PATH + "/languages")
def languages():
    """Returns list of languages."""
    language_list = os.listdir(ProgrammingBooks.path_to_folder)
    language_list.remove(".git"); language_list.remove("CONTRIBUTING.md"); language_list.remove("README.md")

    return jsonify(language_list)