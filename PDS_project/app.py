# ***************************************
# =============== IMPORTS ===============
# ***************************************
from flask import Flask, render_template, url_for, redirect, flash, request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous.url_safe import URLSafeTimedSerializer
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
import forms
from flask_mail import Mail, Message
from wtforms import BooleanField, IntegerField, StringField, EmailField, PasswordField, RadioField, SubmitField, DateField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from datetime import datetime
import random


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

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'bhargavamakwana@gmail.com'
app.config['MAIL_PASSWORD'] = 'rxbrebznbrzxnzpi'
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)


# ***************************************
# =============== MODELS ================
# ***************************************
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def get_token(self, expires_sec=400):
        serial = Serializer(app.config['SECRET_KEY'], expires_in=expires_sec)
        return serial.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_token(token):
        serial = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = serial.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

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
    # username = db.Column(db.String(20), nullable=False)
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
    hid = db.Column(db.Integer, db.ForeignKey(Home.hid), primary_key=True, unique=True)
    policy_id = db.Column(db.Integer, db.ForeignKey(Insurance.policy_id), primary_key=True)
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    premium = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(1), nullable=False)

class AutoInsurance(db.Model, UserMixin):
    policy_id = db.Column(db.Integer, db.ForeignKey(Home.hid), primary_key=True)
    vin = db.Column(db.Integer, db.ForeignKey(Vehicle.vin), primary_key=True)
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    premium = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(1), nullable=False)

class CustomerInsurance(db.Model, UserMixin):
 cid = db.Column(db.Integer, db.ForeignKey(Customer.cid), primary_key=True)
 policy_id = db.Column(db.Integer, db.ForeignKey(Insurance.policy_id), primary_key=True)

# ***************************************
# ================ TABLES ================
# ***************************************
class CustomerInsurancesTable(Table):
    policy_id = Col('Policy Number')
    start_date = Col('Start Date')
    end_date = Col('End Date')
    premium = Col('Premium')
    status = Col('Status')

class CustomerInsurancesTable(Table):
    policy_id = Col('Policy Number')
    start_date = Col('Start Date')
    end_date = Col('End Date')
    premium = Col('Premium')

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

# ***************************************
# ================ ROUTES ===============
# ***************************************
# Homepage Route
@app.route("/")
@app.route("/home")
@login_required
def home():
    # form = HomeForm()
    # If user is admin, redirect him to admin panel
    username = current_user.username
    if username == "admin":
        return redirect(url_for("admin"))

    home_insurances = HomeInsurance.query.join(Insurance, HomeInsurance.policy_id == Insurance.policy_id )\
        .join(CustomerInsurance, CustomerInsurance.policy_id == Insurance.policy_id)\
        .filter(CustomerInsurance.cid == current_user.id).all()\
        #.load_only(HomeInsurance.policy_id, HomeInsurance.start_date, HomeInsurance.end_date, HomeInsurance.premium)\
        #.all()

    auto_insurances = AutoInsurance.query.join(Insurance, AutoInsurance.policy_id == Insurance.policy_id )\
        .join(CustomerInsurance, CustomerInsurance.policy_id == Insurance.policy_id)\
        .filter(CustomerInsurance.cid == current_user.id).all() \
        #.load_only(AutoInsurance.policy_id, AutoInsurance.start_date, AutoInsurance.start_end, AutoInsurance.premium)\
        #.all()

    home_table = CustomerInsurancesTable(home_insurances)
    auto_table = CustomerInsurancesTable(auto_insurances)

    this_user = User.query.filter_by(username=username).first()
    this_customer = Customer.query.filter_by(cid=this_user.id).first()
    if this_customer == None:
        is_customer = False
    else:
        is_customer = True

    return render_template("home.html", auto_table = auto_table, home_table=home_table, is_customer=is_customer)

