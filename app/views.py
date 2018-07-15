from flask import Flask, render_template
from app import app

from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupponsedtobesdfddecret!'

Bootstrap(app)

class LoginForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4,max=80)])
    remember = BooleanField('remember me')

class RegistrationForm(FlaskForm):
    email = StringField('email',validators=[InputRequired(), Email(message='Invalid email'),Length(max=50)])
    username = StringField('username',validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4,max=80)])

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def about():
    form = LoginForm()

    if form.validate_on_submit():
        return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html',form=form)


if __name__== '__main__':
    app.run()