import add_book
import view_books
import update_book
import remove_book
import save_books
import load_books
books=load_books.load_books()
while True:
        print("\nLibrary Management Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Remove Book")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_book.add_books(books)
        elif choice == "2":
            view_books.view_book(books)
        elif choice == "3":
            update_book.update_books(books)
        elif choice == "4":
            remove_book.remove_books(books)
        elif choice == "5":
            save_books.save_book(books)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")