# My Policies Route
@app.route("/mypolicies")
@login_required
def mypolicies():
    home_insurances = HomeInsurance.query.join(Insurance, HomeInsurance.policy_id == Insurance.policy_id ) \
        .join(CustomerInsurance, CustomerInsurance.policy_id == Insurance.policy_id) \
        .filter(CustomerInsurance.cid == current_user.id).all() \

    auto_insurances = AutoInsurance.query.join(Insurance, AutoInsurance.policy_id == Insurance.policy_id ) \
        .join(CustomerInsurance, CustomerInsurance.policy_id == Insurance.policy_id) \
        .filter(CustomerInsurance.cid == current_user.id).all() \

    return render_template("mypolicies.html", home_insurances= home_insurances, auto_insurance=auto_insurances)

# Login Route
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
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


# Logout Route
@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Forgot Password routes
def send_mail(user):
    token = user.get_token()
    msg = Message('Password Reset Request', recipients=[user.email], sender='bhargavamakwana@gmail.com')
    msg.body = f''' To reset password.
        {url_for('reset_token', token=token, _external=True)}
    '''
    mail.send(msg)

@app.route("/forgotpassword", methods=['GET', 'POST'])
def forgot_password():
    form = forms.ForgotPasswordForm()
    print("Calling here")
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first_or_404()
            print("Calling inside try!")
            print(user)
        except:
            print("Calling inside Except!")
            flash('Invalid email address!', 'error')
            return render_template('forgot_password.html', form=form)
        send_password_reset_link(user)
        flash('Please check your email for a password reset link.',
             'success')
        return redirect(url_for('login'))
    return render_template('forgot_password.html', form=form)


def send_password_reset_link(user):
     password_reset_serializer = URLSafeTimedSerializer(app.config)
     password_reset_url = url_for(
                      'reset_token',
                      token = password_reset_serializer.dumps(user.email, salt='password-reset-salt'),
                       _external=True)
     send_mail(user)


@app.route("/newautoinsurance", methods=['GET', 'POST'])
def add_auto_insurance():
    username = current_user.username
    this_user = User.query.filter_by(username=username).first()
    this_customer = Customer.query.filter_by(cid=this_user.id).first()
    print(f'AI {this_customer}')
    if this_customer == None:
        first_name= request.form.get("first_name")
        last_name= request.form.get("last_name")
        marital_status = request.form.get("marital_status")
        gender = request.form.get("gender")
        street = request.form.get("street")
        city = request.form.get("city")
        zipcode = request.form.get("zipcode")
        new_customer = Customer(cid=this_user.id, first_name=first_name, last_name=last_name, marital_status=marital_status, gender=gender, street=street, city=city, zipcode=zipcode)
        db.session.add(new_customer)
        # db.session.commit()
    vin = request.form.get("vin")
    make = request.form.get("make")
    model = request.form.get("model")
    year = request.form.get("year")
    status = request.form.get("status")
    dln = request.form.get("dln")
    state = request.form.get("state")
    first = request.form.get("first")
    last = request.form.get("last")
    dob = "1990-12-11" #request.form.get("dob")
    dob = datetime(int(dob.split("-")[0]), int(dob.split("-")[1]), int(dob.split("-")[2]))
    new_vehicle = Vehicle(vin=vin, make=make, model=model, year=year, status=status)
    db.session.add(new_vehicle)
    new_driver = Driver(dln=dln, state=state, first_name=first, last_name=last, dob=dob)
    db.session.add(new_driver)
    # db.session.commit()
    start_date=datetime(2022,1,1)
    end_date= datetime(2022,2,2)
    policy_id = random.randint(10000,1000000)
    new_auto_insurance = AutoInsurance(policy_id= policy_id, vin=vin ,start_date= start_date ,end_date=end_date , premium=200 , status ='C')
    db.session.add(new_auto_insurance)
    # db.session.commit()
    new_insurance=Insurance(policy_id=policy_id, policy_type='A')
    db.session.add(new_insurance)
    # db.session.commit()
    new_customer_insurance = CustomerInsurance(cid=current_user.id ,policy_id=policy_id)
    db.session.add(new_customer_insurance)
    db.session.commit()
    flash("Insurance application submitted!", "success")
    return redirect(url_for('home'))


