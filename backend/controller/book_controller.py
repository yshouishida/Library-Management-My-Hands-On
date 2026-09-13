from backend.services.book_service import get_books_service
from backend.utils.api_response import error, success

def get_books_control():
    books = get_books_service()

    if books is None:
        return error("Books are not found.", 404)

    return success("Get successfully", 200, books)

