from __future__ import annotations

import os
import random

from .objects.book import ProgrammingBook

class ProgrammingBooks():
    def __init__(self):
        self.folder_name = "Anime-Girls-Holding-Programming-Books"
        self.path_to_folder = f"./files/{self.folder_name}"

    def random_language(self) -> str:
        language_list = os.listdir(self.path_to_folder)
        language = language_list[random.randint(0, len(language_list) - 1)]

        if language in [".git", "CONTRIBUTING.md", "README.md"]:
            return "Python"
        else:
            return language

    def random_book(self, language:str) -> ProgrammingBook|None:
        """Returns random book from a specific language."""
        for actual_language in os.listdir(f"{self.path_to_folder}/"):
            if language.upper() == actual_language.upper():
                actual_pictures_list = os.listdir(f"{self.path_to_folder}/{actual_language}/")

                picture_name = actual_pictures_list[random.randint(0, len(actual_pictures_list) - 1)]

                return ProgrammingBook(
                    file_name=picture_name,
                    file_path=f"{self.folder_name}/{actual_language}/{picture_name}",
                    language=actual_language,
                )

            else:
                pass

        return None