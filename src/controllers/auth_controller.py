from datetime import timedelta
from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from psycopg2 import errorcodes

from init import db, bcrypt
from models.member import Member, member_schema

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route("/register", methods=["POST"])
def auth_register():
    try:
        # Get the data from the request body
        body_data = request.get_json()

        # Create a new member instance
        member = Member(
            first_name=body_data.get('first_name'),
            last_name=body_data.get('last_name'),
            email=body_data.get('email'),
            password=bcrypt.generate_password_hash(body_data.get('password')).decode('utf-8')
        )

        # Add and commit the member to the database
        db.session.add(member)
        db.session.commit()

        # Return the registered member
        return member_schema.dump(member), 201

    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The {err.orig.diag.column_name} is required"}, 400
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "Email address already in use"}, 409

@auth_bp.route("/login", methods=["POST"])
def auth_login():
    # Get the data from the request body
    body_data = request.get_json()

    # Find the member with the email address
    stmt = db.select(Member).filter_by(email=body_data.get("email"))
    member = db.session.scalar(stmt)

    # If the member exists and the password is correct
    if member and bcrypt.check_password_hash(member.password, body_data.get("password")):
        # Create a JWT token
        token = create_access_token(identity=str(member.member_id), expires_delta=timedelta(days=1))
        # Return the token along with the member info
        return {"email": member.email, "token": token}
    else:
        # Return an error
        return {"error": "Invalid email or password"}, 401