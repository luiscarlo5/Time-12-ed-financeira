

import matplotlib.pyplot as plt
# Dados dos gastos nos últimos 7 dias
dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
gastos = [45, 60, 30, 50, 70, 20, 55]

meses = []
investimentos = []


# Gráfico de barra
plt.figure(figsize=(8, 6))
plt.bar(dias, gastos, color='blue')
plt.title('Gastos por Dia (Barra)')
plt.ylabel('Gastos em R$')
plt.xlabel('Dias da Semana')
plt.tight_layout()
plt.savefig('./static/imgs_matplotib/gastos_barra.png', dpi=300)
plt.close()

def grafico_semanal_embarra(dias, gastos):
  # Gráfico de barra
  plt.figure(figsize=(8, 6))
  plt.bar(dias, gastos, color='blue')
  plt.title('Gastos por Dia (Barra)')
  plt.ylabel('Gastos em R$')
  plt.xlabel('Dias da Semana')
  plt.tight_layout()
  plt.savefig('./static/imgs_matplotib/gastos_barra_semanal.png', dpi=300)
  plt.close()

def gastos_mensais(meses, gastos):
  # Gráfico de coluna (horizontal)
  plt.figure(figsize=(8, 6))
  plt.barh(meses, gastos, color='green')
  plt.title('Gastos por Dia (Coluna)')
  plt.xlabel('Gastos em R$')
  plt.ylabel('Dias da Semana')
  plt.tight_layout()
  plt.savefig('./static/imgs_matplotib/gastos_coluna.png', dpi=300)
  plt.close()



def gasto_grupos():
  # Gráfico de pizza
  plt.figure(figsize=(8, 6))
  plt.pie(gastos, labels=dias, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
  plt.title('Gastos por grupo')
  plt.tight_layout()
  plt.savefig('./static/imgs_matplotib/gastos_pizza_.png', dpi=300)
  plt.close()


def grafico_linha(dias, gastos):
  # Gráfico de linha
  plt.figure(figsize=(8, 6))
  plt.plot(dias, gastos, marker='o', linestyle='-', color='red')
  plt.title('Gastos por Dia')
  plt.ylabel('Gastos em R$')
  plt.xlabel('Dias da Semana')
  plt.tight_layout()
  plt.savefig('./static/imgs_matplotib/gastos_linha.png', dpi=300)
  plt.close()

