from fastapi import FastAPI
import os
import importlib
from pathlib import Path
readme_path = Path(__file__).parent / "README.md"
readme_content = readme_path.read_text(encoding="utf-8")

app = FastAPI(
    title="Minha API",
    description=readme_content,
    version="1.0.0",
    terms_of_service="https://meusite.com/termos",
    contact={
        "name": "Gabriel Henrique Pascon",
        "url": "https://github.com/seuusuario",
        "email": "gh.pascon@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)



def include_all_routes():
    routes_path = os.path.join(os.path.dirname(__file__),"app", "routes")

    for filename in os.listdir(routes_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            file_path = os.path.join(routes_path, filename)

            spec = importlib.util.spec_from_file_location(f"app.routes.{module_name}", file_path)
            module = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(module)
                if hasattr(module, "router"):
                    app.include_router(module.router)
                    print(f"✅ Rota incluída: {module_name}")
                else:
                    print(f"⚠️  Arquivo {filename} não contém um 'router'")
            except Exception as e:
                print(f"❌ Erro ao importar {filename}: {e}")

include_all_routes()


# python -m app.database.init_db
# uvicorn main:app --reload
