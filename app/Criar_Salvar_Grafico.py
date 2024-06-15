import matplotlib.pyplot as plt
from ModelosIA import Varejo as IA 

import os

   
def grafico_em_barra_topicos(topicos, gastos):
  # Gráfico de barra
  plt.figure(figsize=(8, 6))
  plt.bar(topicos, gastos, color='blue')
  plt.title('Gastos por Dia (Barra)')
  plt.ylabel('Gastos em R$')
  plt.xlabel('Dias da Semana')
  plt.tight_layout()
  pasta = 'app/static/imgs_matplotlib'
  if not os.path.exists(pasta):
    os.makedirs(pasta) 
  caminho_completo = os.path.join(pasta, 'gastos_barra_topico.png')
  # Salvar o gráfico
  plt.savefig(caminho_completo)
  plt.close()

def grafico_semanal_em_barra(dias, gastos):
  plt.figure(figsize=(8, 6))
  plt.bar(dias, gastos, color='blue')
  plt.title('Gastos por Dia (Barra)')
  plt.ylabel('Gastos em R$')
  plt.xlabel('Dias da Semana')
  plt.tight_layout()
  pasta = 'app/static/imgs_matplotlib'
  if not os.path.exists(pasta):
    os.makedirs(pasta) 
  caminho_completo = os.path.join(pasta, 'gastos_barra_semanal_.png')
  plt.savefig(caminho_completo)
  plt.close()


def gastos_mensais(meses, gastos):
  plt.figure(figsize=(8, 6))
  plt.barh(meses, gastos, color='green')
  plt.title('Gastos Mensais (Coluna)')
  plt.xlabel('Gastos em R$')
  plt.ylabel('Dias da Semana')
  plt.tight_layout()
  pasta = 'app/static/imgs_matplotlib'
  if not os.path.exists(pasta):
    os.makedirs(pasta) 
  caminho_completo = os.path.join(pasta, 'gastos_coluna_mensal_.png')
  plt.savefig(caminho_completo)
  plt.close()

def gasto_grupos_topicos(topicos, dados):
   
  plt.figure(figsize=(8, 6))
  plt.pie(dados, labels=topicos, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
  plt.title('Gastos por grupo')
  plt.tight_layout()
  pasta = 'app/static/imgs_matplotlib'
  if not os.path.exists(pasta):
    os.makedirs(pasta) 
  caminho_completo = os.path.join(pasta, 'dados_pizza_mensal.png')
  plt.savefig(caminho_completo)
  plt.close()

def grafico_linha_meses(meses, dados, premiun=False):
  # Gráfico de linha
  if premiun==True:
    meses_aux = ['janeiro', 'fevereiro', 'março',' abril', 'maio', 'junho', 'julho', 'agosto', 'setembro']
    meses = meses_aux
    novos_dados = IA.previsor(dados[-1]) 
    dados = dados + novos_dados



  plt.figure(figsize=(8, 6))
  plt.plot(meses, dados, marker='o', linestyle='-', color='red')
  plt.title('Gastos mensal atual e futuros')
  plt.ylabel('Gastos em R$')
  plt.xlabel('Meses em 2024')
  plt.tight_layout()
  pasta = 'app/static/imgs_matplotlib'
  if not os.path.exists(pasta):
    os.makedirs(pasta)  
  caminho_completo = os.path.join(pasta, 'previsao_mensal_por_IA.png')
  plt.savefig(caminho_completo)
  plt.close()
