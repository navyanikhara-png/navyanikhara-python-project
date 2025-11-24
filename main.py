library=[]
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    library.append({"title": title, "author": author, "status": "Available"})
    print("Book added successfully!\n")

def view_books():
    if not library:
        print("No books in library.\n")
        return
    print("\n--- Library Books ---")
    for i, book in enumerate(library, start=1):
        print(f"{i}. {book['title']} by {book['author']} - {book['status']}")
    print()

def search_book():
    name = input("Enter book title to search: ")
    for book in library:
        if book['title'].lower() == name.lower():
            print(f"Book Found: {book['title']} by {book['author']} - {book['status']}\n")
            return
    print("Book not found.\n")

def issue_book():
    name = input("Enter book title to issue: ")
    for book in library:
        if book['title'].lower() == name.lower():
            if book['status'] == "Available":
                book['status'] = "Issued"
                print("Book issued successfully!\n")
            else:
                print("Book already issued.\n")
            return
    print("Book not found.\n")

def return_book():
    name = input("Enter book title to return: ")
    for book in library:
        if book['title'].lower() == name.lower():
            if book['status'] == "Issued":
                book['status'] = "Available"
                print("Book returned successfully!\n")
            else:
                print("Book was not issued.\n")
            return
    print("Book not found.\n")

while True:
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid option. Try again.\n")
