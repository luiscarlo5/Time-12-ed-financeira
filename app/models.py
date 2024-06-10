from app import db, bcrypt

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    banco = db.relationship('Banco', backref='usuario', uselist=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Usuario {self.username}>'

class GastosInvestimentos(db.Model):
  id = db.Column(db.Integer, primary_key=True)


  user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

  def __repr__(self):
    return f'<Banco {self.bank_name} - {self.account_number}>'

def create_database():
    db.create_all()
