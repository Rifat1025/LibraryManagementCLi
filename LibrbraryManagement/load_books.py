import json
def load_books():
    try:
        with open('books.json', "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []