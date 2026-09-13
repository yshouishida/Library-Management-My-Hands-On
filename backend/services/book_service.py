from backend.repositories.book_repository import (
    get_books_repo,
    get_by_id_repo
)

def get_books_service():
    books = get_books_repo()

    if not books:
        return None

    return books

def get_by_id_service():
    book = get_by_id_repo()

    if not book:
        return None

    return book



