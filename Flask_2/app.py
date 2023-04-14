from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return 'Sobre'

# Caso tentem entrar com caminho inexistente
@app.route('/<string:nome>')
def error(nome):
    erro_no_caminho = f'<h1> A Página que você está procurando ({nome}) Inexistente </h1>'
    return erro_no_caminho

@app.route('/jogo', methods=["GET", "POST"])    # O método "POST" tambem deve estar form do game.html
def jogo():
    variavel = "Game: Adivinhe o número correto"
    
    if request.method == "GET":
        return render_template("game.html", variavel=variavel)
    else:
        numero = randint(1,20)
        palpite = int(request.form.get("name"))
        if numero == palpite:
            return '<h1> Você acertou</h1>'
        else:
            return '<h1> Perdeu.</h1>'
