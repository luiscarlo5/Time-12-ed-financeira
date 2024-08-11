#Trabalho computacional I
#Disciplina: Cálculo Numérico
#Objetivos:
#Implementar os métodos numéricos estudados para achar raízes de equações.
#Resolver, analisar e apresentar soluções para vários problemas com os métodos numéricos a serem implementados.
#Data da Entrega: 13/08/2024
#Alunos:
#Horley Alfredo dos Santos 473104
#Antônio Gustavo de Almeida Lemos 553091
#Luis Carlos Rodrigues dos Anjos 509022
#Samuel Sales Furtado 413384
#Antonio Mateus Barbosa Azevedo 470988
#Janielle do Nascimento Albino 510765
#Gabriel Richard Tavares de Oliveira 538828
#Noely Gomes Barroso 512262

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

#print("opa meu patrão")
caminho_completo = ""

# a) Implementar algoritmo para calcular Q pelo método do Ponto Fixo com um Φ que converge.
def metodo_ponto_fixo(g, x0, tol, maxiter):
  x1 = g(x0)

  erro = abs(x1-x0)/abs(x1)

  verro = []
  vraiz = []
  vphi = []
  it = 1

  verro.append(erro)
  vraiz.append(x0)
  vphi.append(x1)

  while erro > tol and it < maxiter:
    x0 = x1
    x1 = g(x0)

    erro = abs(x1-x0)/abs(x1)

    verro.append(erro)
    vraiz.append(x0)
    vphi.append(x1)

    it = it+1

  return(x1, vraiz, vphi, verro)

# b)  Implementar algoritmo para calcular Q pelo método de Newton modificado.
def metodo_newton_raphson(f, g, x0, tol, maxiter):
  x1 = x0 - (f(x0)/g(x0))
  erro = abs(x1-x0)/abs(x1)

  vraiz_x0 = []
  vraiz_x1 = []
  vfuncao = []
  vderivada = []
  verro = []

  it = 1

  vraiz_x0.append(x0)
  vraiz_x1.append(x1)
  vfuncao.append(f(x0))
  vderivada.append(g(x0))
  verro.append(erro)


  while erro > tol and it < maxiter:
    x0 = x1
    x1 = x0 - (f(x0)/g(x0))

    erro = abs(x1-x0)/abs(x1)

    vraiz_x0.append(x0)
    vraiz_x1.append(x1)
    vfuncao.append(f(x0))
    vderivada.append(g(x0))
    verro.append(erro)

    it = it+1

  return(x1, vraiz_x0, vraiz_x1, vfuncao, vderivada, verro)

# c) Implementar algoritmo para calcular Q pelo método da Secante original.
def metodo_secante(f, x0, x1, tol, max_iter):
  fle = (f(x1)-f(x0))/(x1-x0)
  x2 = x1 - f(x1)/fle

  erro = abs(x2-x1)/abs(x1)

  vraiz_x1 = []
  vraiz_x2 = []
  vfuncao_x1 = []
  vfuncao_x2 = []
  verro = []

  vraiz_x1.append(x0)
  vraiz_x2.append(x1)
  vfuncao_x1.append(f(x0))
  vfuncao_x2.append(f(x1))
  verro.append(erro)

  it = 1

  while erro > tol and it < max_iter:
    x0 = x1
    x1 = x2

    fle = (f(x1)-f(x0))/(x1-x0)
    x2 = x1 - f(x1)/fle

    erro = abs(x2-x1)/abs(x1)

    vraiz_x1.append(x0)
    vraiz_x2.append(x1)
    vfuncao_x1.append(f(x0))
    vfuncao_x2.append(f(x1))
    verro.append(erro)

    it=it+1

  return (x2, vraiz_x1, vraiz_x2, vfuncao_x1, vfuncao_x2, verro)

# d) Testar os resultados para d usando como padrão C = 1, Q0 = 0,5 e ε = 10-4.
# Definindo a função f(Q)
def create_f(C):
  def f(Q):
    return C * np.exp(Q) - 4 * Q**2
  return f

# Definindo a derivada de f(Q)
def create_g(C):
  def g(Q):
    return (C * np.exp(Q) - 8 * Q)
  return g

