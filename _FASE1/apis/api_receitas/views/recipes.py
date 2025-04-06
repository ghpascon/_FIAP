from main import app,db
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flasgger import swag_from
from flask import request, jsonify
from models.database import Recipe

@app.route('/recipes', methods=['POST'])
@jwt_required()
@swag_from('../swagger/recipes/create_recipe.yml')
def create_recipe():
    data = request.get_json()
    new_recipe = Recipe(
        title=data['title'],
        ingredients=data['ingredients'],
        time_minutes=data['time_minutes']
    )
    
    db.session.add(new_recipe)
    db.session.commit()
    
    return jsonify({"msg": "Recipe created"}), 201

@app.route('/recipes', methods=['GET'])
@jwt_required()
@swag_from('../swagger/recipes/get_recipes.yml')
def get_recipes():
    ingredient = request.args.get('ingredient')
    max_time = request.args.get('max_time', type=int)

    query = Recipe.query
    if ingredient:
        query = query.filter(Recipe.ingredients.ilike(f"%{ingredient}%"))
    if max_time is not None:
        query = query.filter(Recipe.time_minutes <= max_time)

    recipes = query.all()

    return jsonify([
        {
            "id": r.id,
            "title": r.title,
            "ingredients": r.ingredients,
            "time_minutes": r.time_minutes
        }
        for r in recipes
    ])

@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
@jwt_required()
@swag_from('../swagger/recipes/update_recipe.yml')  # Referência ao arquivo YAML separado
def update_recipe(recipe_id):
    """Atualiza uma receita existente."""
    data = request.get_json()
    recipe = Recipe.query.get_or_404(recipe_id)

    if 'title' in data:
        recipe.title = data['title']
    if 'ingredients' in data:
        recipe.ingredients = data['ingredients']
    if 'time_minutes' in data:
        recipe.time_minutes = data['time_minutes']

    db.session.commit()
    return jsonify({"msg": "Recipe updated"}), 200

@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
@jwt_required()
@swag_from('../swagger/recipes/delete_recipe.yml')  # Referência ao arquivo YAML separado
def delete_recipe(recipe_id):
    """Deleta uma receita existente."""
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return jsonify({"msg": "Recipe not found"}), 404

    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"msg": "Recipe Deleted"}), 200