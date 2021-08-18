from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import ValidationError, validators
from chat.models import User
class LoginForm(FlaskForm):
    code = StringField('账号',validators=[DataRequired('请输入用户名!'),Length(1, 20, '长度要介于(1-20)')])
    password = PasswordField('密码',validators=[DataRequired('请输入密码!'),Length(8, 128, '长度要介于(8-128)')])
    submit = SubmitField('登录')
class RegisterForm(FlaskForm):
    code = StringField('账号', validators=[DataRequired('请输入用户名!'), Length(1, 20, '长度要介于(1-20)')])
    password = PasswordField('密码', validators=[DataRequired('请输入密码!'), Length(8, 128, '长度要介于(8-128)'), EqualTo('password_confirm', message='密码不一致')])
    password_confirm = PasswordField('确认密码', validators=[DataRequired('请确认密码!')])
    email = StringField('邮箱', validators=[DataRequired('请输入邮箱!'), Email('邮箱格式不正确')])
    website = StringField('个人主页', [validators.optional()])
    github = StringField('GitHub', [validators.optional()])
    bio = TextAreaField('个人简介', [validators.optional()])
    submit = SubmitField('注册')

    def validate_code(self, field):
        if User.query.filter_by(code=field.data.lower()).first():
            raise ValidationError('账号已注册!')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('邮箱已注册!')