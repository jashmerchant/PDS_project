# ***************************************
# =============== IMPORTS ===============
# ***************************************
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt


# ***************************************
# =============== CONFIGS ===============
# ***************************************
app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "error"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ***************************************
# =============== MODELS ================
# ***************************************
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(80), nullable=False)


# ***************************************
# ================ FORMS ================
# ***************************************
class RegistrationForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Username"})
    email = EmailField(validators=[InputRequired()], render_kw={"placeholder": "Enter Email"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Password"})
    submit = SubmitField("Register")

    # Validate if username is unique
    def validate_username(self, username):
        # Try to look through db to find a similar username
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        # If it founds a similar username in db it'll raise a validation error thus guaranting unique usernames
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Password"})
    submit = SubmitField("Login")

class ForgotPassword(FlaskForm):
    email = EmailField(validators=[InputRequired()], render_kw={"placeholder": "Enter Email"})
    submit = SubmitField("Login")



# ***************************************
# ================ ROUTES ===============
# ***************************************
@app.route("/")
@app.route("/home")
@login_required
def home():
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home'))

    return render_template("login.html", form=form)

@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/forgotpassword", methods=['GET', 'POST'])
def forgot_password():
    return render_template("forgot_password.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account successfully created!", "success")
        return redirect(url_for('login'))

    return render_template("register.html", form=form)

@app.route("/admin")
@login_required
def admin():
    username = current_user.username
    if username == "admin":
        return render_template("admin.html")
    else:
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)