import json

FILENAME = "library.txt"

# Load library from file
def load_library():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save library to file
def save_library():
    with open(FILENAME, "w") as file:
        json.dump(library, file, indent=4)

library = load_library()

def show_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)
    save_library()
    print("Book added successfully!")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library()
            print("Book removed successfully!")
            return
    print("Book not found.")

def search_book():
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    query = input("Enter the search term: ").lower()
    found_books = []

    for book in library:
        if choice == "1" and query in book["title"].lower():
            found_books.append(book)
        elif choice == "2" and query in book["author"].lower():
            found_books.append(book)

    if found_books:
        print("Matching Books:")
        for i, book in enumerate(found_books, start=1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found.")

def display_books():
    if not library:
        print("Library is empty.")
        return

    print("Your Library:")
    for i, book in enumerate(library, start=1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

def display_statistics():
    total_books = len(library)
    if total_books == 0:
        print("Library is empty.")
        return

    read_books = sum(1 for book in library if book["read"])
    percent_read = (read_books / total_books) * 100
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percent_read:.1f}%")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("Library saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()