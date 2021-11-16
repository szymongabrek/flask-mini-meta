import os
from flask import Flask, render_template,request, redirect
from flask.helpers import url_for
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

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


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Tutaj zaprogramuj dodanie uzytkownika do bazy
        username = request.form["username"]
        password = request.form["password"]

        database = db.get_db()
        error = None

        if not username:
            error = "Username is required"
        elif not password:
            error = "Dawaj hasło"
        
        if not error:
            try:
                database.execute(f"INSERT INTO user (username, password) VALUES (?, ?", (username, generate_password_hash(password)))

                database.commit()
            except database.IntegrityError:
                error = f"User {username} is already registered"
            else:
                return redirect(url_for("login"))





        return f"Tutaj kiedyś utworzymy Ci uzytkownika: {username}@{password}"
    return render_template("auth/register.html", title="Register")


@app.route('/logout')
def logout():
    return "Wylogowano"
