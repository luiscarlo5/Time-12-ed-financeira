from flask import render_template, request, flash, redirect, jsonify, send_from_directory,  url_for
from flask import send_file, Flask
from io import BytesIO
import os
from flask_migrate import Migrate  #para fazer o mapeamento do objeto relacional



#DIRETORIO = "C:\\Users\\professor\\Documents\\PROJETO-MANDACARU\\app\\static\\files_SAVED"
  
from flask import Flask, render_template
from app.database import db
from app.usuarios import bp_usuarios
from flask_migrate import Migrate  #para fazer o mapeamento do objeto relacional
from app.models import create_database

class Config:
  SECRET_KEY = 'CHAVE-time12'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///dbmeu.sqlite'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)  #inicializa o banco de dados com a variavel app

# app.config['SECRECT_KEY'] = 'CHAVE-time12'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbmeu.sqlite'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # para imitir informações do sistema
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
# bp_usuarios = Blueprint("usuarios", __name__, template_folder="templates")



migrate = Migrate(app, db)  #inicializa o mapeamento do objeto relacional
# vai associar minha aplicação app a minha aplicação bd

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('projetoTime12_flask.html')

if __name__ == '__main__':
    with app.app_context():
        create_database()
    app.run(debug=True)


#def create_app():
  # app = ...
  # existing code omitted
  #from . import db
  #db.init_app(app)

  #return app
#def create_app():
  #app = ...
  # existing code omitted
  #from . import auth
  #app.register_blueprint(auth.bp)

  #return app



#@app.route('/Login')
#def login():
  # autenticar 
  # if true  return render_template('Menu.html')
  # if false  return render_template('Registar.html')
  # return render_template('Menu.html')

#@app.route('/regitrar')
#def registrar():
  # registrar usuario e seus dados de ultimos gastos

  
  #return render_template('Menu.html')

#@app.route('/menu')
#def menu():
  # redirecionar para
  # estudo de educação financeira     - Ed-financeira.html
  # exercícios de ed. fianceira       - quiz.html
  # gráficos de gastos/investimentos  - visualizadorGrafico.html
  #return render_template('funcionalidadeEscolhida.html')


#@app.route('/graficos')
#def visualizadorGrafico():
  # pega dados da página e joga no bd do usuario logado e manda 
  # para /backend/Criar-Salvar-Grafico.py que salva os graficos 
  # em /static/imgs_matplotlib

  # manda o caminho atualizado dos graficos que foram salvos como
  # imagens .jpg e manda para o template visualizadorGrafico.html

  #return render_template('visualizadorGrafico.html')
  
if __name__ == '__main__':
  app.run(debug=True)