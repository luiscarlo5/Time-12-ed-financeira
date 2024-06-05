from flask import render_template, request, flash, redirect, jsonify, send_from_directory,  url_for
from flask import send_file, Flask
from io import BytesIO
import os

DIRETORIO = "C:\\Users\\professor\\Documents\\PROJETO-MANDACARU\\app\\static\\files_SAVED"

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template('InicioTime12.html')

@app.route('/Login')
def login():
  # autenticar 
  # if true  return render_template('Menu.html')
  # if false  return render_template('Registar.html')
  return render_template('Menu.html')

@app.route('/regitrar')
def registrar():
  # registrar usuario e seus dados de ultimos gastos
  return render_template('Menu.html')

@app.route('/menu')
def menu():
  # redirecionar para
  # estudo de educação financeira     - Ed-financeira.html
  # exercícios de ed. fianceira       - quiz.html
  # gráficos de gastos/investimentos  - visualizadorGrafico.html
  return render_template('funcionalidadeEscolhida.html')


@app.route('/graficos')
def visualizadorGrafico():
  # pega dados da página e joga no bd do usuario logado e manda 
  # para /backend/Criar-Salvar-Grafico.py que salva os graficos 
  # em /static/imgs_matplotlib

  # manda o caminho atualizado dos graficos que foram salvos como
  # imagens .jpg e manda para o template visualizadorGrafico.html

  return render_template('visualizadorGrafico.html')
  
if __name__ == '__main__':
    app.run(debug=True)