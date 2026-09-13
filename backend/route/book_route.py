from flask import Blueprint
from backend.controller.book_controller import (
    get_books_control,
    get_by_id_control,
    add_book_control,
    update_book_control,
    delete_book_control
)

book_bp = Blueprint("books", __name__)

@book_bp.route("/api/books", methods=["GET"])
def get_books():
    return get_books_control()


@book_bp.route("/api/books/<int:id>", methods=["GET"])
def get_by_id(id):
    return get_by_id_control(id)


@book_bp.route("/api/books", methods=["POST"])
def add_book():
    return add_book_control()


@book_bp.route("/api/books/<int:id>", methods=["PUT"])
def update_book(id):
    return update_book_control(id)


@book_bp.route("/api/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    return delete_book_control(id)