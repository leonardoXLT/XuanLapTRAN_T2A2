from datetime import date
import functools

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.book import Book, books_schema, book_schema
# Import other models as needed

books_bp = Blueprint('books', __name__, url_prefix='/books')

@books_bp.route('/', methods=["GET"])
def get_all_books():
    books = Book.query.all()
    return books_schema.dump(books)

@books_bp.route('/<int:book_id>', methods=["GET"])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return book_schema.dump(book)
    else:
        return {"error": "Book not found"}, 404

# Implement POST, PUT, DELETE methods as needed
