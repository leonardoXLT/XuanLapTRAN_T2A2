from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.borrowing_record import BorrowingRecord, borrowing_record_schema, borrowing_records_schema
from models.book import Book
from models.member import Member

borrowing_record_bp = Blueprint('borrowing_records', __name__, url_prefix='/borrowing-records')

@borrowing_record_bp.route('/', methods=['GET'])
def get_all_borrowing_records():
    borrowing_records = db.session.scalars(db.select(BorrowingRecord))
    return borrowing_records_schema.dump(borrowing_records)

@borrowing_record_bp.route('/<int:record_id>', methods=['GET'])
def get_one_borrowing_record(record_id):
    borrowing_record = db.session.scalar(db.select(BorrowingRecord).filter_by(record_id=record_id))
    if borrowing_record:
        return borrowing_record_schema.dump(borrowing_record)
    else:
        return {"error": f"Borrowing record with id {record_id} not found"}, 404

@borrowing_record_bp.route('/', methods=['POST'])
@jwt_required()
def create_borrowing_record():
    body_data = borrowing_record_schema.load(request.get_json())

    # Get the book and member from the request data
    book_id = body_data.get('book_id')
    member_id = body_data.get('member_id')
    book = db.session.scalar(db.select(Book).filter_by(book_id=book_id))
    member = db.session.scalar(db.select(Member).filter_by(member_id=member_id))

    # Create a new borrowing record instance
    borrowing_record = BorrowingRecord(
        book=book,
        member=member,
        borrowed_on=body_data.get('borrowed_on'),
        return_date=body_data.get('return_date'),
        fine_amount=body_data.get('fine_amount')
    )

    # Add the borrowing record to the session and commit
    db.session.add(borrowing_record)
    db.session.commit()

    return borrowing_record_schema.dump(borrowing_record), 201

@borrowing_record_bp.route('/<int:record_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_borrowing_record(record_id):
    # Get the borrowing record to be updated
    borrowing_record = db.session.scalar(db.select(BorrowingRecord).filter_by(record_id=record_id))

    if borrowing_record:
        # Update the borrowing record with the new data
        body_data = borrowing_record_schema.load(request.get_json(), partial=True)
        borrowing_record.book_id = body_data.get('book_id') or borrowing_record.book_id
        borrowing_record.member_id = body_data.get('member_id') or borrowing_record.member_id
        borrowing_record.borrowed_on = body_data.get('borrowed_on') or borrowing_record.borrowed_on
        borrowing_record.return_date = body_data.get('return_date') or borrowing_record.return_date
        borrowing_record.fine_amount = body_data.get('fine_amount') or borrowing_record.fine_amount

        # Commit the changes
        db.session.commit()

        return borrowing_record_schema.dump(borrowing_record)
    else:
        return {"error": f"Borrowing record with id {record_id} not found"}, 404

@borrowing_record_bp.route('/<int:record_id>', methods=['DELETE'])
@jwt_required()
def delete_borrowing_record(record_id):
    # Get the borrowing record to be deleted
    borrowing_record = db.session.scalar(db.select(BorrowingRecord).filter_by(record_id=record_id))

    if borrowing_record:
        # Delete the borrowing record from the session and commit
        db.session.delete(borrowing_record)
        db.session.commit()
        return {'message': f"Borrowing record with id {record_id} deleted successfully"}
    else:
        return {'error': f"Borrowing record with id {record_id} not found"}, 404
