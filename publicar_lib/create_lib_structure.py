import os

# Definir nome do projeto e módulos
nome_lib = "ghp_utils_test"
modulos = ["saudacoes", "operacoes"]

def criar_estrutura_lib(nome_lib, modulos):
    estrutura = [
        f"{nome_lib}/",
        f"{nome_lib}/{nome_lib}/",
        f"{nome_lib}/{nome_lib}/__init__.py",
        f"{nome_lib}/tests/",
        f"{nome_lib}/setup.py",
        f"{nome_lib}/README.md",
        f"{nome_lib}/requirements.txt",
        f"{nome_lib}/.gitignore",
        f"{nome_lib}/LICENSE"
    ]
    
    # Adicionar módulos e testes
    for modulo in modulos:
        estrutura.append(f"{nome_lib}/{nome_lib}/{modulo}.py")
        estrutura.append(f"{nome_lib}/tests/test_{modulo}.py")
    
    # Criar estrutura de diretórios e arquivos
    for caminho in estrutura:
        if caminho.endswith("/"):
            os.makedirs(caminho, exist_ok=True)
        else:
            open(caminho, "w").close()

    # Preencher os arquivos automaticamente
    preencher_arquivos(nome_lib, modulos)
    
    print(f"Estrutura do projeto '{nome_lib}' criada com sucesso!")

def preencher_arquivos(nome_lib, modulos):
    # Preencher setup.py
    content = f"""from setuptools import setup, find_packages

setup(
    name="{nome_lib}",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # Adicione aqui as dependências, se houver
    author="ghpascon",
    description="Biblioteca de utilitários para saudações e operações básicas",
    url="https://github.com/ghpascon/ghp_utils_test",  # Substitua com o link real
    license="MIT",
    )
    """
    with open(f"{nome_lib}/setup.py", "w") as f:
        f.write(content)

    # Preencher README.md
    content = f"""
# Teste de upload de lib para o pypl
    """
    with open(f"{nome_lib}/README.md", "w") as f:
        f.write(content)           

    # Preencher LICENSE
    content = f"""
MIT License

Copyright (c) 2025 Gabriel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

    """
    with open(f"{nome_lib}/LICENSE", "w") as f:
        f.write(content)        
    
    

if __name__=="__main__":
    criar_estrutura_lib(nome_lib,modulos)