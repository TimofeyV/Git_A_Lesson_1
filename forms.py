from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    firsname = StringField('FirsName', validators=[DataRequired()])
    secondname = StringField('SecondName', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()]) 
    password = PasswordField('Password', validators=[DataRequired()])
