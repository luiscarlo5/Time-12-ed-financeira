from flask import Flask, render_template, request, flash, redirect, url_for
import Criar_Salvar_Grafico as grafico
import bancodados as bd

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template('projetoTime12_flask.html')

@app.route('/login', methods=['GET','POST'])
def login():
  bd.create_table()
  if request.method == 'POST':

    nome = request.form['nome']
    cpf = request.form['cpf']
    senha = request.form['senha']
    aux = bd.insert_user(nome, cpf, senha)
    if aux == True:
      return redirect(url_for('menu', nome=nome))
    else:
      return redirect(url_for('menu', nome=nome+' pela primeira vez'))
    
  return render_template('login_flask.html')

@app.route('/menu')
def menu():
  nome = request.args.get('nome')
  return render_template('menu.html', nome=nome)

@app.route('/inserirDados',methods=['GET', 'POST'])
def inserirDados():
  if request.method == 'POST':
    january = float(request.form['january'])
    february = float(request.form['february'])
    march = float(request.form['march'])
    april = float(request.form['april'])
    may = float(request.form['may'])
    june = float(request.form['june'])
    dados_mensais = [january, february, march, april, may, june]

    # grafico.gasto_grupos_topicos(topicos, salariorenda, dados)
    # grafico.grafico_em_barra_topicos(topicos, gastos)
    dias = []
    dados_alimentacao = request.form['food']
    meses = ['janeiro', 'fevereiro', 'março',' abril', 'maio', 'junho']
    grafico.gastos_mensais( meses , dados_mensais )
    


    seg = float(request.form['monday'])
    ter = float(request.form['tuesday'])
    qua = float(request.form['wednesday'])
    qui = float(request.form['thursday'])
    sex = float(request.form['friday'])
    sab = float(request.form['saturday'])
    dom = float(request.form['sunday'])
    sem = [seg, ter, qua, qui, sex, sab, dom]
    sem_nome = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
    grafico.grafico_semanal_em_barra(sem_nome, sem)

    salario = float(request.form['sallary'])
    alimentacao = float(request.form['food'])
    entreterimento = float(request.form['entertainment'])
    imovel = float(request.form['housing'])
    transporte = float(request.form['transportation'])
    energia = float(request.form['energy'])
    agua = float(request.form['water'])

    topicos_nome = ['Restante', 'Alimentação', 'Entreterimente', 'Imóvel', 'Transporte', 'Energia', 'Água']
    diferenca = salario - (alimentacao + entreterimento + imovel + transporte + energia)
    topicos_gastos = [diferenca, alimentacao, entreterimento, imovel, transporte, energia, agua ]
    grafico.gasto_grupos_topicos(topicos_nome, topicos_gastos)
    Prime = True
    if Prime==True:
      grafico.grafico_linha_meses(meses, dados_mensais, premiun=True)
    else:
      grafico.grafico_linha_meses(meses, dados_mensais, premiun=False)

    return redirect(url_for('menu'))
    
  return render_template('inserirDados.html')

@app.route('/graficos')
def graficos():
  return render_template('graficos.html')

@app.route('/edfinanceira')
def edfinanceira():
  return render_template('ed-financeira.html')

@app.route('/quiz')
def quiz():
  return render_template('quiz.html')

@app.route('/deletar')
def deletar():
  nome = request.args.get('nome')
  return render_template('atualizar_deletar.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
