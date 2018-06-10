from flask import render_template, flash, redirect, url_for, request
from app import app, db, api
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.resources.calhas import Calhas
from app.resources.vidros import Vidros


# Define url para fazer registo na aplicacao. valida form e adiciona user.
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# Define o url para o login na aplicacao
@app.route('/login', methods=['GET', 'POST'])
def login():

    # Caso o user esteja ja autenticado pelo flask-login, e redirecionado
    # para a pagina inicial
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    # Valida os dados que sao enviados do browser na altura do login.
    # De acordo com isso pode dar erro ou redirecionar para a pagina inicial
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        # Verifica se existe o user com o username dado e se a password faz match com a
        # existente na base de dados.
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        # FAz login do user com o flask-login
        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


# Route para fazer logout do user com o flask-login
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# Define urls para a pagina inicial. Login e necessario. Definido pelo decorator login_required do flask-login.
@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


api.add_resource(Calhas, '/api/calhas')
api.add_resource(Vidros, '/api/vidros')

