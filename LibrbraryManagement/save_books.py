import json
def save_book(books):
    with open('books.json', "w") as file:
        json.dump(books, file, indent=4)