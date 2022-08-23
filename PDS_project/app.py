# ***************************************
# =============== IMPORTS ===============
# ***************************************
import socket
from flask import Flask, render_template, url_for, redirect, flash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from flask_mail import Mail, Message
from wtforms import BooleanField, IntegerField, StringField, EmailField, PasswordField, RadioField, SubmitField, DateField
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

app.config['MAIL_SERVER'] = 'smtp@gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'johndopehere@gmail.com' 
app.config['MAIL_PASSWORD'] = 'Itshighnoon@71'

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
    submit = SubmitField("Send")

class ResetPassword(FlaskForm):
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Password"})
    confirm_password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField("Submit")

class CustomerInsurancesTable(Table):
    policy_id = Col('Policy Number')
    start_date = Col('Start Date')
    end_date = Col('End Date')
    premium = Col('Premium')
    status = Col('Status')

class CustomerForm(FlaskForm):
    cust_id = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Enter customer id"})
    fname = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter First Name"})
    lname = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Last Name"})
    street = StringField(validators=[InputRequired(), Length(min=4, max=40)], render_kw={"placeholder": "Enter Address"})
    city = StringField(validators=[InputRequired(), Length(min=4, max=40)], render_kw={"placeholder": "Enter City"})
    zipcode = IntegerField(validators=[InputRequired(), Length(5)], render_kw={"placeholder": "Enter Zip code"})
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    married_status = RadioField('Marital Status', choices=[('M', 'Married'), ('S', 'Single'), ('W', 'Widow')])
    #cust type field is not decalred. As discussed we assume that the person is the customer
    submit = SubmitField("Register")

# class HomeForm(FlaskForm):
#     purchase_value = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Enter Purchase Value"})
#     area = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Enter Area"})
#     aff = RadioField(validators=[InputRequired()])
#     hss = RadioField(validators=[InputRequired()])
#     basement = BooleanField(validators=[InputRequired()], render_kw={"placeholder": "Enter Basement"})
#     zipcode = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Enter Purchase Value"})
#     city = StringField(validators=[InputRequired(), Length(min=4, max=40)], render_kw={"placeholder": "Enter City"})
#     purchase_date = DateField(validators=[InputRequired()], render_kw={"placeholder": "Enter Date"})
#     street = StringField(validators=[InputRequired(), Length(min=4, max=40)], render_kw={"placeholder": "Enter Address"})
#     home_type = RadioField('Home Type', choices=[('S', 'Single Family'), ('M', 'Multi Family'), ('C', 'Condominium', 'T', 'Town House')])
#     pool = RadioField('Swimming pool', choices=[('U', 'Underground Pool'), ('O', 'Overground Pool'), ('I', 'Indoor Pool', 'M', 'Multiple Pool')])
#     submit = SubmitField("Register")

class VehicleForm(FlaskForm):
    vehicle_id = StringField(validators=[InputRequired(), Length(min=4, max=40)], render_kw={"placeholder": "Enter Vehicle ID number"})
    make = StringField(validators=[InputRequired(), Length(min=4, max=40)], render_kw={"placeholder": "Enter Vehicle make number"})
    model = StringField(validators=[InputRequired(), Length(min=4, max=40)], render_kw={"placeholder": "Enter Vehicle model"})
    year = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Enter Year of the vehicle purchased"})
    status = RadioField('Swimming pool', choices=[('L', 'Leased'), ('O', 'Owned'), ('F', 'Financed')])

class DriverForm(FlaskForm):
    dln = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Enter Driver license number"})
    state = StringField(validators=[InputRequired(), Length(min=4, max=40)], render_kw={"placeholder": "Enter State"})
    fname = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter First Name"})
    lname = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Last Name"})
    dob = DateField(validators=[InputRequired()], render_kw={"placeholder": "Enter Date of Birth"})

class HomeInsuranceForm(FlaskForm):
    policy_id = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Enter policy id"})
    h_id = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Enter home id"})
    start_date = DateField(validators=[InputRequired()], render_kw={"placeholder": "Enter Start Date"})
    end_date = DateField(validators=[InputRequired()], render_kw={"placeholder": "Enter End Date"})
    premium = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Enter Premium Amount"})
    status = RadioField('Home Type', choices=[('C', 'Current'), ('P', 'Expired')])

class AutoInsuranceForm(FlaskForm):
    policy_id = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Enter policy id"})
    vehicle_id = StringField(validators=[InputRequired(), Length(min=4, max=40)], render_kw={"placeholder": "Enter Vehicle ID number"})
    start_date = DateField(validators=[InputRequired()], render_kw={"placeholder": "Enter Start Date"})
    end_date = DateField(validators=[InputRequired()], render_kw={"placeholder": "Enter End date"})
    premium = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Enter Premium Amount"})
    status = RadioField('Home Type', choices=[('C', 'Current'), ('P', 'Expired')])

class PaymentForm(FlaskForm):
    # The actual table has couple of other fields but not sure if we need to take from the user or impute them with internal logic.
    paym_date = DateField(validators=[InputRequired()], render_kw={"placeholder": "Enter payment date"})
    method = RadioField('Payment Method', choices=[('PayPal'), ('Credit'), ('Debit'), ('Check')])

class CustomerInsurancesTable(Table):
    policy_id = Col('Policy Number')
    start_date = Col('Start Date')
    end_date = Col('End Date')
    premium = Col('Premium')

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

    # print(home_insurances)
    home_table = CustomerInsurancesTable(home_insurances)
    auto_table = CustomerInsurancesTable(auto_insurances)

    return render_template("home.html", auto_table = auto_table, home_table=home_table)

# My Policies Route
@app.route("/mypolicies")
@login_required
def mypolicies():
    return render_template("mypolicies.html")

# Login Route
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
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
    msg = Message('Password Reset Request', recipients=[user.email], sender='johndopehere@gmail.com')
    msg.body = f''' To reset password. 
        {url_for('reset_token', token=token, _external=True)}
    '''
    mail.send(msg)

@app.route("/forgotpassword", methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPassword()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_mail(user)
            print(user)
            flash("Password reset link sent", "success")
            return redirect(url_for('login'))
    return render_template("forgot_password.html", form=form)

@app.route("/forgotpassword/<token>", methods=['GET', 'POST'])
def reset_token(token):
    user = User.verify_token(token)
    if user is None:
        flash("Warning", "success")
        return redirect(url_for('forgot_password'))
    
    form = ResetPassword()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password=hashed_password
        db.session.commit()
        flash("Password Change Successful", "success")
        return redirect(url_for('login'))
    return render_template("reset_password.html", form=form)

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


if __name__ == "__main__":
    app.run(debug=True)