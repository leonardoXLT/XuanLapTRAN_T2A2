from init import db, ma
from marshmallow import fields

class Book(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    shelf_location = db.Column(db.String(255))
    status = db.Column(db.String(50), default='available')

    # Relationship with Category
    category = db.relationship('Category', back_populates='books')

class BookSchema(ma.Schema):
    class Meta:
        fields = ('book_id', 'title', 'author', 'category_id', 'shelf_location', 'status')

book_schema = BookSchema()
books_schema = BookSchema(many=True)
