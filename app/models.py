from app import db, login
from datetime import datetime

# Usado para gerar versoes codificadas das passwords a guardar na base de dados
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# Funcao para o flask-login saber como deve ir aceder ao user na base de dados
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# Tabela da base de dados para definir um utilizador
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Maneira como o python mostra no terminal depois de fazer print
    def __repr__(self):
        return '<User {}>'.format(self.username)


class Melamina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    espessura = db.Column(db.String(140))
    cor = db.Column(db.String(140))
    stock = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Melamina {}-{}>'.format(self.cor, self.espessura)


class Perfil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referencia = db.Column(db.String(140))
    tipo = db.Column(db.String(140))
    cor = db.Column(db.String(140))
    stock = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Perfil {}>'.format(self.referencia)


class Calha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referencia = db.Column(db.String(140))
    tipo = db.Column(db.String(140))
    cor = db.Column(db.String(140))
    stock = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Calha {}>'.format(self.referencia)


class Vidro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(140))
    cor = db.Column(db.String(140))
    stock = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Vidro {}>'.format(self.tipo)


class Rodizio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(140))
    stock = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Rodizio {}>'.format(self.tipo)


class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(140))
    receita = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Modelo {}>'.format(self.tipo)