def mega_funcao(C, lista_c):
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd
  import time
  import codigo_calnum as abcd
  import os

  #e) Fornecer um quadro resposta, com Q calculado para cada método dado (comparando resposta, acurácia(erro), tempo, número de iterações etc).

  # Ponto fixo
  # Usuando φ_1(Q)
  #print(f'Raiz encontrada para o método do Ponto Fixo com phi_1 Q = {abcd.raiz_ponto_fixo_com_phi1}\n')
  #print(f'Tempo de execução do método do Ponto Fixo com phi_1: {abcd.tempo_execucao_ponto_fixo_com_phi1} segundos\n\n')
  #print(abcd.df_ponto_fixo_com_phi1)

  # Usuando φ_3(Q)
  #print(f'Raiz encontrada para o método do Ponto Fixo com phi_3 Q = {abcd.raiz_ponto_fixo_com_phi3}\n')
  #print(f'Tempo de execução do método do Ponto Fixo com phi_3: {abcd.tempo_execucao_ponto_fixo_com_phi3} segundos\n\n')
  #print(abcd.df_ponto_fixo_com_phi3)

  # Newton Raphson
  #print(f'Raiz encontrada para o método de Newton Raphson Q = {abcd.raiz_newton_raphson}\n')
  #print(f'Tempo de execução do método do Ponto Fixo com phi_3: {abcd.tempo_execucao_newton_raphson} segundos\n\n')
  #print(abcd.df_newton_raphson)

  # Secante
  #print(f'Raiz encontrada para o método da Secante Q = {abcd.raiz_secante}\n')
  #print(f'Tempo de execução do método da Secante: {abcd.tempo_execucao_secante} segundos\n\n')
  #print(abcd.df_secante)

  ## f) Fornecer um quadro comparativo, com todos os dados para cada método (comparando resposta, acurácia (erro),
  #  tempo, número de iterações etc).
  data = {
      'Metodos': ['metodo_ponto_com_phi1', 'metodo_ponto_com_phi3', 'metodo_newton_raphson', 'metodo_secante'],
      'Raizes': [
          abcd.raiz_ponto_fixo_com_phi1,
          abcd.raiz_ponto_fixo_com_phi3,
          abcd.raiz_newton_raphson,
          abcd.raiz_secante
      ],
      'Erro': [
          abcd.df_ponto_fixo_com_phi1['Erros'].iloc[-1],
          abcd.df_ponto_fixo_com_phi3['Erros'].iloc[-1],
          abcd.df_newton_raphson['Erros'].iloc[-1],
          abcd.df_secante['Erros'].iloc[-1]
      ],
      'Tempo_execucao': [
          abcd.tempo_execucao_ponto_fixo_com_phi1,
          abcd.tempo_execucao_ponto_fixo_com_phi3,
          abcd.tempo_execucao_newton_raphson,
          abcd.tempo_execucao_secante
      ],
      'Numero_iteracoes': [
          len(abcd.df_ponto_fixo_com_phi1),
          len(abcd.df_ponto_fixo_com_phi3),
          len(abcd.df_newton_raphson),
          len(abcd.df_secante)
      ]
  }

  df_resultados = pd.DataFrame(data)
  #print(df_resultados)

  ###
  df_resultados_erro = df_resultados.sort_values(by='Erro')
  # Plot comparando os Erros encontrados
  plt.figure(figsize=(10, 6))
  plt.bar(df_resultados_erro['Metodos'], df_resultados_erro['Erro'], color='brown')
  plt.xlabel('Metodos')
  plt.ylabel('Erro')
  plt.title('Comparação dos Erros encontrados')
  plt.close()


  ###
  df_resultados_tempo_execucao = df_resultados.sort_values(by='Tempo_execucao')
  # Plot comparando os Erros encontrados
  plt.figure(figsize=(10, 6))
  plt.bar(df_resultados_tempo_execucao['Metodos'], df_resultados_tempo_execucao['Tempo_execucao'], color='#C0BBF9')
  plt.xlabel('Metodos')
  plt.ylabel('Tempo de execução')
  plt.title('Comparação dos Tempos de execução encontrados')
  plt.close()

  #plt.show()

  ###
  df_resultados_numero_iteracoes = df_resultados.sort_values(by='Numero_iteracoes')
  # Plot comparando os Erros encontrados
  plt.figure(figsize=(10, 6))
  plt.bar(df_resultados_numero_iteracoes['Metodos'], df_resultados_numero_iteracoes['Numero_iteracoes'], color='#DB6446')
  plt.xlabel('Metodos')
  plt.ylabel('Número de iterações')
  plt.title('Comparação dos Números de iterações encontrados')
  plt.close()


  C = C
  pasta = 'calculo_numerico/app/static/imgs_matplotlib'

  # g) Analisar o efeito da variação do valor de C (diferentes fornecedores) para cada método 
  # considerado(comparando resposta, acurácia (erro), tempo, número de iterações etc).

  # Dados de entrada: n (número de valores de C), C (para cada n) e ε (precisão).
  # Dados de saída: quadros resposta (com Q e erro para cada C e método) e comparativo.
  # Valores para C
  # n = int(input('Digite o número de valores de C: '))
  C_values = []
  for i in lista_c:
    C_values.append(i)

  # Isolamento
  Q0 = 0.5
  h = 0.01

  intervalos = []
  Resultados_isolamento = ""
  for C in C_values:
    intervalos.append(abcd.isolamento_analitico(C, Q0, h))
    if len(intervalos[-1]) == 0:
      #print('Não a troca de sinal')
      Resultados_isolamento = Resultados_isolamento+'- Não a troca de sinal\n' 
    else:
      #print(intervalos[-1])
      Resultados_isolamento = Resultados_isolamento+" - "+str(intervalos[-1])+"\n" 
  #print(Resultados_isolamento )
  # Comparação dos métodos
  resultados = []
  for C in C_values:

    # Método do Ponto Fixo phi1
    Q0 = 0.5
    tol = 1e-4
    maxiter = 100
    start_time = time.time()
    [raiz_ponto_fixo1, vraiz1, vph1i, erros_ponto_fixo1] = abcd.metodo_ponto_fixo(abcd.create_phi_1(C), Q0, tol, maxiter)
    tempo_execucao_ponto_fixo1 = time.time() - start_time

    # Método do Ponto Fixo
    Q0 = 0.5
    tol = 1e-4
    maxiter = 100
    start_time = time.time()
    [raiz_ponto_fixo3, vraiz3, vphi3, erros_ponto_fixo3] = abcd.metodo_ponto_fixo(abcd.create_phi_3(C), Q0, tol, maxiter)
    tempo_execucao_ponto_fixo3 = time.time() - start_time

    # Método de Newton-Raphson
    Q0 = 0.5
    tol = 1e-4
    maxiter = 100
    start_time = time.time()
    [raiz_newton, vraiz_x0, vraiz_x1, vfuncao, vderivada, erros_newton] = abcd.metodo_newton_raphson(abcd.create_f(C), abcd.create_g(C), Q0, tol, maxiter)
    tempo_execucao_newton = time.time() - start_time

    # Método da Secante
    Q0 = 0.5
    Q1 = 1
    tol = 1e-4
    maxiter = 100
    start_time = time.time()
    [raiz_secante,vraiz_x1, vraiz_x2, vfuncao_x1, vfuncao_x2, erros_secante] = abcd.metodo_secante(abcd.create_f(C), Q0, Q1, tol, maxiter)
    tempo_execucao_secante = time.time() - start_time

    resultados.append({
        'C': C,
        'Raiz Ponto Fixo Phi1': raiz_ponto_fixo1,
        'Erro Ponto Fixo Phi1': erros_ponto_fixo1[-1] if erros_ponto_fixo1 else None,
        'Tempo Ponto Fixo Phi1': tempo_execucao_ponto_fixo1,
        'Iterações Ponto Fixo Phi1': len(erros_ponto_fixo1),
        'Raiz Ponto Fixo Phi3': raiz_ponto_fixo3,
        'Erro Ponto Fixo Phi3': erros_ponto_fixo3[-1] if erros_ponto_fixo3 else None,
        'Tempo Ponto Fixo Phi3': tempo_execucao_ponto_fixo3,
        'Iterações Ponto Fixo Phi3': len(erros_ponto_fixo3),
        'Raiz Newton': raiz_newton,
        'Erro Newton': erros_newton[-1] if erros_newton else None,
        'Tempo Newton': tempo_execucao_newton,
        'Iterações Newton': len(erros_newton),
        'Raiz Secante': raiz_secante,
        'Erro Secante': erros_secante[-1] if erros_secante else None,
        'Tempo Secante': tempo_execucao_secante,
        'Iterações Secante': len(erros_secante)
    })

  # Criando um DataFrame com os resultados
  df_comparacao = pd.DataFrame(resultados)
  df_comparacao

  tempo_ponto_fixo1 = df_comparacao['Tempo Ponto Fixo Phi1'].tolist()
  tempo_ponto_fixo3 = df_comparacao['Tempo Ponto Fixo Phi3'].tolist()
  tempo_newton = df_comparacao['Tempo Newton'].tolist()
  tempo_secante = df_comparacao['Tempo Secante'].tolist()


  metodos = ['Ponto Fixo Phi1', 'Ponto Fixo Phi3', 'Newton', 'Secante']

  plt.bar(metodos, [tempo_ponto_fixo1[0], tempo_ponto_fixo3[0] , tempo_newton[0], tempo_secante[0]])

  plt.title('Comparação do Tempo de Execução')
  plt.xlabel('Método')
  plt.ylabel('Tempo de Execução')
  if not os.path.exists(pasta):
    os.makedirs(pasta)
  nome_aux = 'Tempo_execucao.png'
  caminho_completo = os.path.join(pasta, nome_aux)
  plt.savefig(caminho_completo)
  plt.close()


  erros_ponto_fixo1 = df_comparacao['Erro Ponto Fixo Phi1'].tolist()
  erros_ponto_fixo3 = df_comparacao['Erro Ponto Fixo Phi3'].tolist()
  erros_newton = df_comparacao['Erro Newton'].tolist()
  erros_secante = df_comparacao['Erro Secante'].tolist()

  metodos = ['Ponto Fixo Phi1', 'Ponto Fixo Phi3', 'Newton', 'Secante']
  import matplotlib.pyplot as plt

  plt.bar(metodos, [erros_ponto_fixo1[0], erros_ponto_fixo3[0], erros_newton[0], erros_secante[0]])

  plt.title('Comparação dos Erros')
  plt.xlabel('Método')
  plt.ylabel('Erro')
  if not os.path.exists(pasta):
    os.makedirs(pasta)
  nome_aux = 'comparacao_erros.png'
  caminho_completo = os.path.join(pasta, nome_aux)
  plt.savefig(caminho_completo)
  plt.close()


  import matplotlib.pyplot as plt
  iteracoes_ponto_fixo1 = df_comparacao['Iterações Ponto Fixo Phi1'].tolist()
  iteracoes_ponto_fixo3 = df_comparacao['Iterações Ponto Fixo Phi3'].tolist()
  iteracoes_newton = df_comparacao['Iterações Newton'].tolist()
  iteracoes_secante = df_comparacao['Iterações Secante'].tolist()

  metodos = ['Ponto Fixo Phi1', 'Ponto Fixo Phi3', 'Newton', 'Secante']
  plt.bar(metodos, [iteracoes_ponto_fixo1[0], iteracoes_ponto_fixo3[0], iteracoes_newton[0], iteracoes_secante[0]])

  plt.title('Comparação do Número de Iterações')
  plt.xlabel('Método')
  plt.ylabel('Número de Iterações')
  if not os.path.exists(pasta):
    os.makedirs(pasta)
  nome_aux = 'comparacao_iteracoes.png'
  caminho_completo = os.path.join(pasta, nome_aux)
  plt.savefig(caminho_completo )
  plt.close()

  return Resultados_isolamento

