from main import app
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask import jsonify
from flasgger import swag_from

@app.route('/')
def index():
    return 'API RECEITAS'

@app.route('/protected')
@jwt_required()
@swag_from('../swagger/basics/protected.yml')
def protected():
    current_user_id = get_jwt_identity()
    return jsonify({"msg":f"Usuario com id {current_user_id} acessou a rota protegida"})