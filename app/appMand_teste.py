from flask import Flask, render_template, request
from . import Criar_Salvar_Grafico as grafico

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template('projetoTime12_flask.html')

@app.route('/login')
def login():
  return render_template('login_flask.html')

@app.route('/menu')
def menu():
  return render_template('Menu.html')

@app.route('/inserirDados',methods=['GET', 'POST'])
def visualizadorGrafico():
  if request.method == 'POST':
    # Processamento dos gastos diários e por tópico, como antes
    # Processamento dos gastos mensais
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
    meses = ['janeiro', 'fevereiro', 'março',' abril', 'maio', 'junho']
    grafico.gastos_mensais( meses , dados_mensais )
    #grafico.grafico_semanal_em_barra(dias, gastos)
    if Prime==True:
      grafico.grafico_linha_dias(meses, dados_alimentacao, premiun=True)
    else:
      grafico.grafico_linha_dias(meses, dados_alimentacao, premiun=False)

  return render_template('inserirDados.html')

@app.route('/graficos')
def visualizadorGrafico():
  return render_template('Graficos.html')

@app.route('/edfinanceira')
def edfinanceira():
  return render_template('ed-financeira.html')

@app.route('/quiz')
def quiz():
  return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=True)
