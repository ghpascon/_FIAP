from flask import Flask
from config.app_config import Config
from flask_sqlalchemy import SQLAlchemy
import os

# Inicializa o banco de dados sem associar ao app ainda
db = SQLAlchemy()

def create_app():
    """Fábrica de aplicações Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa o banco de dados com o app
    db.init_app(app)

    # Importa os modelos depois de inicializar o app

    # Cria as tabelas dentro do contexto do app
    with app.app_context():
        if not os.path.exists(app.config['SQLALCHEMY_DATABASE_URI'].replace("sqlite:///", "")):
            print("🔹 Criando banco de dados...")
            db.create_all()
            print("✅ Banco de dados criado com sucesso!")
        else:
            print("✔ Banco de dados já existe.")

    return app
from models.database import *

# Criando a aplicação Flask
app = create_app()
