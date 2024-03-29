from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.staff import Staff, staff_schema, staffs_schema
from models.borrowing_record import BorrowingRecord
from models.book import Book

staff_bp = Blueprint('staff', __name__, url_prefix='/staff')

@staff_bp.route('/', methods=['GET'])
def get_all_staff():
    staff = db.session.scalars(db.select(Staff))
    return staffs_schema.dump(staff)

@staff_bp.route('/<int:staff_id>', methods=['GET'])
def get_one_staff(staff_id):
    staff = db.session.scalar(db.select(Staff).filter_by(staff_id=staff_id))
    if staff:
        return staff_schema.dump(staff)
    else:
        return {"error": f"Staff with id {staff_id} not found"}, 404

@staff_bp.route('/', methods=['POST'])
@jwt_required()
def create_staff():
    body_data = staff_schema.load(request.get_json())

    # Create a new staff instance
    staff = Staff(
        name=body_data.get('name'),
        email=body_data.get('email'),
        password=bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8')
    )

    # Add the staff to the session and commit
    db.session.add(staff)
    db.session.commit()

    return staff_schema.dump(staff), 201

@staff_bp.route('/<int:staff_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_staff(staff_id):
    # Get the staff to be updated
    staff = db.session.scalar(db.select(Staff).filter_by(staff_id=staff_id))

    if staff:
        # Update the staff with the new data
        body_data = staff_schema.load(request.get_json(), partial=True)
        staff.name = body_data.get('name') or staff.name
        staff.email = body_data.get('email') or staff.email
        staff.password = bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8') or staff.password

        # Commit the changes
        db.session.commit()

        return staff_schema.dump(staff)
    else:
        return {"error": f"Staff with id {staff_id} not found"}, 404

@staff_bp.route('/<int:staff_id>', methods=['DELETE'])
@jwt_required()
def delete_staff(staff_id):
    # Get the staff to be deleted
    staff = db.session.scalar(db.select(Staff).filter_by(staff_id=staff_id))

    if staff:
        # Delete the staff from the session and commit
        db.session.delete(staff)
        db.session.commit()
        return {'message': f"Staff '{staff.name}' deleted successfully"}
    else:
        return {'error': f"Staff with id {staff_id} not found"}, 404

@staff_bp.route('/update-book-status/<int:book_id>', methods=['PUT'])
@jwt_required()
def update_book_status(book_id):
    # Get the book to be updated
    book = db.session.scalar(db.select(Book).filter_by(book_id=book_id))

    if book:
        # Update the book status
        new_status = request.get_json().get('status')
        book.status = new_status
        db.session.commit()
        return {'message': f"Book '{book.title}' status updated to '{new_status}'"}
    else:
        return {'error': f"Book with id {book_id} not found"}, 404

@staff_bp.route('/manage-borrowing-records/<int:record_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def manage_borrowing_record(record_id):
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
