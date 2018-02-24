# coding:utf8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length

from ..model import Admin


class LoginForm(FlaskForm):
    '''
    管理员登录表单
    '''
    """注册表单"""

    account = StringField(label='账号'
                          , validators=[DataRequired('账号是必填写字段'), Length(6, 12, message=u'账号长度在6到20位')]
                          , description='账号'
                          , render_kw={
            "class": "form-control",
            "placeholder": "请您输入账号！",

        })
    pwd = PasswordField(label='密码'
                        , validators=[DataRequired('密码是必填写字段'), Length(6, 12, message=u'密码长度在6到12位')]
                        , description='密码'
                        , render_kw={
            "class": "form-control",
            "placeholder": "请您输入密码！",

        })
    submit = SubmitField(label='登录'
                         , render_kw={
            "class": "ui fluid large teal submit button"
        })

    def validate_account(self, field):
        account = field.data
        Admin_Account = Admin.query.filter_by(account=account).first()
        if Admin_Account == None:
            raise ValidationError('账号不存在,请使用命令创建')
