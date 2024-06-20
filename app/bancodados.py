import sqlite3

# Função para conectar ao banco de dados
def connect_db():
  return sqlite3.connect('usuarios_time12.db')

# Função para criar a tabela 'users' se não existir
def create_table():
  conn = connect_db()
  cursor = conn.cursor()
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY,
      name TEXT,
      cpf TEXT UNIQUE,
      password TEXT
  )
  ''')
  conn.commit()
  cursor.close()
  conn.close()

# Função para inserir um novo usuário na tabela 'users'
def insert_user(nome, cpf, senha):
  conn = connect_db()
  cursor = conn.cursor()
  
  # Verifica se o CPF já está na tabela
  cursor.execute('SELECT * FROM users WHERE name = ? AND cpf = ? AND password = ?', (nome, cpf, senha))
  result = cursor.fetchone()
  
  if result:
    cursor.close()
    conn.close()
    return 

  # Insere os dados na tabela 'users'
  cursor.execute('''
  INSERT INTO users (name, cpf, password) VALUES (?, ?, ?)
  ''', (nome, cpf, senha))
    
  conn.commit()
  cursor.close()
  conn.close()
  return False

def uptade(nome):
  return 0
  # Atualizando a idade de um usuário
  #conn.execute("UPDATE usuarios SET idade = 31 WHERE nome = 'Maria'")
  
# Função principal para demonstrar a inserção e verificação
def main():
  create_table()
  name = input("Digite o nome: ")
  cpf = input("Digite o CPF: ")
  password = input("Digite a senha: ")
  message = insert_user(name, cpf, password)
  print(message)

conn = connect_db()
# Seleciona todos os dados da tabela 'users'
cursor = conn.cursor()
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
  print(row)
# Fecha o cursor e a conexão
cursor.close()
conn.close()