from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.book import Book, book_schema, books_schema
from models.category import Category

book_bp = Blueprint('books', __name__, url_prefix='/books')

@book_bp.route('/', methods=['GET'])
def get_all_books():
    books = db.session.scalars(db.select(Book))
    return books_schema.dump(books)

@book_bp.route('/<int:book_id>', methods=['GET'])
def get_one_book(book_id):
    book = db.session.scalar(db.select(Book).filter_by(book_id=book_id))
    if book:
        return book_schema.dump(book)
    else:
        return {"error": f"Book with id {book_id} not found"}, 404

@book_bp.route('/', methods=['POST'])
@jwt_required()
def create_book():
    body_data = book_schema.load(request.get_json())

    # Get the category from the request data
    category_id = body_data.get('category_id')
    category = db.session.scalar(db.select(Category).filter_by(category_id=category_id))

    # Create a new book instance
    book = Book(
        title=body_data.get('title'),
        author=body_data.get('author'),
        category=category,
        shelf_location=body_data.get('shelf_location'),
        status=body_data.get('status')
    )

    # Add the book to the session and commit
    db.session.add(book)
    db.session.commit()

    return book_schema.dump(book), 201

@book_bp.route('/<int:book_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_book(book_id):
    # Get the book to be updated
    book = db.session.scalar(db.select(Book).filter_by(book_id=book_id))

    if book:
        # Update the book with the new data
        body_data = book_schema.load(request.get_json(), partial=True)
        book.title = body_data.get('title') or book.title
        book.author = body_data.get('author') or book.author
        book.category_id = body_data.get('category_id') or book.category_id
        book.shelf_location = body_data.get('shelf_location') or book.shelf_location
        book.status = body_data.get('status') or book.status

        # Commit the changes
        db.session.commit()

        return book_schema.dump(book)
    else:
        return {"error": f"Book with id {book_id} not found"}, 404

@book_bp.route('/<int:book_id>', methods=['DELETE'])
@jwt_required()
def delete_book(book_id):
    # Get the book to be deleted
    book = db.session.scalar(db.select(Book).filter_by(book_id=book_id))

    if book:
        # Delete the book from the session and commit
        db.session.delete(book)
        db.session.commit()
        return {'message': f"Book '{book.title}' deleted successfully"}
    else:
        return {'error': f"Book with id {book_id} not found"}, 404