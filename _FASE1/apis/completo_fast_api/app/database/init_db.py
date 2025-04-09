from app.database.session import Base, engine
from app import models  # Isso importa todos os modelos via importlib

def init():
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    init()
