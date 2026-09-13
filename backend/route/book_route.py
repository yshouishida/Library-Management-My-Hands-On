from flask import Blueprint
from backend.controller.book_controller import get_books_control

book_bp = Blueprint("books", __name__)

@book_bp.route("/api/books", methods=["GET"])
def get_books():
    return get_books_control()