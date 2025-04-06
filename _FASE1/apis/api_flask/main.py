from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger

app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'Flask API FIAP',
    'description': 'API de exemplo documentada com Flasgger',
    'version': '1.0.0',
    'termsOfService': '/terms',  # Página de termos de uso (opcional)
    'contact': {
        'name': 'Equipe de Suporte',
        'email': 'suporte@email.com',
        'url': 'https://www.fiap.com.br'
    },
    'license': {
        'name': 'MIT',
        'url': 'https://opensource.org/licenses/MIT'
    },
    'uiversion': 3,  # Usa a versão mais recente do Swagger UI
    'swagger_ui': True,  # Habilita o Swagger UI
    'specs_route': '/docs/'  # Altera a URL padrão da documentação
}
swagger = Swagger(app) 

auth = HTTPBasicAuth()

users = {
    "user1":"123",
    "user2":"456",
}
@auth.verify_password
def verify_password(username,password):
    if username in users and users[username]==password:
        return username
    return None

from views.basics import *
from views.crud import *
from views.scrapping import *

if __name__ == "__main__":
    app.run(debug=True)