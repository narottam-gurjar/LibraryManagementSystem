import json

class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            return "Book borrowed successfully"
        return "Book is not available"

    def return_book(self):
        if not self.available:
            self.available = True
            return "Book returned successfully"
        return "Book is already available"

    def display(self):
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Available: {self.available}"
        )


def find_book(books, title):
    for book in books:
        if title.lower() == book.title.lower():
            return book
    return None


def borrow_book(books, title):
    result = find_book(books, title)

    if result is not None:
        return result.borrow()
    return "Book not found"


def return_book_by_title(books, title):
    result = find_book(books, title)

    if result is not None:
        return result.return_book()
    return "Book not found"


class Library:
    def __init__(self, books):
        self.books = books

    def show_books(self):
        if not self.books:
            print("No books in the library.")
            return

        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.title}: {book.author} | {status}")

    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.title.lower() == book.title.lower():
                return "Book already exists"

        self.books.append(book)
        return "Book added successfully"

    def remove_book(self, title):
        book = find_book(self.books, title)

        if book is not None:
            self.books.remove(book)
            return "Book removed successfully"
        return "Book doesn't exist"

    def available_books(self):
        found = False

        for book in self.books:
            if book.available:
                print(book.title)
                found = True

        if not found:
            print("No books available")

    def search_by_author(self, author):
        found = False

        for book in self.books:
            if book.author.lower() == author.lower():
                print(book.title)
                found = True

        if not found:
            print("No books found for this author")

    def search_by_title(self, title):
        book = find_book(self.books, title)

        if book is not None:
            print(book.author)
        else:
            print("Book not found")

    def total_books(self):
        return len(self.books)

    def count_available_books(self):
        count = 0

        for book in self.books:
            if book.available:
                count += 1

        return count

def save_books(library):
    book_data = []

    for books in library.books:
        book_data.append({
            "title": books.title,
            "author": books.author,
            "available": books.available
        })

    with open("books.json","w") as file:
        json.dump(book_data, file, indent=4)

    print("Books saved successfully!")

def load_books():
    try:
        with open("books.json", "r") as file:
            book_data = json.load(file)

        books = []

        for data in book_data:
            if not all(key in data for key in ["title", "author", "available"]):
                print("Warning: A book is missing a required information!")
                continue
            book = Book(data["title"], data["author"], data["available"])
            books.append(book)

        return books

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning: books.json is empty or corrupted")
        return []

books = load_books()
library = Library(books)

while True:
    print("\n------ Library Management System ------")
    print("1. Show all books")
    print("2. Add a book")
    print("3. Remove a book")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Search by title")
    print("7. Search by author")
    print("8. Count books")
    print("9. Exit")

    choice = input("Enter a choice: ").strip()

    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Invalid choice. Please enter 1-9.")
        continue

    elif choice == "1":
        library.show_books()

    elif choice == "2":
        title = input("Enter book title: ").strip()
        author = input("Enter author: ").strip()

        if not title or not author:
            print("Title and author can't be empty.")
            continue

        book = Book(title, author, True)
        message = library.add_book(book)
        print(message)

        if message == "Book added successfully":
            save_books(library)

    elif choice == "3":
        title = input("Enter book title to remove: ").strip()

        if not title:
            print("Book title can't be empty.")
            continue

        message = library.remove_book(title)
        print(message)

        if message == "Book removed successfully":
            save_books(library)

    elif choice == "4":
        title = input("Enter book title to borrow: ").strip()

        if not title:
            print("Book title can't be empty.")
            continue

        message = borrow_book(library.books, title)
        print(message)

        if message == "Book borrowed successfully":
            save_books(library)

    elif choice == "5":
        title = input("Enter book title to return: ").strip()

        if not title:
            print("Book title can't be empty.")
            continue

        message = return_book_by_title(library.books, title)
        print(message)

        if message == "Book returned successfully":
            save_books(library)

    elif choice == "6":
        title = input("Enter book title to search: ").strip()

        if not title:
            print("Search title can't be empty.")
            continue

        library.search_by_title(title)

    elif choice == "7":
        author = input("Enter author to search: ").strip()

        if not author:
            print("Author name can't be empty.")
            continue

        library.search_by_author(author)

    elif choice == "8":
        print("Total books:", library.total_books())
        print("Available books:", library.count_available_books())

    elif choice == "9":
        print("Exiting Library Management System...")
        break