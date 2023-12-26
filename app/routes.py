from app import app
from app.forms import LoginForm,SignupForm
from flask import render_template, flash, redirect, url_for


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    user = {"username": "name"}
    posts = [
        {"author": {"username": "John"}, "body": "Hey there"},
        {"author": {"username": "Mike"}, "body": "Welcome"},
    ]
    loginform = LoginForm()
    signupform = SignupForm()
    forms = {
        'signup': signupform,
        'login': loginform
    }

    return render_template(    
        "index.html", title="Home", user=user, posts=posts, form=forms
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if form.validate_on_submit():
        flash(
            "Login requested for {}, remember me = {}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In")


@app.route("/login", methods=["GET", "POST"])
def signup():
    if form.validate_on_submit():
        flash(
            "Login requested for {}, remember me = {}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In")
