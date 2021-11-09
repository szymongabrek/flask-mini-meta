import os
from flask import Flask, render_template
from . import db

app = Flask(__name__, instance_relative_config=True)

app.config["DATABASE"] = os.path.join(app.instance_path, 'minimeta.sqlite')
app.config["SECRET_KEY"] = 'tajne haslo'

#node lepszy

db.init_app(app)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass


@app.route('/')
@app.route('/hello')
def hello():
    user = {'username': 'Zdziso'}
    posts = [
        { 'author': {'username': 'Euzebiusz'},
           'body': 'Na górze roze na dole fikołki'},
        { 'author': {'username': 'Duzo'},
        'body': 'Lorem ipsum sit dolor amet!'},
    ]
    return render_template("blog/index.html", title="Home", user=user, posts=posts)

@app.route('/login')
def login():
    return render_template("auth/login.html", title="Login")


@app.route('/register')
def register():
    return render_template("auth/register.html", title="Register")


@app.route('/logout')
def logout():
    return "Wylogowano"
