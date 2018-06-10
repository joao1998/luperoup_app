import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # segredo usado para login
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'segredo-para-seguranca'

    # uri com o endereco para aceder a base de dados
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

