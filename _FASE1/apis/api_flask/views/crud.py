from flask import jsonify, request
from main import app
from flasgger import swag_from

lista = []
@app.route("/items", methods=['GET'])
@swag_from({
    'tags': ['CRUD'],
    'summary': 'Retorna a lista',
    'description': 'Retorna a lista',
    'responses': {
        '200': {
            'description': 'lista com os itens',
        }
    }
})
def ler_items():
    return jsonify(lista)
    
@app.route("/items", methods=['POST'])
@swag_from({
    'tags': ['CRUD'],
    'summary': 'Adiciona um item na lista',
    'description': 'Adiciona um item na lista',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'item': {'type': 'string', 'example': 'caneta'},
                },
                'required': ['item']
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Item adicionado com sucesso',
        },
        '400': {
            'description': 'Erro ao adicionar item'
        }
    }
})
def adicionar():
    data = request.get_json()
    lista.append(data)
    return jsonify(data),201



@app.route("/items/<int:item_id>", methods=['PUT'])
def update(item_id):
    data = request.get_json()
    if 0<= item_id <len(lista):
        lista[item_id]=data
        return jsonify(lista[item_id])
    return jsonify({"error":"item not found"}),404

@app.route("/items/<int:item_id>", methods=['DELETE'])
def remover(item_id):
    if 0<= item_id <len(lista):
        removed = lista.pop(item_id)
        return jsonify(removed)
    return jsonify({"error":"item not found"}),404