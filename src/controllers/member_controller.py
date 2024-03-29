from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.member import Member, member_schema, members_schema

member_bp = Blueprint('members', __name__, url_prefix='/members')

@member_bp.route('/', methods=['GET'])
def get_all_members():
    members = db.session.scalars(db.select(Member))
    return members_schema.dump(members)

@member_bp.route('/<int:member_id>', methods=['GET'])
def get_one_member(member_id):
    member = db.session.scalar(db.select(Member).filter_by(member_id=member_id))
    if member:
        return member_schema.dump(member)
    else:
        return {"error": f"Member with id {member_id} not found"}, 404

@member_bp.route('/', methods=['POST'])
def create_member():
    body_data = member_schema.load(request.get_json())

    # Create a new member instance
    member = Member(
        first_name=body_data.get('first_name'),
        last_name=body_data.get('last_name'),
        email=body_data.get('email'),
        password=bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8')
    )

    # Add the member to the session and commit
    db.session.add(member)
    db.session.commit()

    return member_schema.dump(member), 201

@member_bp.route('/<int:member_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_member(member_id):
    # Get the member to be updated
    member = db.session.scalar(db.select(Member).filter_by(member_id=member_id))

    if member:
        # Update the member with the new data
        body_data = member_schema.load(request.get_json(), partial=True)
        member.first_name = body_data.get('first_name') or member.first_name
        member.last_name = body_data.get('last_name') or member.last_name
        member.email = body_data.get('email') or member.email
        member.password = bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8') or member.password

        # Commit the changes
        db.session.commit()

        return member_schema.dump(member)
    else:
        return {"error": f"Member with id {member_id} not found"}, 404

@member_bp.route('/<int:member_id>', methods=['DELETE'])
@jwt_required()
def delete_member(member_id):
    # Get the member to be deleted
    member = db.session.scalar(db.select(Member).filter_by(member_id=member_id))

    if member:
        # Delete the member from the session and commit
        db.session.delete(member)
        db.session.commit()
        return {'message': f"Member '{member.first_name} {member.last_name}' deleted successfully"}
    else:
        return {'error': f"Member with id {member_id} not found"}, 404
