from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db
from models.category import Category, category_schema, categories_schema

category_bp = Blueprint('categories', __name__, url_prefix='/categories')

@category_bp.route('/', methods=['GET'])
def get_all_categories():
    categories = db.session.scalars(db.select(Category))
    return categories_schema.dump(categories)

@category_bp.route('/<int:category_id>', methods=['GET'])
def get_one_category(category_id):
    category = db.session.scalar(db.select(Category).filter_by(category_id=category_id))
    if category:
        return category_schema.dump(category)
    else:
        return {"error": f"Category with id {category_id} not found"}, 404

@category_bp.route('/', methods=['POST'])
@jwt_required()
def create_category():
    body_data = category_schema.load(request.get_json())

    # Create a new category instance
    category = Category(
        name=body_data.get('name'),
        description=body_data.get('description')
    )

    # Add the category to the session and commit
    db.session.add(category)
    db.session.commit()

    return category_schema.dump(category), 201

@category_bp.route('/<int:category_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_category(category_id):
    # Get the category to be updated
    category = db.session.scalar(db.select(Category).filter_by(category_id=category_id))

    if category:
        # Update the category with the new data
        body_data = category_schema.load(request.get_json(), partial=True)
        category.name = body_data.get('name') or category.name
        category.description = body_data.get('description') or category.description

        # Commit the changes
        db.session.commit()

        return category_schema.dump(category)
    else:
        return {"error": f"Category with id {category_id} not found"}, 404

@category_bp.route('/<int:category_id>', methods=['DELETE'])
@jwt_required()
def delete_category(category_id):
    # Get the category to be deleted
    category = db.session.scalar(db.select(Category).filter_by(category_id=category_id))

    if category:
        # Delete the category from the session and commit
        db.session.delete(category)
        db.session.commit()
        return {'message': f"Category '{category.name}' deleted successfully"}
    else:
        return {'error': f"Category with id {category_id} not found"}, 404
