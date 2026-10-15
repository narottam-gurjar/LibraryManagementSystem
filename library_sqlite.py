
import sqlite3

def connect_db():
    connection = sqlite3.connect("library_app.db")
    return connection

def create_table():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            author TEXT NOT NULL,
            available INTEGER NOT NULL DEFAULT 1
        )
    """)

    connection.commit()
    connection.close()


def add_book(title, author):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO books (title, author) VALUES (?, ?)",
            (title, author)
        )
        connection.commit()
        print("Book added successfully!")

    except sqlite3.IntegrityError:
        print("A book with this title already exists.")

    finally:
        connection.close()


def show_books():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    if not books:
        print("No books in the library.")
    else:
        for book in books:
            status = "Available" if book[3] == 1 else "Borrowed"

            print(
                f"ID: {book[0]} | "
                f"Title: {book[1]} | "
                f"Author: {book[2]} | "
                f"Status: {status}"
            )

    connection.close()


def count_books():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM books")
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM books WHERE available = 1"
    )
    available = cursor.fetchone()[0]

    print("Total books:", total)
    print("Available books:", available)
    print("Borrowed books:", total - available)

    connection.close()


def search_book(title):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM books WHERE title = ?",
        (title,)
    )

    book = cursor.fetchone()

    if book:
        status = "Available" if book[3] == 1 else "Borrowed"
        print(f"Title: {book[1]}")
        print(f"Author: {book[2]}")
        print(f"Status: {status}")
    else:
        print("Book not found.")

    connection.close()


def search_by_author(author):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT title, author FROM books WHERE author = ?",
        (author,)
    )

    books = cursor.fetchall()

    if books:
        for book in books:
            print(f"Title: {book[0]} | Author: {book[1]}")
    else:
        print("No books found for this author.")

    connection.close()


def borrow_book(title):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT available FROM books WHERE title = ?",
        (title,)
    )

    book = cursor.fetchone()

    if book is None:
        print("Book not found.")
    elif book[0] == 0:
        print("Book is already borrowed.")
    else:
        cursor.execute(
            "UPDATE books SET available = 0 WHERE title = ?",
            (title,)
        )
        connection.commit()
        print("Book borrowed successfully!")

    connection.close()


def return_book(title):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT available FROM books WHERE title = ?",
        (title,)
    )

    book = cursor.fetchone()

    if book is None:
        print("Book not found.")
    elif book[0] == 1:
        print("Book is already available.")
    else:
        cursor.execute(
            "UPDATE books SET available = 1 WHERE title = ?",
            (title,)
        )
        connection.commit()
        print("Book returned successfully!")

    connection.close()


def remove_book(title):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM books WHERE title = ?",
        (title,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Book removed successfully!")
    else:
        print("Book not found.")

    connection.close()


def menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. Show all books")
        print("2. Add a book")
        print("3. Search by title")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Remove a book")
        print("7. Search by author")
        print("8. Count books")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_books()

        elif choice == "2":
            title = input("Enter book title: ").strip()
            author = input("Enter author: ").strip()

            if title and author:
                add_book(title, author)
            else:
                print("Title and author cannot be empty.")

        elif choice == "3":
            title = input("Enter book title to search: ").strip()

            if title:
                search_book(title)
            else:
                print("Title cannot be empty.")

        elif choice == "4":
            title = input("Enter book title to borrow: ").strip()

            if title:
                borrow_book(title)
            else:
                print("Title cannot be empty.")

        elif choice == "5":
            title = input("Enter book title to return: ").strip()

            if title:
                return_book(title)
            else:
                print("Title cannot be empty.")

        
        elif choice == "6":
            title = input("Enter book title to remove: ").strip()

            if title:
                remove_book(title)
            else:
                print("Title cannot be empty.")
      
        elif choice == "7":
            author = input("Enter author name: ").strip()

            if author:
                search_by_author(author)
            else:
                print("Author name cannot be empty.")

        elif choice == "8":
            count_books()

        elif choice == "9":
            print("Exiting Library Management System...")
            break

        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid choice. Please enter 1-9.")
            continue


create_table()

menu()