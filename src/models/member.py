from init import db, ma
from marshmallow import fields

class Member(db.Model):
    __tablename__ = 'members'
    member_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class MemberSchema(ma.Schema):
    class Meta:
        fields = ('member_id', 'first_name', 'last_name', 'email', 'password')

member_schema = MemberSchema()
members_schema = MemberSchema(many=True)

