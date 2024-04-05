from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = "Beto"
    dado = {"profissao": "Tec Suporte", "local": "Ufes"}
    return render_template('index.html', name=nome, dados=dado)

@app.route('/users')
def users():
    return render_template('users.html')
