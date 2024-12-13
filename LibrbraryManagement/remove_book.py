import save_books
def remove_books(books):
    isbn = int(input("\nEnter the ISBN of the book to remove: "))
    for book in books:
        if book["isbn"] == isbn:
            confirm = input(f"Are you sure you want to delete '{book['title']}'? (y/n): ").strip().lower()
            if confirm == 'y':
                books.remove(book)
                save_books.save_book(books)
                print(f"Book '{book['title']}' has been removed.")
                return
            else:
                print("Operation canceled.")
                return
    print("No book found with the given ISBN.")
