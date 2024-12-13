import random
from datetime import datetime
import save_books

def add_books(books):
    print("\nAdd a New Book:")
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    quantity = input("Quantity: ").strip()

    if not quantity.isdigit():
        print("Error: Quantity must be a valid number.")
        return

    isbn =random.randint(1000000000, 9999999999)
    added_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "quantity": int(quantity),
        "added_at": added_at
    }
    books.append(new_book)
    save_books.save_book(books)
    print(f"Book added successfully with ISBN: {isbn}")