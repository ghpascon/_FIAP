from flask import Flask
from config.app_config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flasgger import Swagger
import importlib
import pkgutil

app = Flask(__name__)

# https://flask.palletsprojects.com/en/stable/config/
app.config.from_object(Config)

db = SQLAlchemy(app)

jwt = JWTManager(app)

swagger = Swagger(app)

import views
for module_info in pkgutil.iter_modules(views.__path__):
    module = importlib.import_module(f"views.{module_info.name}")
    exec(f"from views.{module_info.name} import *")

if __name__ == "__main__":
    app.run(debug=True)