# Mandacaru.dev – The Twelve  
### Plataforma Web de Educação Financeira com IA, Gráficos e Metodologia Ágil

Este projeto é uma aplicação web desenvolvida com **Flask**, focada em **Educação Financeira**, combinando recursos informativos, gráficos interativos, quizzes e um módulo de **previsão com Inteligência Artificial**.  
Foi desenvolvido ao longo de pouco mais de **1 mês**, aplicando princípios de **metodologia ágil**, priorização de funcionalidades e integração contínua.

---

## Funcionalidades Principais

### 1. Área Informativa de Educação Financeira  
Conteúdos introdutórios e explicativos sobre finanças pessoais, pensados para usuários iniciantes.

### 2. Inteligência Artificial  
Um modelo de **Regressão Linear** treinado a partir de dados históricos de inflação de alimentos no estado de São Paulo.  
Ele gera uma **previsão para os próximos 3 meses**, exibida no último gráfico da aba de visualizações.

*O modelo foi desenvolvido em um notebook no Google Colab:*  
`Time 12/app/ModelosIA/Notebook-&-Dados_Ia`

---

### 3. Inserção de Dados pelo Usuário  
O usuário pode inserir:

- Gastos mensais (janeiro a junho)  
- Gastos semanais (segunda a domingo)  
- Categorias de despesas (alimentação, imóvel, água, energia etc.)  
- Salário mensal  

Essas informações são registradas e utilizadas para gerar diversos gráficos.

---

### 4. Geração de Gráficos  
A aplicação cria automaticamente gráficos por meio do módulo:

