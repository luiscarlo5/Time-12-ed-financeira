from flask import Flask, render_template, request, flash, redirect, url_for, session
import codigo_calnum_efg as codigoG
app = Flask(__name__)
app.secret_key = 'supersecretkey_calc_num'  # Necessário para usar sessões

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    num_c = request.form.get('num_c')
    session['numero_C'] = num_c 
    return redirect(url_for('numc', num_c=num_c)) # chama afunção e nao a rota
  return render_template('CalNum.html')


@app.route('/num_c', methods=['GET', 'POST'])
def numc():
  if request.args.get('num_c') != None:
    num_c = request.args.get('num_c')
  else:
    num_c = session.get('numero_C')
  
  num_c_int = int(num_c)

  #print(f"tome tome tome{num_c}  {type(num_c_int) }")
  # Cria uma lista com números de 1 até num
  #numeros = list(range(1, num_c_int + 1))
  numeros = []
  for i in range(0, num_c_int):
    numeros.append(i+1)
    #print(f"uauauauau{i}")

  #num_c = request.args.get('num_c')
  if request.method == 'POST':
    #print(f"numeros {numeros} {type(numeros)}")
    lista_c_enviados = []
    for i in numeros:
      aux = f"valorC_numero{str(i)}"
      lista_c_enviados.append( request.form.get(aux) )
      #print("Bom dia princesa")
      
    session['lista_c_enviados'] = lista_c_enviados
    ##print(session)

    return redirect(url_for('resultc'))
  return render_template('Num_c.html', num_c=numeros)

@app.route('/results_c', methods=['GET'])
def resultc():
  lista_c_enviados = session.get('lista_c_enviados', [])
  num_c = session.get('num_c', 1)
  #print(lista_c_enviados)
  lista_int = []
  for stringC in lista_c_enviados:
    lista_int.append(int(stringC))
  C = session.get('numero_C')

  C_int = int(C)
  print(f"---------{C} -- {type(C_int)}")
  print(f"---------{lista_int} -- {type(lista_int)}")
  print(f"---------{5} -- {type(5)}")
  resultadosLC = codigoG.mega_funcao(C_int, lista_int)

  return render_template('resultc.html', resultadosLC=resultadosLC)

   


if __name__ == '__main__':
    app.run(debug=True)
