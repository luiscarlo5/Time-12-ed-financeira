from flask import Flask, render_template

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

@app.route('/visualizadorGrafico')
def visualizadorGrafico():
  return render_template('visualizadorGrafico.html')

@app.route('/visualizadorGraficoPrime')
def visualizadorGraficoPrime():
  return render_template('visualizadorGraficoPrime.html')

@app.route('/edfinanceira')
def edfinanceira():
  return render_template('ed-financeira.html')


   


@app.route('/quiz')
def quiz():
  return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=True)
