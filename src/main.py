import os

from flask import Flask
from marshmallow.exceptions import ValidationError

from init import db, ma, bcrypt, jwt

def create_app():
    app = Flask(__name__)

    app.json.sort_keys = False

    # Configurations
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    # Connect libraries with Flask app
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Error handlers
    @app.errorhandler(400)
    def bad_request(err):
        return {"error": str(err)}, 400

    @app.errorhandler(404)
    def not_found(err):
        return {"error": str(err)}, 404

    @app.errorhandler(ValidationError)
    def validation_error(error):
        return {"error": error.messages}, 400

    # Register blueprints
    from controllers.book_controller import book_bp
    app.register_blueprint(book_bp)

    from controllers.member_controller import member_bp
    app.register_blueprint(member_bp)

    # Add more controllers as needed

    return app

