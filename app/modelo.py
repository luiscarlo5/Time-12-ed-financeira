from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class Usuario(db.Model):
  __tablename__="usuario"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(100), nullable=False)
  cpf = db.Column(db.String(100), unique=True, nullable=False)
  senha = db.Column(db.String(128), nullable=False)

  def _init_(self, nome, cpf, senha):
    self.nome = nome
    self.cpf = cpf
    self.senha = senha  

  def set_password(self, senha):
    self.senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')

  def check_password(self, senha):
    return bcrypt.check_password_hash(self.senha_hash, senha)

class Financa(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
  ano = db.Column(db.Integer, nullable=False)
  mes = db.Column(db.Integer, nullable=False)
  custo_fixo = db.Column(db.Float, nullable=False)
  custo_variavel = db.Column(db.Float, nullable=False)
  lucro_total = db.Column(db.Float, nullable=False)

  usuario = db.relationship('Usuario', backref=db.backref('financas', lazy=True))

  def __repr__(self):
    return "Usuario: {}".format(self.nome)
  # se chamarmos este metodo ao printarmos aparece esse metodo __repr__

def create_database():
  db.create_all()

