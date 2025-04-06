from main import app,db
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flasgger import swag_from
from flask import request, jsonify
from models.database import User

@app.route('/auth/register', methods=['POST'])
@swag_from('../swagger/auth/register.yml')
def register_user():
    data = request.get_json()

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "User already exists"}), 400

    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User created"}), 201

@app.route('/auth/login', methods=['POST'])
@swag_from('../swagger/auth/login.yml')  # Referência ao arquivo externo
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and user.password == data['password']:
        token = create_access_token(identity=str(user.id))
        return jsonify({"access_token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401