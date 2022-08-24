from flask import Flask, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
# from app import User
from wtforms import IntegerField, StringField, EmailField, PasswordField, RadioField, SubmitField, DateField
from wtforms.validators import InputRequired, Length, ValidationError

# class RegistrationForm(FlaskForm):
#     username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Username"})
#     email = EmailField(validators=[InputRequired()], render_kw={"placeholder": "Enter Email"})
#     password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Password"})
#     submit = SubmitField("Register")

#     # Validate if username is unique
#     def validate_username(self, username):
#         # Try to look through db to find a similar username
#         existing_user_username = User.query.filter_by(
#             username=username.data).first()
#         # If it founds a similar username in db it'll raise a validation error thus guaranting unique usernames
#         if existing_user_username:
#             flash("That username already exists. Please choose a different one.", "error")
#             raise ValidationError(
#                 'That username already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Password"})
    submit = SubmitField("Login")

class ForgotPasswordForm(FlaskForm):
    email = EmailField(validators=[InputRequired()], render_kw={"placeholder": "Enter Email"})
    submit = SubmitField("Send")

class ResetPasswordForm(FlaskForm):
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter Password"})
    confirm_password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField("Submit")

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