from init import db, ma
from marshmallow import fields

class Category(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    # Relationship with Book
    books = db.relationship('Book', back_populates='category', lazy='dynamic')

class CategorySchema(ma.Schema):
    class Meta:
        fields = ('category_id', 'name', 'description')

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

