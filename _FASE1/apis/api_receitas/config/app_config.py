class Config:
    SECRET_KEY = 'my_secret'
    CACHE_TYPE = 'simple'
    SWAGGER = {
        'title': 'Catálogo de receitas gourmet',
        'uiversion': 3
    }
    SQLALCHEMY_DATABASE_URI = 'sqlite:///recipes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'my_jwt'