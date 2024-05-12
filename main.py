# Статья по хэшу пароля: https://proproprogs.ru/flask/registraciya-polzovateley-i-shifrovanie-paroley

from flask import Flask, make_response, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


menu = [
    {'name': 'Главная',
     'url': 'index'},
    {'name': 'Обо мне',
     'url': 'about'},
     {'name': 'Каталог',
     'url': 'catalog'},
     {'name': 'Контакты',
     'url': 'contacts'},
     {'name': 'Регистрация',
      'url': "registration"} 
]

@app.route('/')
def index():
    context = {
        'title': "Главная",
        'menu': menu
    }
    return render_template('index.html', **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.route('/about/')
def about():
    context = {
        'title': "Обо мне",
        'menu': menu
    }
    return render_template('about.html', **context)

@app.route('/catalog/')
def catalog():
    context = {
        'title': "Каталог",
        'menu': menu
    }
    return render_template('catalog.html',**context)


@app.route('/contacts/')
def contacts():
    context = {
        'title': "Контакты",
        'menu': menu
    }
    return render_template('contacts.html',**context )

@app.route('/login/')
def login(): 
    context = {
        'title': "Вход",
        'menu': menu
    }
    return render_template('login.html', **context)

@app.post('/login/')
@csrf.exempt
def login_post():
    name = request.form.get('name')
    phone = request.form.get('phone')
    context = {
        'title': "Вход",
        'menu': menu,
        'name': name
    }
    response = make_response(render_template('hello.html', **context))
    response.set_cookie('username', name)
    response.set_cookie('phone', phone) 
    return response

@app.route('/exit/')
def exit():
    responce = make_response(redirect(url_for('index')))
    responce.delete_cookie('username')
    responce.delete_cookie('phone')
    return responce


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        firstname = form.firsname.data
        secondname = form.secondname.data
        email = form.email.data
        hash = generate_password_hash(form.password.data)
        user = User(firstname = firstname, secondname = secondname, email = email, password = hash)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html', form=form)

@app.route('/users/')
def all_users():
    users = User.query.all()
    print(users)
    return render_template('index.html', )

if __name__ == "__main__":
    app.run(debug=True)
