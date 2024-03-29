import os
from flask import Flask
from marshmallow.exceptions import ValidationError

# Import the extensions from the init.py file
from init import db, ma, bcrypt, jwt

# Import the models
from models.book import Book
from models.borrowing_record import BorrowingRecord
from models.category import Category
from models.member import Member
from models.staff import Staff

# Import the controllers (blueprints)
from controllers.auth_controller import auth_bp
from controllers.book_controller import book_bp

# Create the Flask application
app = Flask(__name__)

# Configure the Flask application
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the extensions with the Flask app
db.init_app(app)
ma.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# Define error handlers
@app.errorhandler(400)
def bad_request(err):
    return {"error": str(err)}, 400

@app.errorhandler(404)
def not_found(err):
    return {"error": str(err)}, 404

@app.errorhandler(ValidationError)
def validation_error(error):
    return {"error": error.messages}, 400

# Register blueprints (controllers)
app.register_blueprint(auth_bp)
app.register_blueprint(book_bp)

# Define a route for the index
@app.route('/')
def index():
    return "Welcome to LibraLink Library Management System"

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        # Create database tables if they don't exist
        db.create_all()
    # Run the Flask application
    app.run(debug=True)
