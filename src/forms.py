from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, EmailField
from wtforms.validators import DataRequired, Length, Email, ValidationError

def length_check(form,field):
    if len(field.data) == 0:
        raise ValidationError('Fields should not be null')
    

class AddPostForm(Form):
    title = StringField('Title', validators=[ DataRequired()])
    description = TextAreaField('Description', validators = [DataRequired()])

class SignUpForm(Form):
    firstname= StringField('First Name', validators= [DataRequired(), length_check])
    lastname = StringField('Last Name', validators= [DataRequired()])
    username = StringField('User Name', validators= [ DataRequired(), Length(min=4)])
    password = PasswordField('Password',validators=[ DataRequired(), Length(min=6)])
    email = EmailField('Email', validators= [DataRequired(), Email()])
    submit = SubmitField('Sign Up')


class SignInForm(Form):
    email = EmailField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=6, max=30)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In')

class AboutUserForm(Form):
    firstname= StringField('First Name', validators= [DataRequired(), length_check])
    lastname = StringField('Last Name', validators= [DataRequired()])
    username = StringField('User Name', validators= [ DataRequired(), Length(min=4)])
    password = PasswordField('Password',validators=[ DataRequired(), Length(min=6)])
    email = EmailField('Email', validators= [DataRequired(), Email()])
