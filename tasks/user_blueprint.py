from flask import Blueprint, jsonify, request, abort
from models import User, db

user_blueprint = Blueprint('user_blueprint', __name__)

# Gets and returns all users
@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# Gets and returns an user with a specific ID
@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

# Create a user
@user_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

# Update a user
@user_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    request_data = request.get_json()
    user_to_update = User.query.get_or_404(user_id)
    request_username = request_data.get('username')
    request_email = request_data.get('email')
    if request_username and request_email:
        user_to_update.username = request_username
        user_to_update.email = request_email
        db.session.commit()
        return jsonify(user_to_update.to_dict())
    else:
        return abort(400, {'error': 'Niepełne dane użytkownika.'})

# Delete a user
@user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    user_to_delete = User.query.get_or_404(user_id)
    db.session.delete(user_to_delete)
    db.session.commit()
    return jsonify({})