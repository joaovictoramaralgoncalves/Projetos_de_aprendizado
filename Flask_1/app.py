# API - é um lugar para disponivilizar recursos e /ou funcionalidades
# 1. Objetivo - Criar um api de disponibiliza a consulta, criação,edição e exclusão de livros.
# 2. URL base - localhost
# 3.Enpoints-
#     - localhost/livros (GET)
#     - localhost/livros/id (GET)
#     - localhost/livros/id (PUT)
#     - localhost/livros/id (DELETE)
# 4. Quais recursos - Livros

from flask import Flask, jsonify, request


#Criando aplicação flask com o nome do arquivo atual
app = Flask(__name__)   

livros = [
    {
     'id': 1, 
     'títulos': 'O Senhor dos Anéis - A Sociedade do Anel',
     'autor': 'J.R.R Tolken'
    },
    {
    'id': 2,
    'título': 'Harry Potter e a Pedra Filosofal',
    'autor': 'J.K Howling'
    },
    {
    'id': 3,
    'título': 'James Clear',
    'autor': 'Hábitos Atômicos'
    }
]

# Colsultar(todos)
@app.route('/livros', methods = ['GET'])    # methods = ['GET'] para aceirar somente o método GET
def obter_livros():    # a função obter_livros() retorna a var livros em formato json
    return jsonify(livros)


# Consultar(id)
@app.route('/livros/<int:id>', methods = ['GET'])
def obter_livro_por_id(id):
    for livro in livros:    # para cada livro em livros eu vou pegar a classe id
        if livro.get('id') == id:    # verificar se .get('id') é igual a var id
            return jsonify(livro)

# Editar
@app.route('/livros/<int:id>', methods = ['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)    # pegar o item e atualizar para a alteração feita
            return jsonify(livros[indice])


# Criar
@app.route('/livros', methods = ['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

# Excluir
@app.route('/livros/<int:id>', methods = ['DELETE'])
def Excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)