from init import db, ma
from datetime import datetime
from marshmallow import fields

class BorrowingRecord(db.Model):
    __tablename__ = 'borrowing_records'
    record_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('members.member_id'), nullable=False)
    borrowed_on = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime)
    fine_amount = db.Column(db.Float, default=0.0)

    # Relationships
    book = db.relationship('Book', backref='borrowing_records')
    member = db.relationship('Member', backref='borrowing_records')

class BorrowingRecordSchema(ma.Schema):
    class Meta:
        fields = ('record_id', 'book_id', 'member_id', 'borrowed_on', 'return_date', 'fine_amount')

borrowing_record_schema = BorrowingRecordSchema()
borrowing_records_schema = BorrowingRecordSchema(many=True)
