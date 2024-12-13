import save_books

def update_books(books):
    isbn = int(input("\nEnter the ISBN of the book to update: "))
    for book in books:
        if book["isbn"] == isbn:
            print(f"Updating book: {book['title']} by {book['author']}")
            book['title'] = input("New Title (leave blank to keep current): ").strip() or book['title']
            book['author'] = input("New Author (leave blank to keep current): ").strip() or book['author']
            quantity = input("New Quantity (leave blank to keep current): ").strip()
            if quantity.isdigit():
                book['quantity'] = int(quantity)
            elif quantity:
                print("Invalid input for quantity. Keeping current value.")
            save_books.save_book(books)
            print("Book updated successfully!")
            return
    print("No book found with the given ISBN.")
