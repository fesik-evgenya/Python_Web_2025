from flask_wtf import FlaskForm
from wtforms import (StringField,PasswordField,
                     BooleanField, SubmitField)
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired('Это обязательное поле')])
    password = PasswordField('Пароль', validators=[DataRequired('Без пароля нельзя')])
    remember_me = BooleanField('Запомнить меня', validators=[DataRequired('')])
    submit = SubmitField('Войти')