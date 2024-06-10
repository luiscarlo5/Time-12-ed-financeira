from flask import Blueprint
from flask import render_template, request, redirect
# para enxergar rotas em outros arquivos
from app.models import Usuario
from app.database import db

bp_gastos_investimentos = Blueprint("gastos_investimentos", __name__, template_folder="templates")

@bp_gastos_investimentos.route('/pegardados', methods=['GET', 'POST'])
def pegardados():
  if request.method=='GET':
    return render_template('Menu.html')
 
  if request.method=='POST':
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    senha = request.form.get('senha')
    csenha = request.form.get('csenha')
    
    u = Usuario(nome, cpf, senha)
    db.session.add(u)
    db.session.commit()
    return 'Cadastrados com sucesso'
  return render_template('usuarios_create.html')

@bp_gastos_investimentos.route('/recovery') 
def recovery():
  usuarios = Usuario.query.all() # recupera todos os usuarios e forma de objeto
  return render_template('usuarios_recovery.html', usuarios=usuarios)

@bp_gastos_investimentos.route('/update/<int:id>', methods=['GET', 'POST']) # recebe o id do ususrio
def update(id):
  u = Usuario.query.get(id)

  if request.method=='GET':
    
    return render_template('usuario_update.html', u = u)
  if request.method=='POST':
    nome = request.form.get('nome');
    senha = request.form.get('senha');
    u.nome = nome
    u.senha = senha
    db.session.add(u)
    db.session.commit()
    #return 'Dados atualizados com sucesso'
    return redirect('/usuarios/recovery') # rediciona para uma rota especifica    


@bp_gastos_investimentos.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
  u = Usuario.query.get(id)

  if request.method=='GET':
    return render_template('usuario_update.html', u = u)
  
  if request.method=='POST':

    db.session.delete(u)
    db.session.commit()
    return 'Dados deletados com sucesso'
  