from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
class LoginForm(FlaskForm):
    code = StringField('账号',validators=[DataRequired('请输入用户名!'),Length(1, 20, '长度要介于(1-20)')])
    password = PasswordField('密码',validators=[DataRequired('请输入密码!'),Length(8, 128, '长度要介于(8-128)')])
    submit = SubmitField('登录')