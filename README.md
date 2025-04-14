Plataforma The Twelve Web para educação financeira, com área de ensino padrão e lúdico e de anásile de gastos e investimentos do cliente, podendo ter a possibilidade de ter previsões atráves de IAs de previsão (modelos clássicos)

# 💰 EduFinance - Plataforma Interativa de Educação Financeira

![EduFinance Banner](https://media.giphy.com/media/xT0GqzTQmGk5YkLCy0/giphy.gif)

## 📘 Sobre o Projeto

O **EduFinance** é uma plataforma interativa feita com 💻 **Flask + Python** para ajudar jovens e adultos a aprenderem sobre finanças de forma divertida!

🔍 O projeto inclui:
- Quizzes com temas de orçamento, investimentos, dívidas e mais 💸
- Previsor inteligente de gastos usando **regressão linear** 🤖
- Análises financeiras com **matplotlib** 📊
- Banco de dados local com **SQLite3** 💾
- Visual moderno com imagens e **GIFs motivacionais** 🎉

---

## 🚀 Tecnologias Utilizadas

| Tecnologia      | Finalidade |
|------------------|------------|
| Python           | Lógica do projeto |
| Flask            | Backend Web |
| SQLite3          | Banco de dados |
| Matplotlib       | Gráficos |
| HTML/CSS + Jinja2| Templates |
| Scikit-learn     | IA (Regressão Linear) |
| Pandas / Numpy   | Manipulação e análise de dados |

---

## 🧠 IA - Previsor Financeiro

Utilizamos **Regressão Linear** para prever os gastos mensais dos usuários com base no histórico de despesas e receitas.

### Etapas do pipeline:

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Carregar dados
df = pd.read_csv('dados_financeiros.csv')

# Pré-processamento
df = df.dropna()
X = df[['renda_mensal', 'gastos_essenciais', 'gastos_lazer']]
y = df['gasto_previsto']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Treinamento
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Previsão
previsao = modelo.predict([[3000, 1200, 500]])
