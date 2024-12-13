def view_book(books):
    print("\nAll Books:")
    if not books:
        print("No books available.")
        return
    print("{:<30} {:<20} {:<15} {:<10} {:<20}".format("Title", "Author", "ISBN", "Quantity", "Added At"))
    print("-" * 100)
    for book in books:
        print("{:<30} {:<20} {:<15} {:<10} {:<20}".format(book['title'], book['author'], book['isbn'], book['quantity'], book['added_at']))
