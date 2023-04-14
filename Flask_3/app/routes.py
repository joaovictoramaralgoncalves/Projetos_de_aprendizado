from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = "Jão"
    dados = {"profissão": "Estagiário","Função": "--"}
    return render_template('index.html', nome = nome, dados = dados)

@app.route('/contato')
def contao():
    return render_template('contato.html')