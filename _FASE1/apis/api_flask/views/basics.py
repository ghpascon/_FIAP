from flask import jsonify
from main import app,auth
from flasgger import swag_from

@app.route("/")
def index():
    """
    Index route
    """
    return 'Api Flask'

@app.route('/hello')
@auth.login_required
@swag_from({
    'tags': ['BASICS'],
    'summary': 'Saudação simples',
    'description': 'Retorna uma mensagem de saudação.',
    'responses': {
        200: {
            'schema': {
                'example': {"msg": "Hello World"}
            }        
        },
        401: {
            'description': 'Não autorizado'
        }
    }
})
def hello():
    return jsonify({"msg":"Hello World"})
