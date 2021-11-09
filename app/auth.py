from flask import render_template, app
@app.route('/login')
def login():
    return render_template("auth/login.html", title="Login")


@app.route('/register')
def register():
    return render_template("auth/register.html", title="Register")


@app.route('/logout')
def logout():
    return "Wylogowano"
