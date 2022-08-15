# ***************************************
# =============== IMPORTS ===============
# ***************************************
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, col
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

class Driver(db.Model, UserMixin):
    dln = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(20), primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    dob = db.Column(db.Date(), nullable=False)

class Vehicle(db.Model, UserMixin):
    vin = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(1), nullable=False)

class VehicleDriver(db.Model, UserMixin):
    vin = db.Column(db.Integer, db.ForeignKey(Vehicle.vin), primary_key=True)
    dln = db.Column(db.Integer, db.ForeignKey(Driver.dln), primary_key=True)
    state = db.Column(db.String(20), db.ForeignKey(Driver.state), primary_key=True)

class Customer(db.Model, UserMixin):
    cid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    street = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(30), nullable=True)
    marital_status = db.Column(db.String(1), nullable=False)

class Insurance(db.Model, UserMixin):
    policy_id = db.Column(db.Integer, primary_key=True)
    policy_type = db.Column(db.String(1), nullable=False)

class Invoice(db.Model, UserMixin):
    inv_num = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    due_date = db.Column(db.Date(), nullable=False)
    policy_id = db.Column(db.Integer, db.ForeignKey(Insurance.policy_id), nullable=False)

class Payment(db.Model, UserMixin):
    transaction_id = db.Column(db.Integer, primary_key=True)
    inv_num = db.Column(db.Integer, db.ForeignKey(Invoice.inv_num), primary_key=True)
    payment_date = db.Column(db.Date(), nullable=False)
    method = db.Column(db.String(6), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

class Home(db.Model, UserMixin):
    hid = db.Column(db.Integer, primary_key=True)
    purchase_date = db.Column(db.Date(), nullable=False)
    purchase_value = db.Column(db.Integer, nullable=False)
    area = db.Column(db.Integer, nullable=False)
    home_type = db.Column(db.String(1), nullable=False)
    aff = db.Column(db.Integer, nullable=False)
    hss = db.Column(db.Integer, nullable=False)
    sp = db.Column(db.String(1), nullable=True)
    basement = db.Column(db.String(1), nullable=False)
    street = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)

class HomeInsurance(db.Model, UserMixin):
    hid = db.Column(db.Integer, db.ForeignKey(Home.hid), primary_key=True)
    policy_id = db.Column(db.Integer, db.ForeignKey(Insurance.policy_id), primary_key=True)
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    premium = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(1), nullable=False)

class AutoInsurance(db.Model, UserMixin):
    hid = db.Column(db.Integer, db.ForeignKey(Home.hid), primary_key=True)
    vin = db.Column(db.Integer, db.ForeignKey(Vehicle.vin), primary_key=True)
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    premium = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(1), nullable=False)

class CustomerInsurance(db.Model, UserMixin):
 cid = db.Column(db.Integer, db.ForeignKey(Customer.cid), primary_key=True)
 policy_id = db.Column(db.Integer, db.ForeignKey(Insurance.policy_id), primary_key=True)

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
            flash("That username already exists. Please choose a different one.", "error")
            raise ValidationError(
                'That username already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Password"})
    submit = SubmitField("Login")

class ForgotPassword(FlaskForm):
    email = EmailField(validators=[InputRequired()], render_kw={"placeholder": "Enter Email"})
    submit = SubmitField("Login")

class CustomerInsurancesTable(Table):
    ### TODO ###



# ***************************************
# ================ ROUTES ===============
# ***************************************
@app.route("/")
@app.route("/home")
@login_required
def home():
    home_insurances = Insurance.join(HomeInsurance, HomeInsurance.policy_id == Insurance.policy_id )\
        .join(CustomerInsurance, CustomerInsurance.policy_id == Insurance.policy_id)\
        .filter_by(CustomerInsurance.cid == current_user.cid).all()

    auto_insurances = Insurance.join(AutoInsurance, AutoInsurance.policy_id == Insurance.policy_id )\
        .join(CustomerInsurance, CustomerInsurance.policy_id == Insurance.policy_id)\
        .filter_by(CustomerInsurance.cid == current_user.cid).all()

    home_table = Table(home_insurances)
    auto_table = Table(auto_insurances)

    return render_template("home.html", auto_table = auto_table, home_table=home_table)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     if user:
    #         if bcrypt.check_password_hash(user.password, form.password.data):
    #             login_user(user)
    #             return redirect(url_for('home'))
    if not form.validate_on_submit():
        return render_template("login.html", form=form)
    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        flash("Username doesn't exist", "error")
        return render_template("login.html", form=form)
    if not bcrypt.check_password_hash(user.password, form.password.data):
        flash("Wrong password", "error")
        return render_template("login.html", form=form)
    login_user(user)
    return redirect(url_for('home'))


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