## Isolamento gráfico ##***
def isolamento_grafico(C, Q0):
  # Valores de Q (em Toneladas)
  Q = np.linspace(Q0, 1, 400)

  # Plotando a função Custo f(Q)
  plt.figure(figsize=(10, 6))

  f = create_f(C)
  plt.plot(Q, f(Q), label=f'f(Q) com C={C}')

  plt.title('Gráfico da função f(Q) = Ce^Q - 4Q^2 para diferentes valores de C (em Bilhões)')
  plt.xlabel('Q (em Toneladas)')
  plt.ylabel('f(Q)')
  plt.legend()
  plt.grid(True)

  #plt.savefig(caminho_completo)
  plt.close()


# Valores de C e Q0
C = 1
Q0 = 0.5

isolamento_grafico(C, Q0)

##  Isolamento analítico   ##***
def isolamento_analitico(C, Q0, h):
  intervalos = []

  f = create_f(C)

  while Q0 < C:
    if f(Q0) * f(Q0+h) < 0:
      intervalos.append((Q0, Q0+h))
    Q0 += h

  return intervalos

# Valores de C e Q0
C = 1
Q0 = 0.5

# Passo
h = 0.01
isolamento_analitico(C, Q0, h)

## Método do ponto fixo ## 
# Usuando φ_1(Q)
def create_phi_1(C):
  def phi_1(Q):
    return (C * np.exp(Q)) / (4 * Q)
  return phi_1
Q0 = 0.5
C = 1
tol = 1e-4
maxiter = 100

start_time = time.time()
[raiz_ponto_fixo_com_phi1, raizes, phis, erros] = metodo_ponto_fixo(create_phi_1(C), Q0, tol, maxiter)
end_time = time.time()

tempo_execucao_ponto_fixo_com_phi1 = end_time - start_time

# Exibir a raiz encontrada
#print(f'Raiz encontrada Q = {raiz_ponto_fixo_com_phi1}\n')

# Criar DataFrame
data = {
    'Raizes Xi': raizes,
    'Phi g(Xi)': phis,
    'Erros': erros
}

df_ponto_fixo_com_phi1 = pd.DataFrame(data)

## Usuando φ_3(Q)
# Definindo a phi_3(Q)
def create_phi_3(C):
  def phi_3(Q):
    return (np.sqrt(C * np.exp(Q))) / 2
  return phi_3

Q0 = 0.5
C = 1
tol = 1e-4
maxiter = 100

start_time = time.time()
[raiz_ponto_fixo_com_phi3, raizes, phis, erros] = metodo_ponto_fixo(create_phi_3(C), Q0, tol, maxiter)
end_time = time.time()

tempo_execucao_ponto_fixo_com_phi3 = end_time - start_time

# Exibir a raiz encontrada
#print(f'Raiz encontrada Q = {raiz_ponto_fixo_com_phi3}\n')

# Criar DataFrame
data = {
    'Raizes Xi': raizes,
    'Phi g(Xi)': phis,
    'Erros': erros
}

df_ponto_fixo_com_phi3 = pd.DataFrame(data)

# Método de Newton
Q0 = 0.5
C = 1
tol = 1e-4
maxiter = 100

start_time = time.time()
[raiz_newton_raphson, raizes_x0, raizes_x1, funcoes, derivadas, erros] = metodo_newton_raphson(create_f(C), create_g(C), Q0, tol, maxiter)
end_time = time.time()

tempo_execucao_newton_raphson = end_time - start_time

# Exibir a raiz encontrada
#print(f'Raiz encontrada Q = {raiz_newton_raphson}\n')

# Criar DataFrame
data = {
    'Raizes Xi': raizes_x0,
    'Funcoes F(Xi)': funcoes,
    'Derivadas dF(Xi)': derivadas,
    'Raizes Xi+1': raizes_x1,
    'Erros': erros
}

df_newton_raphson = pd.DataFrame(data)

# Método da Secante
Q0 = 0.5
Q = 1
C = 1
tol = 1e-4
maxiter = 100


start_time = time.time()
[raiz_secante, raizes_x1, raizes_x2, funcoes_x1, funcoes_x2, erros] = metodo_secante(create_f(C), Q0, Q, tol, maxiter)
end_time = time.time()

tempo_execucao_secante = end_time - start_time
# Exibir a raiz encontrada
#print(f'Raiz encontrada Q = {raiz_secante}\n')

# Criar DataFrame
data = {
    'Raizes (X_k-1)': raizes_x1,
    'Raizes (X_k)': raizes_x2,
    'Funcoes f(X_k-1)': funcoes_x1,
    'Funcoes f(X_k)': funcoes_x2,
    'Erros': erros
}

df_secante = pd.DataFrame(data)

#print(df_secante['Erros'])
#print("deu certo")