@app.route("/forgotpassword/<token>", methods=['GET', 'POST'])
def reset_token(token):
    user = User.verify_token(token)
    if user is None:
        flash("Warning", "success")
        return redirect(url_for('forgot_password'))

    form = forms.ResetPasswordForm()
    if form.validate_on_submit():
        print("Inside reset token!")
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password=hashed_password
        db.session.commit()
        flash("Password Change Successful", "success")
        return redirect(url_for('login'))
    print("Before render template")
    return render_template("reset_password.html", form=form, token=token)

# Registration Route
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # Hashes password and stores in db on successful registration of a user
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account successfully created!", "success")
        return redirect(url_for('login'))

    return render_template("register.html", form=form)

# Admin Routes
@app.route("/admin")
@login_required
def admin():
    username = current_user.username
    if username == "admin":
        Users = User.query.all()
        return render_template("admin.html", users=Users)
    else:
        return redirect(url_for('home'))

@app.route("/admin/customers")
@login_required
def customers():
    username = current_user.username
    if username == "admin":
        Customers = Customer.query.all()
        return render_template("customers.html", customers=Customers)
    else:
        return redirect(url_for('home'))

@app.route("/admin/reports")
@login_required
def reports():
    username = current_user.username
    if username == "admin":
        return render_template("reports.html")
    else:
        return redirect(url_for('home'))

@app.route("/delete_user/<int:id>")
def delete_user(id):
    username = current_user.username
    if username == "admin":
        user_to_delete = User.query.get(id)
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('home'))


@app.route("/homeinsurance", methods=['GET', 'POST'])
def home_insurance_submit():
    hid = request.form.get("hid")
    username = current_user.username
    this_user = User.query.filter_by(username=username).first()
    this_customer = Customer.query.filter_by(cid=this_user.id).first()
    print(f'HI {this_customer}')
    if this_customer == None:
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        married_status = request.form.get("married")
        gender = request.form.get("gender")
        street = request.form.get("street")
        zip = request.form.get("zip")
        city = request.form.get("city")
        new_customer = Customer(cid=this_user.id, first_name=fname, last_name=lname, marital_status=married_status, gender=gender, street=street, city=city, zipcode=zip)
        db.session.add(new_customer)
        # db.session.commit()
    purchase_value = request.form.get("pval")
    area = request.form.get("area")
    aff = request.form.get("aff")
    hss = request.form.get("hss")
    bs = request.form.get("bs")
    pool = request.form.get("pool")
    house_type = request.form.get("house")
    purchase_date = request.form.get("date")
    dt = datetime.strptime(purchase_date, '%Y-%m-%d').date()
    start_date=datetime(2022,1,1)
    end_date= datetime(2022,2,2)
    policy_id = random.randint(10000,1000000)
    new_home = Home(hid=hid, purchase_date=dt, purchase_value=purchase_value, area=area, home_type=house_type, aff=aff, hss=hss, sp=pool, basement=bs, street=street, city=city, zipcode=zip)
    db.session.add(new_home)
    # db.session.commit()
    new_home_insurance = HomeInsurance(policy_id=policy_id, hid=hid, start_date=start_date, end_date=end_date, premium=200 , status ='C')
    db.session.add(new_home_insurance)
    # db.session.commit()
    new_insurance=Insurance(policy_id=policy_id, policy_type='H')
    db.session.add(new_insurance)
    # db.session.commit()
    new_customer_insurance = CustomerInsurance(cid=current_user.id, policy_id=policy_id)
    db.session.add(new_customer_insurance)
    db.session.commit()
    flash("Insurance application submitted!", "success")
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)