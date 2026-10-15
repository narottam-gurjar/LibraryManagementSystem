# Library Management System

A command-line Library Management System built with Python. It supports book management, borrowing and returning books, and persistent storage.

## Features

- Add and remove books
- Display all books
- Search by title or author
- Borrow and return books
- Count total, available, and borrowed books
- Prevent duplicate book titles
- Store book records persistently

## Technologies Used

- Python
- SQLite (`sqlite3`)
- JSON
- Git and GitHub

## Project Files

- `main.py` — Original JSON-based implementation
- `books.json` — JSON book data
- `database.py` — SQLite database setup and practice
- `library_sqlite.py` — SQLite-based Library Management System
- `library_app.db` — SQLite database created when the SQLite application runs

## How to Run

Make sure Python 3 is installed.

Run the original JSON version:

```bash
python main.py
```

Run the SQLite version:

```bash
python library_sqlite.py
```

## What I Learned

- Python functions, classes, and objects
- File handling and JSON
- SQL CRUD operations
- SQLite database connections
- Input validation and error handling
- Git version control and GitHub

## Future Improvements

- Add book IDs to search and remove books
- Add library member accounts
- Introduce book due dates
- Add automated tests
- Build a graphical user interface

## Author

Narottam Singh Gurjar

GitHub: [@narottam-gurjar](https://github.com/narottam-gurjar)