from flask import render_template, request, flash, redirect, jsonify, send_from_directory,  url_for
from flask import send_file, Flask
from io import BytesIO
import os

DIRETORIO = "C:\\Users\\professor\\Documents\\PROJETO-MANDACARU\\app\\static\\files_SAVED"

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template('projetoVS.html')

@app.route('/teste')
def teste():
  return render_template('imagemAprimorada.html')


@app.route('/arquivo/<nome_do_arquivo>', methods=["GET"])
def get_arquivo(nome_do_arquivo):
  return send_from_directory(DIRETORIO, nome_do_arquivo, as_attachment=True)

@app.route('/arquivo', methods=["POST"])
def post_arquivo():
  ## parte que nao consegui
  
  arquivo = request.files.get('image') # image é o id
  print(arquivo)
  nome_do_arquivo = arquivo.filename
  arquivo.save(os.path.join(DIRETORIO,nome_do_arquivo))

  print(nome_do_arquivo)
  imagem_url = url_for('static', filename=f'files_SAVED/{nome_do_arquivo}')
  return render_template('imagemAprimorada.html', imagem_url=nome_do_arquivo)
    
  
if __name__ == '__main__':
    app.run(debug=True)