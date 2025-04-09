import os

folders = ['app', 'app/database' 'app/models', 'app/routes', 'app/auth', 'app/schemas']

files = {'app/main.py':'','.env': 'SECRET_KEY=your_secret_key\nALGORITHM=HS256\nACCESS_TOKEN_EXPIRE_MINUTES=30\nDATABASE_URL=sqlite:///./app.db\n', 'requirements.txt': 'fastapi==0.111.0\nuvicorn[standard]==0.29.0\npydantic==2.7.1\nSQLAlchemy==2.0.30\npython-jose==3.3.0\npasslib[bcrypt]==1.7.4\npython-dotenv==1.0.1\n', 'README.md': '# Projeto FastAPI com SQLAlchemy, JWT e .env\n\n## Instruções\n\n1. Instale as dependências:\n```bash\npip install -r requirements.txt\n```\n\n2. Execute o servidor:\n```bash\nuvicorn app.main:app --reload\n```\n\nAcesse: http://localhost:8000/docs\n'}

# Criar as pastas
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"[✔] Pasta criada: {folder}")

# Criar os arquivos
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[✔] Arquivo criado: {path}")

print("\n✅ Estrutura do projeto FastAPI criada com sucesso!")
