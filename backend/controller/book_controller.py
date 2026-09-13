from backend.services.book_service import (
    get_books_service,
    get_by_id_service,
    add_book_service,
    update_book_service,
    delete_book_service
)
from backend.utils.api_response import error, success
from flask import request

def get_books_control():
    books = get_books_service()

    if books is None:
        return error("Books are not found.", 404)

    return success(
        "Get successfully", 200, books)


def get_by_id_control(id):
    book = get_by_id_service(id)

    if book is None:
        return error("Book are not found", 404)

    return success("Get successfully", 200, book)

def add_book_control():
    book = request.get_json()

    result = add_book_service(
        book.get("title"),
        book.get("author"),
        book.get("year_published"),
        book.get("genre")
    )

    if result is None:
        return error("Unable to add book", 401)

    return success("Added successfully.", 201, result)

def update_book_control(id):
    book = request.get_json()

    result = update_book_service(
        book.get("title"),
        book.get("author"),
        book.get("year_published"),
        book.get("genre"),
        id)

    if result is None:
        return error("Unable to update book", 401)

    return success("Updated successfully.", 200, result)

def delete_book_control(id):
    result = delete_book_service(id)

    if result is None:
        return error("Unable to delete book", 401)

    return success("Deleted successfully.", 200, result)
