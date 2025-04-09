from passlib.context import CryptContext

# Define o contexto com o algoritmo bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para gerar o hash da senha
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Exemplo de uso
if __name__ == "__main__":
    senha = input("Digite a senha: ")
    hash_senha = hash_password(senha)
    print(f"Senha criptografada: {hash_senha}")
