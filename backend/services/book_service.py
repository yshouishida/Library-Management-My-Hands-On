from backend.repositories.book_repository import (
    get_books_repo,
    get_by_id_repo,
    add_book_repo,
    update_book_repo,
    delete_book_repo
)

def get_books_service():
    books = get_books_repo()

    if not books:
        return None

    return books

def get_by_id_service(id):
    book = get_by_id_repo(id)


    if not book:
        return None

    return book


def add_book_service(title, author, year_published, genre):
    result = add_book_repo(title, author, year_published, genre)

    if not result:
        return None

    return result

def update_book_service(title, author, year_published, genre, id):
    result = update_book_repo(title, author, year_published, genre, id)

    if not result:
        return None

    return result

def delete_book_service(id):
    result = delete_book_repo(id)

    if not result:
        return None

    return result

