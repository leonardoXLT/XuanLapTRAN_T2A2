from init import db, ma
from marshmallow import fields

class Staff(db.Model):
    __tablename__ = 'staff'
    staff_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class StaffSchema(ma.Schema):
    class Meta:
        fields = ('staff_id', 'name', 'email', 'password')

staff_schema = StaffSchema()
staffs_schema = StaffSchema(many=True)

