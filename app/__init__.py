from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(Config)

# Variavel usada para aceder a base de dados pelo python
db = SQLAlchemy(app)

# Usada para fazer gestao das versoes da base de dados
migrate = Migrate(app, db)

# Usado para gerir autenticacao e acesso a routes
login = LoginManager(app)

# Usado para definir routes
api = Api(app)

# Variavel usada para definir a route usada para o login. Util em caso de
# redirect quando o user nao tem permissoes para ver certas paginas.
login.login_view = 'login'

from app import routes, models