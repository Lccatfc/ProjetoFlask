from flask import Flask, render_template, request
import mysql.connector
import json
from mainmysql import myResult, insere


app = Flask(__name__)


@app.route("/inserir")
def inserir():
  email = request.args.get('email')
  nome = request.args.get('nome')
  age = request.args.get('age')
  if 'email' not in request.args or 'nome' not in request.args or 'age' not in request.args:
    return 'Não tem dados'
  insere(email, nome, age)
  return 'você inseriu dados'

@app.route("/exibir")
def index():
  dados = request.args.get('coluna')
  return json.dumps(myResult(dados))
  return dados


if __name__ == '__main__':
  app.run(debug=True)
