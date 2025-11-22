from flask import Blueprint, jsonify, request
from services import generate_token
from models import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"msg": "Missing required fields"}), 400
    
    users = User.query.filter((User.username == username) | (User.email == email)).first()
    
    if users:
        return jsonify({"msg": "User with given username or email already exists"}), 409

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(username=username, email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Missing required fields"}), 400
    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"msg": "Invalid username or password"}), 401

    token = generate_token(user.id)

    return jsonify({"token": token, "msg": f"User {username} succesfully authenticated."}), 200


@auth_bp.route('/users', methods=['GET'])
@jwt_required()
def list_users():
    users = User.query.all()
    users_data = [{"id": user.id, 
                   "username": user.username, 
                   "email": user.email, 
                   "created_at": user.created_at} for user in users]
    return jsonify(users_data), 200